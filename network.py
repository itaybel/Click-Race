"10.0.0.1"

import socket
import pickle


class Network:
    def __init__(self, ishosting):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "10.0.0.2"
        self.ishosting = ishosting

        self.port = 6003
        self.addr = (self.server, self.port)
        self.gameId = self.connect()





    def getGameId(self):
        return self.gameId

    def get(self):
        return self.client.recv(2048)




    def connect(self):
        self.client.connect(self.addr)
        self.client.send(pickle.dumps(self.ishosting))
        if self.ishosting:
            self.gameCode =  self.client.recv(2048).decode()

        return pickle.loads(self.client.recv(2048))


    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)