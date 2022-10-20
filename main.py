"""
Step 1: import pygame library
"""
import pygame
# import paddle class
from paddle import Paddle
from ball import Ball
from brick import Brick
pygame.init()

'''
Step 2: Define colours in the game
'''
#Define some colors in RGB format
WHITE=(255,255,255)
DARKBLUE=(36,90,190)
LIGHTBLUE=(0,176,240)
RED=(255,0,0)
ORANGE=(255,100,0)
YELLOW=(255,255,0)
GREEN=(0,255,0)

score=100
lives=10


'''
Step 3: open a new window
'''
# set window size
size=(800,600)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Shooter Aircraft Breakout Game")


# this will be a list that will contain all the sprites we intend
all_sprites_list=pygame.sprite.Group()


# Create the paddle 
paddle=Paddle(LIGHTBLUE,100,50)
paddle.rect.x=350
paddle.rect.y=560

# Create the ball sprite
balls=[]
ball=Ball(LIGHTBLUE,10,10)
ball.rect.x=400
ball.rect.y=560
# all_sprites_list.add(ball)
balls.append(ball)


all_bricks=pygame.sprite.Group()
for i in range(7):
    brick=Brick(RED,80,30)
    brick.rect.x=60+i*100
    brick.rect.y=100
    all_sprites_list.add(brick)
    all_bricks.add(brick)

for i in range(7):
    brick = Brick(ORANGE,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(YELLOW,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 180
    all_sprites_list.add(brick)
    all_bricks.add(brick)
    
for i in range(7):
    brick = Brick(GREEN,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 220
    all_sprites_list.add(brick)
    all_bricks.add(brick)

# add the paddle to the list of sprites
all_sprites_list.add(paddle)



# the lopp will carry on until exit the game
carryOn=True

#the clock will be used to control how fast screen upload updates
clock=pygame.time.Clock()

#------------ Main program loop
while carryOn:
    # main event loop
    for event in pygame.event.get(): #user did something
        if event.type ==pygame.QUIT: # if user click close
            carryOn=False # Flag that we are done to exit
        
    
    # Moving the paddle when the use uses the arrow key
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5)

    if keys[pygame.K_DOWN]:
        paddle.moveDown(5)
        
    
    #-------- Game logic should go there
    all_sprites_list.update()

    # Check if there is a car collision
    brick_collision_list=pygame.sprite.spritecollide(ball,all_bricks,False)
   

        
    for brick in brick_collision_list:
        # ball.bounce()
        score +=1
        ball.kill()
        # brick.kill()
       
      
        if len(all_bricks) ==0:
            # Display level complete 3 seconds
            font=pygame.font.Font(None,74)
            text=font.render("LEVEL WIN",1,WHITE)
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
                text=font.render("LEVEL WIN",1,WHITE)
                screen.blit(text,(200,300))
                pygame.display.flip()
                pygame.time.wait(3000)
                
                # stop the Game
                carryOn=False
    if keys[pygame.K_UP]:
        
        # ball=Ball(WHITE,10,10)
        all_sprites_list.add(ball)
        ball.rect.x=paddle.rect.x+50
        ball.rect.y=paddle.rect.y
        balls.append(ball)

        for brick in all_bricks:
            brick.rect.y += 1

        if brick.rect.y > 550:
                font=pygame.font.Font(None,74)
                text=font.render("GAME OVER",1,WHITE)
                screen.blit(text,(200,300))
                pygame.display.flip()
                pygame.time.wait(3000)
                    
                # stop the Game
                carryOn=False
    
   
    # for ball in balls:
    #     ball.rect.y-=1

    #--- Drawing code should go here
    # First clear the screen to dark blue
    screen.fill(DARKBLUE)
    pygame.draw.line(screen,WHITE,[0,38],[800,38],2)
    
    # now lets draw all the sprites in one go
    all_sprites_list.draw(screen)
    
    # Display the score and the number of lives at the top of the window
    font=pygame.font.Font(None,34)
    text=font.render("Score: "+str(score),1,WHITE)
    screen.blit(text,(20,10))
    
    text=font.render("Lives: "+str(lives),1,WHITE)
    screen.blit(text,(650,10))
    
    # Go ahead and update the screen with we've drawn
    pygame.display.flip()
    # Limit to 60 frame per second
    clock.tick(60)
# Once we have exited the main program loop we can stop the game
pygame.quit()
