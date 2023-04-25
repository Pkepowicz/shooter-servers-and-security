import socket
import pickle
from player import Player
from projectile import Projectile
from functools import singledispatchmethod


class Network:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "127.0.1.1"
        self.port = 5555
        self.address = (self.server, self.port)
        # self.p = self.connect()

    def connect(self):
        try:
            self.socket.connect(self.address)
            # self.socket.send(pickle.dumps({'game_name': game_name, 'max_players': max_players}))
            return pickle.loads(self.socket.recv(2048))
        except socket.error as e:
            raise e

    @singledispatchmethod
    def send(self, game_object):
        pass

    @send.register
    def _(self, game_object: Player):
        try:
            self.socket.send(pickle.dumps(game_object))
            try:
                return pickle.loads(self.socket.recv(2048))
            except Exception as e:
                print(e)
        except socket.error as se:
            print(se)

    @send.register
    def _(self, game_object: Projectile):
        try:
            self.socket.send(pickle.dumps(game_object))
        except socket.error as se:
            print(se)
