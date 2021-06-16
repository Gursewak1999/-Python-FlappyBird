import pygame

level = []
level1 = []
level2 = []

with open("game1.level") as l:
    for row in l:
        level1.append(list(row))
l.close()
with open("game1.level") as l:
    for row in l:
        level2.append(list(row))
l.close()

level_no = 1

level = level1
width, height = 1366, 768
cell_size = 100
fps = 120
start_x, start_y = 0, 0
y = 0

velocity = 1
isRunning = False
_frame_x, _frame_y = 0, 0
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("FLapPy BiRd")
# win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
win = pygame.display.set_mode((width, height),  pygame.FULLSCREEN)
pygame.display.init()
pygame.mixer.init()
checkPoint = pygame.mixer_music.load("src/checkPoint.wav")
die = pygame.mixer_music.load("src/die.wav")

pipe1_down = pygame.transform.scale(pygame.image.load("src/pipes/pipe1.png"), (cell_size, cell_size)).convert_alpha()
pipe2_down = pygame.transform.scale(pygame.image.load("src/pipes/pipe2.png"), (cell_size, cell_size)).convert_alpha()
pipe3_down = pygame.transform.scale(pygame.image.load("src/pipes/pipe3.png"), (cell_size, cell_size)).convert_alpha()
pipe4_down = pygame.transform.scale(pygame.image.load("src/pipes/pipe4.png"), (cell_size, cell_size)).convert_alpha()
pipe1_up = pygame.transform.flip(
    pygame.transform.scale(pygame.image.load("src/pipes/pipe1.png"), (cell_size, cell_size)), False, True).convert_alpha()
pipe2_up = pygame.transform.flip(
    pygame.transform.scale(pygame.image.load("src/pipes/pipe2.png"), (cell_size, cell_size)), False, True).convert_alpha()
pipe3_up = pygame.transform.flip(
    pygame.transform.scale(pygame.image.load("src/pipes/pipe3.png"), (cell_size, cell_size)), False, True).convert_alpha()
pipe4_up = pygame.transform.flip(
    pygame.transform.scale(pygame.image.load("src/pipes/pipe4.png"), (cell_size, cell_size)), False, True).convert_alpha()
wall_up = pygame.transform.scale(pygame.image.load("src/wall/wall_up.png"), (cell_size, cell_size)).convert_alpha()
wall_down = pygame.transform.scale(pygame.image.load("src/wall/wall_down.png"), (cell_size, cell_size)).convert_alpha()
sky = pygame.transform.scale(pygame.image.load("src/sky.png"), (cell_size, cell_size)).convert_alpha()
ptera = [
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("src/ptera/ptera_1.png"), (cell_size, cell_size)),
                          True, False, ).convert_alpha(),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("src/ptera/ptera_2.png"), (cell_size, cell_size)),
                          True, False).convert_alpha()]
flappyb = pygame.transform.scale(pygame.image.load("src/flappyBird/1_1.png"), (cell_size, cell_size)).convert_alpha()
flappyc = pygame.transform.scale(pygame.image.load("src/flappyBird/1_2.png"), (cell_size, cell_size)).convert_alpha()
flappyd = pygame.transform.scale(pygame.image.load("src/flappyBird/1_3.png"), (cell_size, cell_size)).convert_alpha()
flappye = pygame.transform.scale(pygame.image.load("src/flappyBird/1_4.png"), (cell_size, cell_size)).convert_alpha()
flappyf = pygame.transform.scale(pygame.image.load("src/flappyBird/1_5.png"), (cell_size, cell_size)).convert_alpha()
flappyg = pygame.transform.scale(pygame.image.load("src/flappyBird/1_6.png"), (cell_size, cell_size)).convert_alpha()
flappyh = pygame.transform.scale(pygame.image.load("src/flappyBird/1_7.png"), (cell_size, cell_size)).convert_alpha()
flappyi = pygame.transform.scale(pygame.image.load("src/flappyBird/1_8.png"), (cell_size, cell_size)).convert_alpha()

goj = pygame.transform.scale(pygame.image.load("src/gameOver/images_1.png"), (cell_size, cell_size)).convert_alpha()
gok = pygame.transform.scale(pygame.image.load("src/gameOver/images_2.png"), (cell_size, cell_size)).convert_alpha()
gol = pygame.transform.scale(pygame.image.load("src/gameOver/images_3.png"), (cell_size, cell_size)).convert_alpha()
gom = pygame.transform.scale(pygame.image.load("src/gameOver/images_4.png"), (cell_size, cell_size)).convert_alpha()
gon = pygame.transform.scale(pygame.image.load("src/gameOver/images_5.png"), (cell_size, cell_size)).convert_alpha()
goo = pygame.transform.scale(pygame.image.load("src/gameOver/images_6.png"), (cell_size, cell_size)).convert_alpha()
gop = pygame.transform.scale(pygame.image.load("src/gameOver/images_7.png"), (cell_size, cell_size)).convert_alpha()
goq = pygame.transform.scale(pygame.image.load("src/gameOver/images_8.png"), (cell_size, cell_size)).convert_alpha()


