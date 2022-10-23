"""
Step 1: import pygame library
"""


import sys
import pygame
import config as cfg
from paddle import Paddle
from ball import Ball
from brick import Brick
from game_menu import *
from pygame.locals import *
pygame.init()

score=cfg.SCORE
lives=cfg.LIVES
font = pygame.font.SysFont(None, 30)

# set window size
size=(cfg.WINDOW_WIDTH,cfg.WINDOW_HEIGHT)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Shooter Aircraft Breakout Game")
balls=[]

# this will be a list that will contain all the sprites we intend
all_sprites_list=pygame.sprite.Group()
all_bricks=pygame.sprite.Group()



def paddle_and_ball_initialization():
    # Create the paddle 
    paddle=Paddle(cfg.LIGHTBLUE,100,50)
    paddle.rect.x=350
    paddle.rect.y=560

    # Create the ball sprite
    
    ball=Ball(cfg.LIGHTBLUE,10,10)
    ball.rect.x=400
    ball.rect.y=560
    balls.append(ball)
    all_sprites_list.add(paddle)

    return paddle, ball



def brick_design_on_display():
        
    
    colors=[cfg.RED,cfg.ORANGE,cfg.YELLOW,cfg.GREEN]
    for i in range(7):
        for j in range(4):
            brick = Brick(colors[j],80,30)
            brick.rect.x = 60 + i* 100
            brick.rect.y = 100+j*40
            all_sprites_list.add(brick)
            all_bricks.add(brick)
    return all_bricks
   

def score_and_lives(score):
    font=pygame.font.Font(None,34)
    text=font.render("Score: "+str(score),1,cfg.WHITE)
    screen.blit(text,(20,10))
    text=font.render("Lives: "+str(lives),1,cfg.WHITE)
    screen.blit(text,(700,10))

def game_win_function():
    font=pygame.font.Font(None,74)
    text=font.render("Win, Congratulations!",1,cfg.WHITE)
    screen.blit(text,(150,300))
    pygame.display.flip()
    pygame.time.wait(3000)


def game_over_function():
    font=pygame.font.Font(None,74)
    text=font.render("Game Over",1,cfg.WHITE)
    screen.blit(text,(200,300))
    pygame.display.flip()
    pygame.time.wait(3000)

def brick_and_ball_collision_detection(ball,brick):
    ball.bounce()
    ball.kill()
    brick.kill()
    balls.remove(ball)
            
    if len(all_bricks) ==0:
        game_win_function()
        carryOn=False
        return carryOn
def ball_fire_to_bricks_from_paddle(ball,paddle):
      # ball=Ball(WHITE,10,10)
        all_sprites_list.add(ball)
        ball.rect.x=paddle.rect.x+50
        ball.rect.y=paddle.rect.y
        balls.append(ball)

        for brick in all_bricks:
            brick.rect.y += 1

        if brick.rect.y > 550:
            game_over_function()
            carryOn=False
            return carryOn

def game_end_display_function(clock,score):
    screen.fill(cfg.DARKBLUE)
    pygame.draw.line(screen,cfg.WHITE,[0,38],[800,38],2)
    all_sprites_list.draw(screen)
    score_and_lives(score)
    pygame.display.flip()
    clock.tick(100)
    

def aircraft_shooter_game_screen(carryOn,all_sprites_list,all_bricks,paddle,ball,balls,clock,score,lives):
    
    while carryOn and lives>0: 
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                carryOn=False    
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            paddle.moveRight(5)
        if keys[pygame.K_DOWN]:
            paddle.moveDown(5)
             
        if keys[pygame.K_UP]:            
            game_end=ball_fire_to_bricks_from_paddle(ball,paddle)
            if game_end == False:
                lives-=1
                carryOn=False
        
        all_sprites_list.update()
        for ball in balls:
            brick_collision_list=pygame.sprite.spritecollide(ball,all_bricks,False)     
            for brick in brick_collision_list:
                score +=1
                game_end=brick_and_ball_collision_detection(ball,brick)
                if game_end == False:
                    carryOn=False
       
        game_end_display_function(clock,score)      
    pygame.quit()
        


if __name__ == "__main__":

    # make a game start menu program
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 30)
    screen = pygame.display.set_mode((cfg.WINDOW_WIDTH, cfg.WINDOW_HEIGHT),0,32)
    click = False
    while True:
        screen.fill((0,190,255))
        draw_text('Shooter Aircraft Breakout Game', pygame.font.SysFont(None, 45), (0,0,255), screen, 200, 100)
 
        mx, my = pygame.mouse.get_pos()

        #creating buttons
        button_1 = pygame.Rect(300, 200, 200, 50)
        button_2 = pygame.Rect(300, 300, 200, 50)
        button_3 = pygame.Rect(300,400, 200, 50)
        

        #defining functions when a certain button is pressed
        if button_1.collidepoint((mx, my)):
            if click:
                carryOn=True
                # clock=pygame.time.Clock()
                all_bricks=brick_design_on_display()
                paddle,ball=paddle_and_ball_initialization()
                aircraft_shooter_game_screen(carryOn,all_sprites_list,all_bricks,paddle,ball,balls,clock,score,lives)
        
        if button_2.collidepoint((mx, my)):
            if click:
                options(screen,font,clock,click)
        
        if button_3.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)

 
        #writing text on top of button
        draw_text('PLAY', font, (255,255,255), screen, 370, 220)
        draw_text('Game Rules', font, (255,255,255), screen, 350, 315)
        draw_text('Exit', font, (255,255,255), screen, 380, 420)

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
        clock.tick(60)


    

