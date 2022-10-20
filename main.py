"""
Step 1: import pygame library
"""
import pygame
# import paddle class
import config as cfg
from paddle import Paddle
from ball import Ball
from brick import Brick
pygame.init()


# set window size
size=(cfg.WINDOW_HEIGHT,cfg.WINDOW_WIDTH)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Shooter Aircraft Breakout Game")


# this will be a list that will contain all the sprites we intend
all_sprites_list=pygame.sprite.Group()
balls=[]

# Create the paddle 
def brick_design():
    all_bricks=pygame.sprite.Group()
    for i in range(7):
        brick=Brick(cfg.RED,80,30)
        brick.rect.x=60+i*100
        brick.rect.y=100
        all_sprites_list.add(brick)
        all_bricks.add(brick)

    for i in range(7):
        brick = Brick(cfg.ORANGE,80,30)
        brick.rect.x = 60 + i* 100
        brick.rect.y = 140
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    for i in range(7):
        brick = Brick(cfg.YELLOW,80,30)
        brick.rect.x = 60 + i* 100
        brick.rect.y = 180
        all_sprites_list.add(brick)
        all_bricks.add(brick)
        
    for i in range(7):
        brick = Brick(cfg.GREEN,80,30)
        brick.rect.x = 60 + i* 100
        brick.rect.y = 220
        all_sprites_list.add(brick)
        all_bricks.add(brick)
def paddle_on_game_board():
    paddle=Paddle(cfg.LIGHTBLUE,100,50)
    paddle.rect.x=350
    paddle.rect.y=560
    all_sprites_list.add(paddle)
    return paddle

def initialize_ball_position():
    # Create the ball sprite

    ball=Ball(cfg.LIGHTBLUE,10,10)
    ball.rect.x=400
    ball.rect.y=560
    balls.append(ball)

def game_over_function():
    font=pygame.font.Font(None,74)
    text=font.render("GAME OVER",1,cfg.WHITE)
    screen.blit(text,(200,300))
    pygame.display.flip()
    pygame.time.wait(3000)
                    
    # stop the Game
    carryOn=False

def keyboard_functionalities(paddle,ball,all_bricks):
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5)
    if keys[pygame.K_DOWN]:
        paddle.moveDown(5)
    if keys[pygame.K_UP]:
        
        # ball=Ball(WHITE,10,10)
        all_sprites_list.add(ball)
        ball.rect.x=paddle.rect.x+50
        ball.rect.y=paddle.rect.y
        balls.append(ball)

        for brick in all_bricks:
            brick.rect.y += 1

        if brick.rect.y > 550:
            game_over_function()
              

def brick_and_ball_collision(ball,all_bricks):
    brick_collision_list=pygame.sprite.spritecollide(ball,all_bricks,False)
           
    for brick in brick_collision_list:
        # ball.bounce()
        score +=1
        ball.kill()
        # brick.kill()
       
      
        if len(all_bricks) ==0:
            # Display level complete 3 seconds
            font=pygame.font.Font(None,74)
            text=font.render("LEVEL WIN",1,cfg.WHITE)
            screen.blit(text,(200,300))
            pygame.display.flip()
            pygame.time.wait(3000)
            
            # stop the Game
            carryOn=False
    
    for ball in balls:
        brick_collision_list=pygame.sprite.spritecollide(ball,all_bricks,False)
    
        
        for brick in brick_collision_list:
            # ball.bounce()
            score +=1
            ball.kill()
            brick.kill()
            balls.remove(ball)
          
            if len(all_bricks) ==0:
                # Display level complete 3 seconds
                font=pygame.font.Font(None,74)
                text=font.render("LEVEL WIN",1,cfg.WHITE)
                screen.blit(text,(200,300))
                pygame.display.flip()
                pygame.time.wait(3000)
                
                # stop the Game
                carryOn=False


carryOn=True
clock=pygame.time.Clock()
while carryOn:
   
    for event in pygame.event.get(): 
        if event.type ==pygame.QUIT: 
            carryOn=False 
    all_sprites_list.update()

    screen.fill(cfg.DARKBLUE)
    pygame.draw.line(screen,cfg.WHITE,[0,38],[800,38],2)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()



def score_and_live_calculation():
    font=pygame.font.Font(None,34)
    text=font.render("Score: "+str(cfg.SCORE),1,cfg.WHITE)
    screen.blit(text,(20,10))
    
    text=font.render("Lives: "+str(cfg.LIVES),1,cfg.WHITE)
    screen.blit(text,(650,10))


if __name__ == '__main__':
    brick_design()
    padddle=paddle_on_game_board()
    initialize_ball_position()
    keyboard_functionalities()
    brick_and_ball_collision()
    score_and_live_calculation()


    
