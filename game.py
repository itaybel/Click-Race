import pygame
from os import listdir
from os.path import isfile, join
import random
from player import Player

class Game:
    def __init__(self, id):

        self.ready = False
        self.id = id
        self.wins = [0,0]
        self.ties = 0
        self.players = [Player(70, 200), Player(70,400)]

    def getPlayer(self, p):

        return self.players[p]

    def move(self, player, win):
        self.players[player].move(win)


    def connected(self):
        return self.ready

    def gameEnded(self):

        return self.players[0].x >= 1502 or self.players[1].x >= 1502

    def winner(self):

        p1 = self.players[0].x
        p2 = self.players[1].x


        print(f"player1 {p1}\nplayer2{p2}")
        if self.players[0].x >= 1502:
            return self.players[0].car.replace(".png", "")
        elif self.players[1].x >= 1502:
            return self.players[1].car.replace(".png", "")



    def resetWent(self):
        print("reset")
        self.players = [Player(70, 200), Player(70,400)]

