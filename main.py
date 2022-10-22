"""
Step 1: import pygame library
"""
from cmath import rect
import random
import pygame
import config as cfg
from paddle import Paddle
from ball import Ball
from brick import Brick
pygame.init()

score=cfg.SCORE
lives=cfg.LIVES

# set window size
size=(cfg.WINDOW_HEIGHT,cfg.WINDOW_WIDTH)
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
   

def score_and_lives():
    font=pygame.font.Font(None,34)
    text=font.render("Score: "+str(score),1,cfg.WHITE)
    screen.blit(text,(20,10))
    text=font.render("Lives: "+str(lives),1,cfg.WHITE)
    screen.blit(text,(700,10))

def game_win_function():
    font=pygame.font.Font(None,74)
    text=font.render("Win, Congratulations!",1,cfg.WHITE)
    screen.blit(text,(200,300))
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

def game_end_display_function(clock):
    screen.fill(cfg.DARKBLUE)
    pygame.draw.line(screen,cfg.WHITE,[0,38],[800,38],2)
    all_sprites_list.draw(screen)
    score_and_lives()
    pygame.display.flip()
    clock.tick(100)
    

if __name__ == "__main__":
 
    carryOn=True
    clock=pygame.time.Clock()

    all_bricks=brick_design_on_display()
    paddle,ball=paddle_and_ball_initialization()

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
       
        game_end_display_function(clock)      
    pygame.quit()
        