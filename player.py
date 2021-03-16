#dick
import pygame
from os import listdir
from os.path import isfile, join
import random
class Player():
    def __init__(self, x, y, car):

        self.x = x
        self.y = y
        self.car = car

        self.pos = [x, y]
        self.seeAble = True
        self.matchStarted = False
        self.TimerInZero = False
        self.speed = 3
        self.IsWinner = False
        self.canWin = True
        self.GameEnded = False
        self.timer = 10


        pygame.init()

    def move(self, win):
        self.pos = [self.pos[0] + self.speed, self.pos[1]]
        self.x += self.speed

    def IsWon(self):
        return self.x >= 1470




    def draw(self, win):
        carIMG = pygame.image.load("cars/" + self.car)
        carRect = carIMG.get_rect()
        carRect.x , carRect.y = self.x, self.y
        win.blit(carIMG, carRect)




    def update(self, win):
        self.draw(win)