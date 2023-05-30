import socket
from threading import Thread
from player import Player
import pickle
from game import Game
from projectile import Projectile
from encryptor import Encryptor
from constants import SERVER_ADDRESS, SERVER_PORT


class Server:
    def __init__(self):
        self.games = []
        self.server_ip_address = SERVER_ADDRESS
        self.port = SERVER_PORT
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.encryptor = Encryptor("mypassword")
        self.encrypted = False

        if self.bind_socket():
            self.run_server()

    def bind_socket(self):
        try:
            self.socket.bind((self.server_ip_address, self.port))
            return True
        except socket.error as e:
            print(e)
            return False

    def run_server(self):
        self.socket.listen(2)
        print("Server started")
        while True:
            try:
                connection, address = self.socket.accept()
                thread = Thread(target=self.threaded_client, args=(connection, address))
                thread.start()
            except KeyboardInterrupt:
                break
        self.socket.close()

    def threaded_client(self, connection, address):
        print("Connected to: ", address)

        game = self.add_client_to_game(address)
        self.send_client_setup_response(connection, game)
        self.game_loop(address, connection, game)
        if game in self.games and not game.players:
            self.games.remove(game)
        print("Disconnected: ", address)
        connection.close()

    def add_client_to_game(self, address):
        game = self.get_game_instance()
        game.join_new_player()
        return game

    def get_game_instance(self):
        for game in self.games:
            if game.can_player_join():
                return game
        return self.create_new_game()

    def create_new_game(self):
        new_game = Game(len(self.games), 2)
        self.games.append(new_game)
        return new_game

    def send_client_setup_response(self, connection, game):
        if self.encrypted:
            connection.send(self.encryptor.encrypt(pickle.dumps(game.get_last_player_joined())))
        else:
            connection.send(pickle.dumps(game.get_last_player_joined()))

    def game_loop(self, address, connection, game):
        while True:
            try:
                if received := pickle.loads((connection.recv(2048) if not self.encrypted else self.encryptor.decrypt(connection.recv(2048)))):
                    print(f'Game: {game.id}, received data: {received} from {address}')
                    self.process_and_response(game, received, connection)
                else:
                    break
            except (EOFError, ConnectionError) as e:
                print(str(e))
                break

    def process_and_response(self, game, received, connection):
        if isinstance(received, Player):
            game.update_player(received)
            if game.players:
                other_players = game.get_other_players(received)
                projectiles = game.get_other_projectiles()
                if self.encrypted:
                    connection.sendall(self.encryptor.encrypt(pickle.dumps((other_players, projectiles))))
                else:
                    connection.sendall(pickle.dumps((other_players, projectiles)))
            else:
                pass
        elif isinstance(received, Projectile):
            game.update_projectiles(received)


server = Server()
