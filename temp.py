
import pygame
from paddle import Paddle
from ball import Ball
from brick import Brick

pygame.init()

print("initialized")

WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
 
score = 0
lives = 1

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Shooting Game")

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
 
#Create the Paddle
paddle = Paddle(LIGHTBLUE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560
 

balls = []
ball = Ball(WHITE,10,10)
ball.rect.x = 400
ball.rect.y = 550
all_sprites_list.add(ball)
balls.append(ball)

all_bricks = pygame.sprite.Group()
for i in range(8):
    brick = Brick(RED,70,30)
    brick.rect.x = 15 + i* 100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(8):
    brick = Brick(ORANGE,70,30)
    brick.rect.x = 15 + i* 100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(8):
    brick = Brick(YELLOW,70,30)
    brick.rect.x = 15 + i* 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(8):
    brick = Brick(WHITE,70,30)
    brick.rect.x = 15 + i* 100
    brick.rect.y = 180
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(8):
    brick = Brick(LIGHTBLUE,70,30)
    brick.rect.x = 15 + i* 100
    brick.rect.y = 220
    all_sprites_list.add(brick)
    all_bricks.add(brick)

# Add the paddle to the list of sprites
all_sprites_list.add(paddle)



class Unit():
    def __init__(self):
        self.last = pygame.time.get_ticks()
        self.cooldown = 300    

    def fire(self):
        # fire gun, only if cooldown has been 0.3 seconds since last
        now = pygame.time.get_ticks()
        if now - self.last >= self.cooldown:
            self.last = now


carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()


# Time counter for brick falling
time_counter = 0

brick_fall = pygame.USEREVENT + 1
set_timer = pygame.USEREVENT + 2
pygame.time.set_timer(brick_fall, 1000)
pygame.time.set_timer(set_timer, 1000)

start_ticks=pygame.time.get_ticks() #starter tick

    

# -------- Main Program Loop -----------
while carryOn:
    seconds=(pygame.time.get_ticks()-start_ticks)/1000 
    if seconds>30: 
        font = pygame.font.Font(None, 74)
        text = font.render("GAME OVER", 1, WHITE)
        screen.blit(text, (200,300))
        pygame.display.flip()
        pygame.time.wait(3000)
 
        #Stop the Game
        carryOn=False
        
        print (seconds) #print how many seconds
    time_counter = clock.get_time()
    #print("t", time_counter)
    if time_counter % 3000 == 0:
        print(time_counter)
        for brick in all_bricks:
            brick.rect.y += 10
        time_counter = 0
    #for brick in all_bricks:
        #brick.rect.y += 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop
            
        if event.type == pygame.MOUSEBUTTONUP:
            last = pygame.time.get_ticks()
            now = pygame.time.get_ticks()
            last = now
            ball = Ball(WHITE, 10, 10)
            all_sprites_list.add(ball)
            ball.rect.x = paddle.rect.x + 50
            ball.rect.y = paddle.rect.y
            balls.append(ball)
        if event.type == brick_fall:
            for brick in all_bricks:
                brick.rect.y += 10
        
      
    #Check if there is the ball collides with any of bricks
    brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
    for brick in brick_collision_list:
      ball.bounce()
      score += 1
      brick.kill()
      if len(all_bricks)==0:
           #Display Level Complete Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, WHITE)
            screen.blit(text, (200,300))
            pygame.display.flip()
            pygame.time.wait(3000)
 
            #Stop the Game
            carryOn=False
    
    #Moving the paddle when the use uses the arrow keys 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5) 
        
    all_sprites_list.update()




    #Check if there is the ball collides with any of bullets
    for ball in balls:
        brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
        #print("bullets",brick_collision_list)
        for brick in brick_collision_list:
          #ball.bounce()
          score += 1
          brick.kill()
          ball.kill()
          balls.remove(ball)
          if len(all_bricks) == 0:
              #Display Level Complete Message for 3 seconds
              font = pygame.font.Font(None, 74)
              text = font.render("LEVEL COMPLETE", 1, WHITE)
              screen.blit(text, (200, 300))
              pygame.display.flip()
              pygame.time.wait(3000)

              #Stop the Game
              carryOn = False
    #------Brick falling down ---------

    for ball in balls:
        ball.rect.y -= 1
 
    # --- Drawing code should go here
    # First, clear the screen to dark blue. 
    screen.fill(DARKBLUE)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)
 
    #Display the score and the number of lives at the top of the screen
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650,10))
    
    #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    all_sprites_list.draw(screen)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
    # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()