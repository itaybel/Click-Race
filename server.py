
import socket
import threading
import pickle
from game import Game
import requests
import json
import random
def MyIpAddress():
    resp = requests.get('https://ident.me/')
    return resp.text


#server = MyIpAddress()
server = "10.0.0.2"


port = 6002

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



def threaded_client(conn, p, gameId, IsHosting):


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
        try:
            data = conn.recv(4096).decode()


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




                    conn.sendall(pickle.dumps(game))
            else:
                break

        except:
            break

    try:
        del games[gameId]
    except:
        pass

    idCount -= 1
    conn.close


def generate_game_code():
    chars = "abcdefghijklmnopqrstuvwxyz1234567890"

    code = ""
    for i in range(7):
        code += random.choice(chars)

    return code

while True:
    conn, addr = s.accept()
    IsHosting = pickle.loads(conn.recv(2048))
    print("IsHosting", IsHosting)
    print("Connected to:", addr)

    if IsHosting:
        HostedGames[HostedGamesCount] = Game(HostedGamesCount, code=generate_game_code())
        p = 0
        thread = threading.Thread(target=threaded_client, args=(conn, p, HostedGamesCount, True))
        thread.start()

    else:

        idCount += 1 #adding the people who connected
        p = 0
        gameID = (idCount - 1) // 2

        if idCount % 2 == 1: #if we need to create a new game
            games[gameID] = Game(gameID)
            print("Creating a new game...")
        else:
            games[gameID].ready = True
            p = 1


        thread = threading.Thread(target=threaded_client, args=(conn, p, gameID, False))
        thread.start()