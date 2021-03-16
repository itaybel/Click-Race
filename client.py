import pygame
from network import Network
import threading
import pickle

width = 1500
height = 800
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
import time

def getPythonInput(event):
    if event.key == pygame.K_a:
        return str('a')
    if event.key == pygame.K_b:
        return str('b')
    if event.key == pygame.K_c:
        return str('c')
    if event.key == pygame.K_d:
        return str('d')
    if event.key == pygame.K_e:
        return str('e')
    if event.key == pygame.K_f:
        return str('f')
    if event.key == pygame.K_g:
        return str('g')
    if event.key == pygame.K_h:
        return str('h')
    if event.key == pygame.K_i:
        return str('i')
    if event.key == pygame.K_j:
        return str('j')
    if event.key == pygame.K_k:
        return str('k')
    if event.key == pygame.K_l:
        return str('l')
    if event.key == pygame.K_m:
        return str('m')
    if event.key == pygame.K_n:
        return str('n')
    if event.key == pygame.K_o:
        return str('o')
    if event.key == pygame.K_p:
        return str('p')
    if event.key == pygame.K_q:
        return str('q')
    if event.key == pygame.K_r:
        return str('r')
    if event.key == pygame.K_s:
        return str('s')
    if event.key == pygame.K_t:
        return str('t')
    if event.key == pygame.K_u:
        return str('u')
    if event.key == pygame.K_v:
        return str('v')
    if event.key == pygame.K_w:
        return str('w')
    if event.key == pygame.K_x:
        return str('x')
    if event.key == pygame.K_y:
        return str('y')
    if event.key == pygame.K_z:
        return str('z')
    if event.key == pygame.K_1:
        return str('1')
    if event.key == pygame.K_2:
        return str('2')
    if event.key == pygame.K_3:
        return str('3')
    if event.key == pygame.K_4:
        return str('4')
    if event.key == pygame.K_5:
        return str('5')
    if event.key == pygame.K_6:
        return str('6')
    if event.key == pygame.K_7:
        return str('7')
    if event.key == pygame.K_8:
        return str('8')
    if event.key == pygame.K_9:
        return str('9')
    if event.key == pygame.K_0:
        return str('0')

    if event.key == pygame.K_RETURN:
        return "return"

    return ""

