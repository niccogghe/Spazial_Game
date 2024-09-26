import pygame
import sys
import random


# Inizzializzo pygame
pygame.init()

# Definisco le dimensioni dello schermo
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# Definisco i colori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED =  (255, 0, 0)
BLUE = (0, 0, 255)

obstacle_x = 400
obstacle_y = 400
obstacle_width = 40
obstacle_height = 40
player_x = 200
player_y = 400

#Dichiarazione musica
pygame.mixer.music.load("Nokia Polyphonic tone.mp3")
pygame.mixer.music.play(-1)


# dichiarazione immagini
immagine = pygame.image.load("assets/Up.png")
immagine = pygame.transform.scale(immagine, (30, 27))

naveup = pygame.image.load("assets/navespaziale_up.jpeg")
naveup = pygame.transform.scale(naveup, (20, 20))

navedown = pygame.image.load("assets/navespaziale_down.jpeg")
navedown = pygame.transform.scale(navedown, (20, 20))

naveleft = pygame.image.load("assets/navespaziale_left.jpeg")
naveleft = pygame.transform.scale(naveleft, (20, 20))

naveright = pygame.image.load("assets/navespaziale_right.jpeg")
naveright = pygame.transform.scale(naveright, (20, 20))

immagine_down = pygame.image.load("assets/Down.png")
immagine_down = pygame.transform.scale(immagine_down, (30, 27))

immagine_left = pygame.image.load("assets/Left.png")
immagine_left = pygame.transform.scale(immagine_left, (30, 27))

immagine_right = pygame.image.load("assets/Right.png")
immagine_right = pygame.transform.scale(immagine_right, (30, 27))

morte = pygame.image.load("assets/gam_over.png")
morte = pygame.transform.scale(morte, (250, 130))

ufo = pygame.image.load("assets/ufo.png")
ufo = pygame.transform.scale(ufo, (20, 20))

wall = pygame.image.load("assets/asteroide.jpeg")
wall = pygame.transform.scale(wall, (20, 20))

# Creo lo schermo su cui giocare
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spazial-Game')

# Velocita NAVE
clock = pygame.time.Clock()
NAVE_SPEED = 10


nave_x = SCREEN_WIDTH // 2
nave_y = SCREEN_HEIGHT // 2

ufo_x = SCREEN_WIDTH // 2
ufo_y = SCREEN_HEIGHT // 2



# Quanto è grande NAVE
NAVE_BLOCK = 20
wall_size = 20


def update_score(score):
    font = pygame.font.SysFont('impact', 25)
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, (SCREEN_WIDTH - 120, 10))

