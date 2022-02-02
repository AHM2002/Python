import pygame
import random
import os


pygame.init()

#creating Windows
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width,screen_height))

#colors
white = (255,255,255) 
red = (255,0,0)
black = (0,0,0) 
snakegreen = (35, 45, 40)


#Background image
#bgimg = pygame.image.load("E:\Intro1.png")
outro = pygame.image.load("E:\outro.png")
#Game title
pygame.display.set_caption("Snakes with Milon")
pygame.display.update()
font = pygame.font.SysFont(None,55)
clock = pygame.time.Clock()

def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])
    
def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,color,[x, y, snake_size, snake_size])
'''def bug():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT == pygame.K_RIGHT or event.key == pygame.K_UP == pygame.K_DOWN:'''
                
                 
def Welcome():
    exit_game =False
    while not exit_game:
        gameWindow.fill(black)
        text_screen("Welcome to Snake With Milon",red,200,250)
        text_screen("Press Space Bar to play",red,232,290)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("E:\Music_bgm.mp3")
                    pygame.mixer.music.play()
                    gameLoop()


        pygame.display.update()
        clock.tick(60)

if (not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")

#Game specific variables
def gameLoop():
    exit_game = False
    game_over = False
    snake_x = 50
    snake_y = 50
    snake_size = 10
    food_size = 5
    velocity_x = 0
    velocity_y = 0
    initVelocity = 5 
    fps = 30
    score = 0
    snk_list =[]
    snk_length = 1 

    food_x = random.randint(0, screen_width)
    food_y = random.randint(0, screen_height)
    # Highscore Build
    '''if (not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")'''
    with open("highscore.txt") as f:
        highscore = f.read()

    #Game loop
    while not exit_game:
        if game_over:
            with open("highscore.txt","w") as f:
                f.write(str(highscore))
            gameWindow.blit(outro,(0,0))
            

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        Welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True        
            
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:
                        velocity_x = initVelocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -initVelocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -initVelocity #----> why minus?
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = initVelocity
                        velocity_x = 0
                    if event.key ==pygame.K_1:
                        score += 10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y 

            if abs(snake_x - food_x) < 8 and abs(snake_y - food_y) < 8:
                score += 10
                food_x = random.randint(25, screen_width/2)
                food_y = random.randint(25, screen_height/2)
                snk_length += 5
                if score>int(highscore):
                    highscore = score
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]
                

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load("E:\Music_bgm.mp3")
                pygame.mixer.music.play()

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True 
                pygame.mixer.music.load("E:\Music_bgm.mp3")
                pygame.mixer.music.play()


            gameWindow.fill(snakegreen)
            #gameWindow.blit(bgimg,(screen_height,screen_width))

            text_screen ("Score: "+ str(score)+ "Highsore: "+str(highscore),red,5,5)

            pygame.draw.rect(gameWindow,red,[snake_x,snake_y,snake_size,snake_size])

            pygame.draw.circle(gameWindow,black,(food_x,food_y),food_size)

            plot_snake(gameWindow,red,snk_list,snake_size)
            

        #clock.tick(fps) #--->why not there?
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()

Welcome()
#gameLoop()







