"10.0.0.1"

import socket
import pickle

#"62.171.179.32"
class Network:
    def __init__(self, ishosting, IsJoining=False,compInfo=(False, False, None),  code=None, StartGame=True, justAddId=False):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = 6006
        self.server = "10.0.0.16"

        self.addr = (self.server, self.port)
        self.code = code

        if not justAddId:
            self.ishosting = ishosting
            self.IsJoining = IsJoining
            self.compInfo = compInfo

            self.StartGame = StartGame
            self.gameId = self.connect()

        else:
            self.client.connect(self.addr)
            self.client.send(pickle.dumps([self.code]))

    def getGameId(self):
        return self.gameId

    def get(self):
        return self.client.recv(2048)




    def connect(self):
        self.client.connect(self.addr)
        self.client.send(pickle.dumps([self.ishosting, self.IsJoining, self.compInfo,  self.code]))
        if self.ishosting:
            self.gameCode =  self.client.recv(2048).decode()
        if self.StartGame:
            gotFromServer = pickle.loads(self.client.recv(2048))
            print("got ", gotFromServer)
            return gotFromServer


    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)