def help():

    game_over = False

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # Tasto Q

                    # Tasto C
                if event.key == pygame.K_m:
                    main_menu()  # Recursive call to start a new game


        screen.fill(WHITE)

        #Helper comands

        message("[GAME-CONTROLS]", BLUE, SCREEN_WIDTH / 6, SCREEN_HEIGHT / 4)
        message("[UP]", BLACK, SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3.2)
        message("[DOWN]", BLACK, SCREEN_WIDTH / 6, SCREEN_HEIGHT / 2.7)
        message("[LEFT]", BLACK, SCREEN_WIDTH / 6, SCREEN_HEIGHT / 2.3)
        message("[RIGHT]", BLACK, SCREEN_WIDTH / 6, SCREEN_HEIGHT / 2)
        message("FOR RETURN TO MENU DIGIT [M]", BLUE, SCREEN_WIDTH / 6, SCREEN_HEIGHT/ 1.6)

        screen.blit(immagine, (SCREEN_WIDTH // 4.5, SCREEN_HEIGHT // 3.2) )
        screen.blit(immagine_down, (SCREEN_WIDTH // 3.8, SCREEN_HEIGHT // 2.7) )
        screen.blit(immagine_left, (SCREEN_WIDTH // 4.2, SCREEN_HEIGHT // 2.3) )
        screen.blit(immagine_right, (SCREEN_WIDTH // 3.8, SCREEN_HEIGHT // 2.0) )

        pygame.display.update()

# Font
font_style = pygame.font.SysFont("impact", 25)
score_font = pygame.font.SysFont("impact", 35)


def our_NAVE(x1 ,y1, x_change, y_change, NAVE_BLOCK):
    if x_change == 0 and y_change == -NAVE_BLOCK:
        screen.blit(naveup, (x1, y1))
    elif x_change == 0 and y_change == NAVE_BLOCK:
        screen.blit(navedown, (x1, y1))
    elif x_change == -NAVE_BLOCK and y_change == 0:
        screen.blit(naveleft, (x1, y1))
    elif x_change == NAVE_BLOCK and y_change == 0:
        screen.blit(naveright, (x1, y1))
    else:
        screen.blit(naveright, (x1, y1))

def message(msg, color, x, y):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [x, y])

def gameLoop(score):
    game_over = False
    game_close = False

    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2

    x1_change = 0
    y1_change = 0


    foodx = round(random.randrange(0, SCREEN_WIDTH - NAVE_BLOCK) / 20.0) * 20.0
    foody = round(random.randrange(0, SCREEN_HEIGHT - NAVE_BLOCK) / 20.0) * 20.0
    wall_x = random.randrange(wall_size, SCREEN_WIDTH - wall_size, wall_size)
    wall_y = random.randrange(wall_size, SCREEN_HEIGHT - wall_size, wall_size)

    walls = [(wall_x, wall_y)]


    while not game_over:

        while game_close == True:

            #In game-over manda un messaggio di restart oppure di quit
            screen.fill(WHITE)

            #immagine Game Over
            screen.blit(morte,(SCREEN_WIDTH / 2.9, SCREEN_HEIGHT / 6.4))

            message("Quit[Q]", BLACK, SCREEN_WIDTH / 2.2, SCREEN_HEIGHT / 2.4)
            message("Play[C]", BLACK, SCREEN_WIDTH / 2.2, SCREEN_HEIGHT / 2.0)
            message("Score: " + str(score), BLACK, SCREEN_WIDTH / 2.2, SCREEN_HEIGHT / 1.7)

            pygame.display.update()

            #Abilita il tasto Q-->Quit & C-->Play-again
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    #Tasto Q
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                        #Tasto C
                    if event.key == pygame.K_c:
                        score = 0
                        gameLoop(score)  # Recursive call to start a new game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

                #Abilito i vari tasti ovvero le freccette per muovermi con lo NAVE
            if event.type == pygame.KEYDOWN:
                #Abilito Left
                if event.key == pygame.K_LEFT:
                    x1_change = -NAVE_BLOCK
                    y1_change = 0
                    # Abilito Right
                elif event.key == pygame.K_RIGHT:
                    x1_change = NAVE_BLOCK
                    y1_change = 0
                    # Abilito Up
                elif event.key == pygame.K_UP:
                    y1_change = -NAVE_BLOCK
                    x1_change = 0
                    # Abilito Down
                elif event.key == pygame.K_DOWN:
                    y1_change = NAVE_BLOCK
                    x1_change = 0



        if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(WHITE)
        update_score(score)
        screen.blit(ufo, (foodx, foody))
        for wall_x, wall_y in walls:
            screen.blit(wall, (wall_x, wall_y))
        update_score(score)


        our_NAVE(x1 , y1, x1_change , y1_change, NAVE_BLOCK)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, SCREEN_WIDTH - NAVE_BLOCK) / 20.0) * 20.0
            foody = round(random.randrange(0, SCREEN_HEIGHT - NAVE_BLOCK) / 20.0) * 20.0
            wall_x = random.randrange(wall_size, SCREEN_WIDTH - wall_size, wall_size)
            wall_y = random.randrange(wall_size, SCREEN_HEIGHT - wall_size, wall_size)
            while wall_x == x1 and wall_x == y1:
                wall_x = random.randrange(wall_size, SCREEN_WIDTH - wall_size, wall_size)
                wall_y = random.randrange(wall_size, SCREEN_HEIGHT - wall_size, wall_size)

            walls.append([wall_x, wall_y])

            score += 10


        for wall_x, wall_y in walls:
            if wall_x == x1 and wall_y == y1:
                game_close = True
        
        clock.tick(NAVE_SPEED)

    pygame.quit()
    quit()

def main_menu():

    while True:
        screen.fill(WHITE)

        message("WELCOME TO SPAZIAL-GAME", BLUE, SCREEN_WIDTH / 6, SCREEN_HEIGHT / 4)
        message("PLAY[P]", BLACK, SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3.2)
        message("HELP[H]", BLACK, SCREEN_WIDTH / 6, SCREEN_HEIGHT / 2.7)
        message("QUIT[Q]", BLACK, SCREEN_WIDTH / 6, SCREEN_HEIGHT / 2.3)

        pygame.display.update()

        #Premi P-->Play
        #Premi Q-->Quit
        #Premi H-->Help
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    score = 0
                    gameLoop(score)

pygame.display.update()


if __name__ == "__main__":
    main_menu()