def redrawWindow(win,game,p, n):

    win.fill((255,255,255))
    player = game.players[p]





    if  not game.connected():
        matchStartFont = pygame.font.SysFont('Comic Sans MS', 80)

        text_width, text_height = matchStartFont.size("The match cant start yet.")
        matchStartText = matchStartFont.render("The match cant start yet.", False, (10, 0, 0))


        win.blit(matchStartText, (win.get_width() // 2 - text_width // 2, win.get_height() // 2  - text_height // 2))

        pygame.draw.rect(win, (0, 255, 0), (player.x + 10, player.y + 70, 150, 15))

        player.update(win)


        pygame.display.update()

        pygame.draw.rect(win, (0, 255, 0), (player.x + 10, player.y + 70, 150, 15))


    else:

        colorFont = pygame.font.SysFont('Comic Sans MS', 30)
        colorText = colorFont.render('You are ' + player.car.split(".")[0], False, (10, 0, 0))
        win.blit(colorText, (0, 0))

        pygame.draw.rect(win, (0, 255, 0), (player.x + 10, player.y + 70, 150, 15))
        EndedPlayer = game.gameEnded()

        if EndedPlayer != False:
            #redrawWindow(win, game, player, n)
            pygame.time.delay(500)
            game = n.send("reset")


            winFont = pygame.font.SysFont('Comic Sans MS', 70)
            print(f"your x is {player.x}")
            winner = ""
            for playerInMatch in game.players:
                if playerInMatch.IsWon():
                    winner = playerInMatch

            print("winnerrrrrr", game.gameEnded())


            text = winFont.render(f"{EndedPlayer.car.split('.')[0]} Won!", 1, (10, 0, 0))

            win.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(3000)

        for i in game.players:
            i.update(win)

    pygame.display.update()

def threaded_client(n) :
    global game
    while True:
        data = pickle.loads(n.client.recv(2048))
        game = data



def decrypt(string):
    stringAsArray = string.split("_")
    encryption = {'cgxmr5': 'a', 'p61ksb': 'b', 'vy7y2i': 'c', '85qyp6': 'd', 'mrwtv1': 'e', 'ld26qd': 'f', 'y7azjm': 'g', 'cssr8c': 'h', 'b6u3cq': 'i', 'h3hoy3': 'j', 'j8iyt6': 'k', 'fuyqvm': 'l', 'mp2qd4': 'm', 'm2yfka': 'n', 'gkm63u': 'o', 'vv75k4': 'p', 'pjgcpp': 'q', 'n0qvhu': 'r', 'uk4nc9': 's', '5eebui': 't', 'ulvvmn': 'u', 'lne008': 'v', '7gewba': 'w', 'krgjkm': 'x', '0vtpbz': 'y', 'cjvu39': 'z', 'o1xf3q': '1', 'r9t7qi': '2', '5isjif': '3', '9rpugk': '4', 'ffxb83': '5', 'xd325a': '6', 'rw5wfl': '7', 'ha7t44': '8', 'ak5a6r': '9', '621qv1': '0', 'ope3qs': ' '}

    return "".join([encryption[i] for i in stringAsArray])

def main(n, Hosting):

    n.ishosting = Hosting

    pygame.font.init()


    run = True

    gameIdEnrypt = n.getGameId()
    gameInfo = {}
    for key, value in gameIdEnrypt.items():
        gameInfo[key] = decrypt(value)

    print(gameIdEnrypt)

    player = int(gameInfo["playerId"])
    fps = int(gameInfo["fps"])
    speed = int(gameInfo["speed"])


    clock = pygame.time.Clock()


    #thread = threading.Thread(target=threaded_client, args=(n,))
    #thread.start()
    while run:
        clock.tick(fps)
        #game = pickle.loads(n.client.recv(2048))


        try:
            game = n.send("get")

        except:
            run = False
            exit()
            break






        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and game.connected():
                game.move(player, win)
                o = n.send("newx," + str(game.players[player].x + speed) + "," + str(player))

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


        redrawWindow(win, game, player, n)

def getClickedBtn(btns, pos):
    x = pos[0]
    y = pos[1]

    if type(btns) == list:

        for btn in btns:
            if (x >= btn.x and x <= (btn.width + btn.x)) and (y >= btn.y and y <= (btn.height + btn.y)):
                return (btn, btns.index(btn))


    else:
        if (x >= btns.x and x <= (btns.width + btns.x)) and (y >= btns.y and y <= (btns.height + btns.y)):
            return True
        else:
            return False

def checkCode(n, code):

    used_codes = #how tf can I know the used codes, I mean, I dont know to what I need to change my server code


def join_game_screen(n):
    pygame.font.init()
    run = True
    clock = pygame.time.Clock()

    gameCode = ""
    while run:
        clock.tick(60)
        win.fill((160, 160, 160))
        font = pygame.font.SysFont("calibri", 100)

        #info text
        infoFont = pygame.font.SysFont("calibri", 60)
        text = infoFont.render("Please enter the code of the match", 1, (0, 0, 0))
        win.blit(text, (width // 2 - text.get_width() // 2, 50))


        # Play button

        StartButtonWidth = 450
        StartButtonHeight = 115

        StartButtonX = win.get_width() // 2 - StartButtonWidth // 2
        StartButtonY = 500

        playBtn = pygame.draw.rect(win, (0, 0, 0), (StartButtonX, StartButtonY, StartButtonWidth, StartButtonHeight),width=4)


        text = font.render("Join", 1, (0, 0, 0))
        win.blit(text, (width / 2 - text.get_width() / 2, 510))

        # Type Text button


        textFont = pygame.font.SysFont("calibri", 70)

        text = font.render(gameCode, 1, (0, 0, 0))
        pygame.draw.rect(win, (255, 255, 255), (490  , 310, 500, 100))


        win.blit(text, (width / 2 - text.get_width() / 2, 310))



        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                Joined = getClickedBtn(playBtn)
                if Joined:
                    checkCode(n, gameCode)

            if event.type == pygame.KEYDOWN:
                if event.key == 8:
                    gameCode = gameCode[:-1]

                elif len(gameCode) < 7:

                    if event.key == 8:
                        gameCode = gameCode[:-1]

                    else:
                        gameCode += getPythonInput(event)



def menu_screen(n):
    pygame.font.init()
    run = True
    clock = pygame.time.Clock()

    hostGame = False
    JoinGame = False

    while run:
        clock.tick(60)
        win.fill((160, 160, 160))
        font = pygame.font.SysFont("calibri", 100)

        # Play button

        StartButtonWidth = 450
        StartButtonHeight = 115

        StartButtonX = win.get_width() // 2 - StartButtonWidth // 2
        StartButtonY = 100

        playBtn = pygame.draw.rect(win, (0, 0, 0), (StartButtonX, StartButtonY, StartButtonWidth, StartButtonHeight),width=4)


        text = font.render("Play", 1, (0, 0, 0))
        win.blit(text, (width / 2 - text.get_width() / 2, 120))

        # Host Private Game

        HostGamedListButtonWidth = 650
        HostGameButtonHeight = 115

        HostGameButtonX = win.get_width() // 2 - HostGamedListButtonWidth // 2
        HostGameButtonY = 300


        HostGameBtn = pygame.draw.rect(win, (0, 0, 0), (
            HostGameButtonX, HostGameButtonY, HostGamedListButtonWidth, HostGameButtonHeight),
                         width=4)
        HostAGamefont = pygame.font.SysFont("calibri", 70)

        text = HostAGamefont.render("Host A Private Game", 1, (0, 0, 0))
        win.blit(text, (width / 2 - text.get_width() / 2, 320))

        # Join Private Game

        JoinGamedListButtonWidth = 650
        JoinGameButtonHeight = 115

        JoinGameButtonX = win.get_width() // 2 - JoinGamedListButtonWidth // 2
        JoinGameButtonY = 500

        JoinGameBtn = pygame.draw.rect(win, (0, 0, 0), (
            JoinGameButtonX, JoinGameButtonY, JoinGamedListButtonWidth, JoinGameButtonHeight),
                                       width=4)
        JoinAGamefont = pygame.font.SysFont("calibri", 70)

        text = JoinAGamefont.render("Join A Private Game", 1, (0, 0, 0))
        win.blit(text, (width / 2 - text.get_width() / 2, 520))


        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:


                mousePos = pygame.mouse.get_pos()
                AllButtonsRects = [playBtn, HostGameBtn, JoinGameBtn]
                btnInfo = getClickedBtn(btns=AllButtonsRects, pos=mousePos)
                if btnInfo != None:

                    clickedBtn = btnInfo[0]
                    btnIndex = btnInfo[1]

                    if btnIndex == 0: #if its the play btn
                        run = False
                        main(False)

                        return
                    if btnIndex == 1: #if its the host  btn
                        hostGame = True
                        run = False

                    if btnIndex == 2: #if its the join btn
                        JoinGame = True
                        run = False


    if hostGame:
        main(n, Hosting=True)

    if JoinGame:
        join_game_screen(n)
    else:
        main(n, Hosting=False)









n = Network()
menu_screen(n)