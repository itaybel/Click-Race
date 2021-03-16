import pygame
from os import listdir
from os.path import isfile, join
import random
from player import Player

class Game:
    def __init__(self, id, code=None):

        self.ready = False
        self.id = id
        self.wins = [0,0]
        self.ties = 0
        self.cars = [f for f in listdir("cars") if isfile(join("cars", f))]
        player1Car = random.choice(self.cars)
        newCars = [car for car in self.cars if car != player1Car]
        player2Car = random.choice(newCars)
        self.players = [Player(70, 200, player1Car), Player(70,400, player2Car)]

        if code != None:
            self.code = code

    def getPlayer(self, p):

        return self.players[p]

    def move(self, player, win):
        self.players[player].move(win)


    def connected(self):
        return self.ready

    def gameEnded(self):

        print(f"Player 1 x: {self.players[0].x}")
        print(f"Player 2 x: {self.players[1].x}")

        for i in self.players:
            if i.x >= 1470:
                return i

        return self.players[0].x >= 1470 or self.players[1].x >= 1470

    def winner(self):

        p1 = self.players[0].x
        p2 = self.players[1].x


        if self.players[0].x >= 1470:
            return self.players[0].car.replace(".png", "")
        elif self.players[1].x >= 1470:
            return self.players[1].car.replace(".png", "")



    def resetWent(self):
        player1Car = random.choice(self.cars)
        newCars = [car for car in self.cars if car != player1Car]
        player2Car = random.choice(newCars)
        self.players = [Player(70, 200, player1Car), Player(70, 400, player2Car)]
