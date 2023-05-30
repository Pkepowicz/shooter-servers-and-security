import socket
import pickle
from encryptor import Encryptor
from player import Player
from projectile import Projectile
from constants import SERVER_ADDRESS, SERVER_PORT


class Network:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = SERVER_ADDRESS
        self.port = SERVER_PORT
        self.address = (self.server, self.port)
        self.encryptor = Encryptor("mypassword")
        self.encrypted = False
        # self.p = self.connect()

    def connect(self):
        try:
            self.socket.connect(self.address)
            if self.encrypted:
                return pickle.loads(self.encryptor.decrypt(self.socket.recv(2048)))
            else:
                return pickle.loads(self.socket.recv(2048))

        except socket.error as e:
            raise e

    def send_player(self, game_object: Player):
        try:
            if self.encrypted:
                self.socket.send(self.encryptor.encrypt(pickle.dumps(game_object)))
            else:
                self.socket.send(pickle.dumps(game_object))
            try:
                if self.encrypted:
                    return pickle.loads(self.encryptor.decrypt(self.socket.recv(2048)))
                else:
                    return pickle.loads(self.socket.recv(2048))
            except Exception as e:
                print(e)
        except socket.error as se:
            print(se)

    def send_projectile(self, game_object: Projectile):
        try:
            if self.encrypted:
                self.socket.send(self.encryptor.encrypt(pickle.dumps(game_object)))
            else:
                self.socket.send(pickle.dumps(game_object))
        except socket.error as se:
            print(se)
