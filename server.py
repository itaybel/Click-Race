
import socket
import threading
import pickle
from game import Game
import requests
import json
import random

server = "10.0.0.2"


port = 6003

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen(5)
print("Waiting for a connection, Server Started")

connected = set() #its going to be the connection ips
games = {}
HostedGames = {}

idCount = 0
HostedGamesCount = 0

def encrypt(string):
    encryption = {'a': 'cgxmr5', 'b': 'p61ksb', 'c': 'vy7y2i', 'd': '85qyp6', 'e': 'mrwtv1', 'f': 'ld26qd', 'g': 'y7azjm', 'h': 'cssr8c', 'i': 'b6u3cq', 'j': 'h3hoy3', 'k': 'j8iyt6', 'l': 'fuyqvm', 'm': 'mp2qd4', 'n': 'm2yfka', 'o': 'gkm63u', 'p': 'vv75k4', 'q': 'pjgcpp', 'r': 'n0qvhu', 's': 'uk4nc9', 't': '5eebui', 'u': 'ulvvmn', 'v': 'lne008', 'w': '7gewba', 'x': 'krgjkm', 'y': '0vtpbz', 'z': 'cjvu39', '1': 'o1xf3q', '2': 'r9t7qi', '3': '5isjif', '4': '9rpugk', '5': 'ffxb83', '6': 'xd325a', '7': 'rw5wfl', '8': 'ha7t44', '9': 'ak5a6r', '0': '621qv1', " ": "ope3qs"}
    return ("".join([encryption[i] + "_" for i in string]))[:-1]



def threaded_client(conn, p, gameId, gameType):


    gameInfo = {
        "playerId" : str(p),
        "fps": "30",
        "speed": "24"
    }


    NewGameInfo = {}
    for key, value in gameInfo.items():
        NewGameInfo[key] = encrypt("".join([i for i in value]))




    conn.send(pickle.dumps(NewGameInfo))
    global idCount
    reply = ""
    while True:
        if True:
            try:
                data = conn.recv(4096).decode()
            except:
                data = pickle.loads(conn.recv(4096))

            if gameType == "regular":
                if gameId in games:
                    game = games[gameId]

                    if not data:
                        break

                    else:

                        if "newx" in data:
                            newX = int(data.split(",")[1])
                            playerId = int(data.split(",")[2])

                            game.players[playerId].x = newX




                        if data == "reset":
                            game.resetWent()

                        if "code" in data:
                            print("got code")
                            code = data.split("_")[1]
                            if code in HostedGames.keys():
                                game = HostedGames[code]
                                conn.send(pickle.dumps("true"))
                                # join shit

                            else:
                                conn.send(pickle.dumps("false"))
                        conn.sendall(pickle.dumps(game))
                else:
                    break

            else:

                game = HostedGames[gameId]

                if not data:
                    break

                else:

                    if "newx" in data:
                        newX = int(data.split(",")[1])
                        playerId = int(data.split(",")[2])

                        game.players[playerId].x = newX




                    if data == "reset":
                        game.resetWent()

                    if "code" in data:
                        code = data.split("_")[1]
                        print("HostedGames", HostedGames)
                        print("code", code)

                        if code in HostedGames.keys():
                            game = HostedGames[code]
                            conn.send(pickle.dumps("true"))
                            game.ready = True
                            print("Game is starting")
                            # join shit

                        else:
                            conn.send(pickle.dumps("false"))

                    if  "matchstart" in data:
                        matchCode = int(data.split("_"))
                        print("got matchstart")
                        HostedGames[matchCode].ready = True




        conn.sendall(pickle.dumps(game))

    if gameType == "regular":
        try:
            del games[gameId]
        except:
            pass

        idCount -= 1
    else:
        try:
            del HostedGames[gameId]
        except:
            pass

    conn.close()


def generate_game_code():
    chars = "abcdefghijklmnopqrstuvwxyz1234567890"

    code = ""
    for i in range(7):
        code += random.choice(chars)
    print(code)
    return code

while True:
    conn, addr = s.accept()
    IsHosting = pickle.loads(conn.recv(2048))
    print("Connected to:", addr)

    if IsHosting:
        code = generate_game_code()
        conn.sendall(str.encode(code))

        HostedGames[code] = Game(HostedGamesCount)
        print(addr[0] + " Game is", code)

        p = 0
        thread = threading.Thread(target=threaded_client, args=(conn, p, code, "private"))
        thread.start()

    else:
        print("connected")
        idCount += 1 #adding the people who connected
        p = 0
        gameID = (idCount - 1) // 2

        if idCount % 2 == 1: #if we need to create a new game
            games[gameID] = Game(gameID)
            print("Creating a new game...")
        else:
            games[gameID].ready = True
            p = 1


        thread = threading.Thread(target=threaded_client, args=(conn, p, gameID, "regular"))
        thread.start()