def loadLevel():
    global win, width, sky, cell_size, height, pipe4, pipe3, pipe2, pipe1, _frame_x, _frame_y
    if level_no == 0:
        level = level1
    elif level_no == 1:
        level = level2
    frame_x = -start_x // cell_size
    frame_y = 0
    _frame_x = frame_y
    _frame_y = frame_x

    for i in range(7):
        for j in range(15):
            _sp = sky

            if level[i + frame_y][j + frame_x] == "1":
                _sp = pipe1_down
            elif level[i + frame_y][j + frame_x] == "2":
                _sp = pipe2_down
            elif level[i + frame_y][j + frame_x] == "3":
                _sp = pipe3_down
            elif level[i + frame_y][j + frame_x] == "4":
                _sp = pipe4_down
            elif level[i + frame_y][j + frame_x] == "5":
                _sp = pipe3_up
            elif level[i + frame_y][j + frame_x] == "6":
                _sp = pipe4_up
            elif level[i + frame_y][j + frame_x] == "7":
                _sp = pipe1_up
            elif level[i + frame_y][j + frame_x] == "8":
                _sp = pipe2_up
            elif level[i + frame_y][j + frame_x] == "9":
                _sp = wall_up
            elif level[i + frame_y][j + frame_x] == "a":
                _sp = wall_down
            elif level[i + frame_y][j + frame_x] == "b":
                _sp = flappyb
            elif level[i + frame_y][j + frame_x] == "c":
                _sp = flappyc
            elif level[i + frame_y][j + frame_x] == "d":
                _sp = flappyd
            elif level[i + frame_y][j + frame_x] == "e":
                _sp = flappye
            elif level[i + frame_y][j + frame_x] == "f":
                _sp = flappyf
            elif level[i + frame_y][j + frame_x] == "g":
                _sp = flappyg
            elif level[i + frame_y][j + frame_x] == "h":
                _sp = flappyh
            elif level[i + frame_y][j + frame_x] == "i":
                _sp = flappyi
            elif level[i + frame_y][j + frame_x] == "j":
                _sp = goj
            elif level[i + frame_y][j + frame_x] == "k":
                _sp = gok
            elif level[i + frame_y][j + frame_x] == "l":
                _sp = gol
            elif level[i + frame_y][j + frame_x] == "m":
                _sp = gom
            elif level[i + frame_y][j + frame_x] == "n":
                _sp = gon
            elif level[i + frame_y][j + frame_x] == "o":
                _sp = goo
            elif level[i + frame_y][j + frame_x] == "p":
                _sp = gop
            elif level[i + frame_y][j + frame_x] == "q":
                _sp = goq


            else:
                _sp = sky
            win.blit(_sp, (j * cell_size, i * cell_size))

    return frame_x


_i = 0

gameOver = False


def loadPlayer(i, j):
    global gameOver
    global _i, cell_size, isRunning, _frame_y, _frame_x

    walls = ['1', '2', '3', '4', '5', '6', '7', '8', '9', "a"]
    print(level[3 - y + _frame_x][4 + _frame_y], walls)
    if level[3 - y + _frame_x][4 + _frame_y] in walls:
        isRunning = False
        gameOver = True
        # print(level[3 - y + _frame_x][4 + _frame_y], walls, _frame_x, _frame_y)

    if _i >= 6:
        _i = 0
    win.blit(ptera[_i // 3], (j * cell_size - 1, i * cell_size - 1))
    if isRunning and not gameOver:
        _i = _i + 1


_j = 0
_x = 0


def showGameOver():
    win.blit(goj, (5 * cell_size, 3 * cell_size))
    win.blit(gok, (6 * cell_size, 3 * cell_size))
    win.blit(gol, (7 * cell_size, 3 * cell_size))
    win.blit(gom, (8 * cell_size, 3 * cell_size))
    win.blit(gon, (5 * cell_size, 4 * cell_size))
    win.blit(goo, (6 * cell_size, 4 * cell_size))
    win.blit(gop, (7 * cell_size, 4 * cell_size))
    win.blit(goq, (8 * cell_size, 4 * cell_size))

    pygame.mixer_music.load("src/checkPoint.wav")
    pygame.mixer_music.play()

    pass


def gameLoop():
    global isRunning, start_x, start_y, _j, y, _x
    while True:

        clock.tick(fps)
        if loadLevel() >= len(level[0]) - 20:
            print("You won the match")
            if isRunning:
                isRunning = False
        else:
            if gameOver:
                break
            if isRunning:
                start_x = start_x - 1 * velocity

                if _j > 100:
                    _j = 0
                    y = y - 1
                if _x > 8:
                    _x = 0
                    pygame.mixer_music.load("src/jump.wav")
                    pygame.mixer_music.play()
                    y = y + 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            loadPlayer(3 - y, 4)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                # Fly high
                if not isRunning:
                    isRunning = True

                _x = _x + 1


            _j = _j + 1

            pygame.display.update()


gameLoop()

if gameOver:
    showGameOver()
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.display.update()
else:
    level_no = level_no + 1
    gameLoop()
