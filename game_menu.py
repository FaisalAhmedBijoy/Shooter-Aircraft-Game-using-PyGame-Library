"""
Importing important libraries
"""
import pygame, sys

"""
Setting up an environment to initialize pygame
"""
from pygame.locals import *

 
"""
A function that can be used to write text on our screen and buttons
"""
def draw_text(text, font, color, surface, x, y):
    
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 

 
# Main container function that holds the buttons and game functions
def start_options_menu(screen,font,mainClock,click):
    while True:
 
        screen.fill((0,190,255))
        draw_text('Main Menu', font, (0,0,0), screen, 250, 40)
 
        mx, my = pygame.mouse.get_pos()

        #creating buttons
        button_1 = pygame.Rect(200, 100, 200, 50)
        button_2 = pygame.Rect(200, 180, 200, 50)

        #defining functions when a certain button is pressed
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
 
        #writing text on top of button
        draw_text('PLAY', font, (255,255,255), screen, 270, 115)
        draw_text('OPTIONS', font, (255,255,255), screen, 250, 195)


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
"""
This function is called when the "PLAY" button is clicked.
"""
def game():
    running = True
    while running:
        screen.fill((0,0,0))
       
        draw_text('GAME SCREEN', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
       
        pygame.display.update()
        mainClock.tick(60)

"""
This function is called when the "OPTIONS" button is clicked.
"""
def options(screen,font,mainClock,click=False):
    running = True
    game_rules=['- Keyboard button: space -> Shooting',
                '- Keyboard button: arrow up -> Paddle movement up',
                '- Keyboard button: arrow left -> Paddle move left',
                '- Keyboard button: arrow right -> Paddle move right',
                '- Keyboard button: arrow down -> Paddle move down',
                '- Keyboard button: ESC -> Game exit / back']
    while running:
        screen.fill((0,190,255))
 
        draw_text('Game Rules', pygame.font.SysFont(None, 45), (0, 0, 255), screen, 240, 100)
        # draw_text(game_rules[0], font, (255, 255, 255), screen, 20, 20)
        for index,rules in enumerate(game_rules):
            # print(index,rules)
            draw_text(rules, font, (100, 0, 0), screen, 100, index*30+200)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
       
        pygame.display.update()
        mainClock.tick(60)
 
if __name__ == '__main__':
    mainClock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption('game base')
    screen = pygame.display.set_mode((600, 300),0,32)
    # A variable to check for the status later
    click = False
    font = pygame.font.SysFont(None, 30)
    
    #setting font settings
    font = pygame.font.SysFont(None, 30)
    options(screen,font,mainClock,click)
    # start_options_menu(screen,font,mainClock,click)
    
