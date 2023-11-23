import socket
import threading

class Cliente:
    def __init__(self, username, socket):
        self.username = username
        self.socket = socket

class Partida:
    def __init__(self, cliente1, cliente2):
        self.cliente1 = cliente1
        self.cliente2 = cliente2
