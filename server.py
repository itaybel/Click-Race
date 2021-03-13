
import socket
import threading
import pickle
from game import Game


server = "93.172.68.96"
port = 6001

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
try:
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen(5)
print("Waiting for a connection, Server Started")

connected = set() #its going to be the connection ips
games = {}
idCount = 0



def threaded_client(conn, p, gameId):
    p = str.encode(str(p))
    conn.send(p) #its going to send to the player what player they are
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


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1 #adding the people who connected
    p = 0
    gameID = (idCount - 1) // 2

    if idCount % 2 == 1: #if we need to create a new game
        games[gameID] = Game(gameID)
        print("Creating a new game...")
    else:
        games[gameID].ready = True
        p = 1


    thread = threading.Thread(target=threaded_client,args=(conn, p, gameID))
    thread.start()
