import pygame
from network import Network
import threading
import pickle
import os.path

import random
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

def redrawWindow(win,game,p, n, Hosting=False, Joining=False, isComp=False):

    win.fill((255,255,255))
    player = game.players[p]







    if  not game.connected():
        matchStartFont = pygame.font.SysFont('Comic Sans MS', 80)

        text_width, text_height = matchStartFont.size("The match cant start yet.")
        matchStartText = matchStartFont.render("The match cant start yet.", False, (10, 0, 0))

        if Hosting or Joining:
            font = pygame.font.SysFont("calibri", 60)
            text = font.render(f"Match Code: {n.gameCode}", 1, (0, 0, 0))
            win.blit(text, (width // 2 - text.get_width() // 2, 50))

        win.blit(matchStartText, (win.get_width() // 2 - text_width // 2, win.get_height() // 2  - text_height // 2))
        if not game.gameEnded():

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
            pygame.time.delay(500)
            if Hosting:
                game = n.send("reset")


            winFont = pygame.font.SysFont('Comic Sans MS', 70)
            winner = ""
            for playerInMatch in game.players:
                if playerInMatch.IsWon():
                    winner = playerInMatch


            if isComp:
                n.send(f"winner_{get_player_id()}")
            text = winFont.render(f"{EndedPlayer.car.split('.')[0]} Won!", 1, (10, 0, 0))

            win.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(3000)

            menu_screen()
            return

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

IsInMenu = False


def main(n=None, Hosting=False, comp=False, Joining=False):
    IsInMenu = False
    if n == None:
        n = Network(Hosting, compInfo= (comp, False, None))




    pygame.font.init()


    run = True

    gameIdEnrypt = n.getGameId()


    gameInfo = {}
    for key, value in gameIdEnrypt.items():
        gameInfo[key] = decrypt(value)


    player = int(gameInfo["playerId"])

    fps = int(gameInfo["fps"])
    speed = int(gameInfo["speed"])



    clock = pygame.time.Clock()



    while run:
        pygame.mixer.music.stop()
        clock.tick(fps)

        game = n.send("get")


        #game = pickle.loads(n.client.recv(2048))




        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and game.connected():
                game.move(player, win)
                o = n.send("newx," + str(game.players[player].x + speed) + "," + str(player))

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        redrawWindow(win, game, player, n, Hosting, isComp=comp, Joining=Joining)





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

    n.send("code_" + code)


    IsFound = pickle.loads(n.client.recv(2048)) #here the error, it doesnt get is found


    if IsFound == "false":
        IsFound = False
    else:
        IsFound = True

    return IsFound





def join_game_screen(n=None):


    pygame.font.init()
    run = True
    clock = pygame.time.Clock()

    gameCode = ""
    IsNotFound = False
    while run:
        clock.tick(60)
        win.fill((160, 160, 160))
        font = pygame.font.SysFont("calibri", 100)



        #info text
        infoFont = pygame.font.SysFont("calibri", 60)
        text = infoFont.render("Please enter the code of the match", 1, (0, 0, 0))
        win.blit(text, (width // 2 - text.get_width() // 2, 50))

        #not found text
        notfoundFont = pygame.font.SysFont("calibri", 60)
        text = notfoundFont.render("Invalid Code", 1, (255, 0, 0))
        if IsNotFound:
            win.blit(text, (width // 2 - text.get_width() // 2, win.get_height() - 100))
            pygame.time.delay(1000)
            join_game_screen()
            return


        # Play button

        StartButtonWidth = 450
        StartButtonHeight = 115

        StartButtonX = win.get_width() // 2 - StartButtonWidth // 2
        StartButtonY = 500

        playBtn = pygame.draw.rect(win, (0, 0, 0), (StartButtonX, StartButtonY, StartButtonWidth, StartButtonHeight),width=4)

        backImg = pygame.image.load("images/back.png")
        backRect = backImg.get_rect()
        backRect.x, backRect.y = (0, 0)
        win.blit(backImg, backRect)



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
                btnClicked = getClickedBtn([playBtn, backRect], pygame.mouse.get_pos())
                if btnClicked is None:
                    btnClicked = [-1, -1]
                if btnClicked[1] == 0:



                    n = Network(False, IsJoining=True, code=gameCode) #here it crashes

                    IsFound = checkCode(n, gameCode)
                    if not IsFound:
                        IsNotFound = True

                    else:

                        main(n, False, Joining=True)

                if btnClicked[1] == 1:
                    menu_screen()


            if event.type == pygame.KEYDOWN:
                if event.key == 8:
                    gameCode = gameCode[:-1]

                elif len(gameCode) < 7:

                    if event.key == 8:
                        gameCode = gameCode[:-1]

                    else:
                        gameCode += getPythonInput(event)

def private_game_menu():
    pygame.font.init()
    run = True
    clock = pygame.time.Clock()




    while run:
        clock.tick(60)
        win.fill((160, 160, 160))
        font = pygame.font.SysFont("calibri", 80)


        #Back btn

        backImg = pygame.image.load("images/back.png")
        backRect = backImg.get_rect()
        backRect.x, backRect.y = (0, 0)
        win.blit(backImg, backRect)


        # Host Game button

        HostButtonWidth = 690
        HostButtonHeight = 145

        HostButtonX = win.get_width() // 2 - HostButtonWidth // 2
        HostButtonY = 100

        HostGameBtn = pygame.draw.rect(win, (0, 0, 0), (HostButtonX, HostButtonY, HostButtonWidth, HostButtonHeight),
                                   width=4)

        text = font.render("Host A Private Game", 1, (0, 0, 0))
        win.blit(text, (width / 2 - text.get_width() / 2, 135))

        # Join Game button

        JoinButtonWidth = 690
        JoinButtonHeight = 145

        JoinButtonX = win.get_width() // 2 - JoinButtonWidth // 2
        JoinButtonY = 335

        JoinGameBtn = pygame.draw.rect(win, (0, 0, 0), (JoinButtonX, JoinButtonY, JoinButtonWidth, JoinButtonHeight),
                                   width=4)

        text = font.render("Join A Private Game", 1, (0, 0, 0))
        win.blit(text, (width / 2 - text.get_width() / 2, 365))



        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                mousePos = pygame.mouse.get_pos()
                AllButtonsRects = [HostGameBtn, JoinGameBtn, backRect]
                btnInfo = getClickedBtn(btns=AllButtonsRects, pos=mousePos)
                if btnInfo != None:

                    clickedBtn = btnInfo[0]
                    btnIndex = btnInfo[1]


                    if btnIndex == 0: #if its the host  btn
                        main(None, Hosting=True)
                        return
                        run = False

                    if btnIndex == 1: #if its the join btn
                        join_game_screen()
                        return

                    if btnIndex == 2:
                        menu_screen()
                        return



def get_player_id():
    playerInfo = open("playerInfo.txt", "r")
    return playerInfo.read()

def comp_menu():
    pygame.font.init()
    run = True
    clock = pygame.time.Clock()

    playerId = get_player_id()

    n = Network(ishosting=False, compInfo=(True, True, playerId), StartGame=False)

    rankInPoints = pickle.loads(n.client.recv(2048))
    print(rankInPoints)

    ranksDic = {
        range(0, 300) :"Bronze",
        range(300, 606): "Silver",
        range(600, 900): "Gold",
        range(900, 1200): "Emerald",
        range(1200, 10000): "Elite",

    }

    colorsDic = {
        "Bronze" : (205, 127, 50),
        "Silver": (192, 192, 192),
        "Gold": (255, 215, 0),
        "Emerald": (80, 200, 120),
        "Elite": (1, 55, 125)
    }

    while run:
        clock.tick(60)
        win.fill((160, 160, 160))
        font = pygame.font.SysFont("calibri", 80)
        CPfont = pygame.font.SysFont("calibri", 60)
        RankFont = pygame.font.SysFont("calibri", 100)

        playerRank = "Invalid"

        for i in ranksDic.keys():
            if rankInPoints in i:
                playerRank = ranksDic[i]

        try:
            text = RankFont.render(f"Your rank is {playerRank}", 1, colorsDic[playerRank])
        except:
            text = RankFont.render(f"Your rank is {playerRank}", 1, (0, 0 , 0))

        win.blit(text, (width / 2 - text.get_width() / 2, 50))

        print(playerRank)
        if playerRank == "Invalid":
            text = CPfont.render(f"You have 0 competitive points", 1, (0, 0, 0))
        else:
            text = CPfont.render(f"You have {rankInPoints} competitive points", 1, (0, 0, 0))
        win.blit(text, (width / 2 - text.get_width() / 2, 220))

        # Play button

        StartButtonWidth = 450
        StartButtonHeight = 115

        StartButtonX = win.get_width() // 2 - StartButtonWidth // 2
        StartButtonY = 450

        playBtn = pygame.draw.rect(win, (0, 0, 0), (StartButtonX, StartButtonY, StartButtonWidth, StartButtonHeight),
                                   width=4)

        text = font.render("Play", 1, (0, 0, 0))
        win.blit(text, (width / 2 - text.get_width() / 2, 470))

        # Back btn

        backImg = pygame.image.load("images/back.png")
        backRect = backImg.get_rect()
        backRect.x, backRect.y = (0, 0)
        win.blit(backImg, backRect)


        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                mousePos = pygame.mouse.get_pos()
                AllButtonsRects = [backRect, playBtn]
                btnInfo = getClickedBtn(btns=AllButtonsRects, pos=mousePos)
                if btnInfo != None:

                    clickedBtn = btnInfo[0]
                    btnIndex = btnInfo[1]

                    if btnIndex == 0:  # if its the back btn
                        menu_screen()

                        return

                    if btnIndex == 1:
                        main(Hosting=False, comp=True)

                        return



    else:
        main(Hosting=False)



def playMenuMusic(volume=0.01, timePassed=-1):
    pygame.mixer.init()
    pygame.mixer.music.load("sounds/lobbyMusic.mp3")
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1)

    #
    # print(round(timePassed, 1))
    # pygame.mixer.init()
    # pygame.mixer.music.load("sounds/lobbyMusic.mp3")
    # pygame.mixer.music.set_volume(volume)
    #
    # pygame.mixer.music.play()
    #
    # firstTime = time.time()
    #
    # while pygame.mixer.music.get_busy():
    #
    #     None
    #
    # endTime = time.time()
    # print(round(timePassed, 1))
    #
    # if round(timePassed, 1) == -1 or round(timePassed, 1) >= 3.7:
    #     playMenuMusic(volume, timePassed=endTime- firstTime)



def menu_screen():
    pygame.font.init()

    run = True
    clock = pygame.time.Clock()

    hostGame = False
    JoinGame = False
    goToPrivateGameMenu = False
    IsMuted = False
    EverMuted = False

    sound_thread = threading.Thread(target=playMenuMusic)
    sound_thread.start()

    while run:

        if IsMuted:
            pygame.mixer.music.pause()
        else:
            if EverMuted:
                pygame.mixer.music.unpause()



        clock.tick(60)
        win.fill((160, 160, 160))
        font = pygame.font.SysFont("calibri", 80)

        # Play button

        StartButtonWidth = 450
        StartButtonHeight = 115

        StartButtonX = win.get_width() // 2 - StartButtonWidth // 2
        StartButtonY = 100

        playBtn = pygame.draw.rect(win, (0, 0, 0), (StartButtonX, StartButtonY, StartButtonWidth, StartButtonHeight),width=4)


        text = font.render("Quick Play", 1, (0, 0, 0))
        win.blit(text, (width / 2 - text.get_width() / 2, 120))

        # Comp Play button

        CompButtonWidth = 610
        CompButtonHeight = 115

        CompButtonX = win.get_width() // 2 - CompButtonWidth // 2
        CompButtonY = 300

        compBtn = pygame.draw.rect(win, (0, 0, 0), (CompButtonX, CompButtonY, CompButtonWidth, CompButtonHeight),
                                   width=4)

        text = font.render("Competitive Play", 1, (0, 0, 0))
        win.blit(text, (width / 2 - text.get_width() / 2, 320))

        # Private Game

        PrivateGameWidth = 470
        PrivateGameHeight = 115

        PrivateGameX = win.get_width() // 2 - StartButtonWidth // 2 - 15
        PrivateGameY = 500

        privateGameBtn = pygame.draw.rect(win, (0, 0, 0), (PrivateGameX, PrivateGameY, PrivateGameWidth, PrivateGameHeight),width=4)


        text = font.render("Private Game", 1, (0, 0, 0))
        win.blit(text, (width / 2 - text.get_width() / 2, 520))


        #Mute / Unmute
        muteImg = pygame.image.load("images/mute.png")
        unmuteImg = pygame.image.load("images/unmute.png")

        imageToUse = None

        if IsMuted:
            imageToUse = muteImg
        else:
            imageToUse = unmuteImg

        muteBtn = imageToUse.get_rect()
        muteBtn.x, muteBtn.y = (10, win.get_height() - 90)
        win.blit(imageToUse, muteBtn)



        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:


                mousePos = pygame.mouse.get_pos()
                AllButtonsRects = [playBtn, privateGameBtn, compBtn, muteBtn]
                btnInfo = getClickedBtn(btns=AllButtonsRects, pos=mousePos)
                if btnInfo != None:

                    clickedBtn = btnInfo[0]
                    btnIndex = btnInfo[1]

                    if btnIndex == 0: #if its the play btn
                        run = False
                        main(Hosting=False)

                        return

                    if btnIndex == 1:
                        private_game_menu()

                        return

                    if btnIndex == 2:
                        comp_menu()

                        return

                    if btnIndex == 3:
                        IsMuted = not IsMuted
                        EverMuted = True



    else:
        main(Hosting=False)





def generate_player_id():

    chars = "abcdefghijklmnopqrstuvwxyz1234567890"


    code = ""
    for i in range(20):
        code += random.choice(chars)

    playerInfo = open("playerInfo.txt", "w")
    playerInfo.write(code)

    n = Network(False, justAddId=True, code=code)

    return code

def start():
    if not os.path.isfile("playerInfo.txt"):
        generate_player_id()


    menu_screen()


if __name__ == '__main__':
    start()