
import socket
import threading
import pickle
from game import Game


server = "10.0.0.2"


port = 6000

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


def threaded_client(conn, p, gameId, gameType):


    while True:
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

