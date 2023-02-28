#the space war game created by jjjmmmsss aka james the great aka the rider aka the cruiser aka i love this one ""dab sun"" aka the sun of god aka i dont care aka i will forget you in minutes aka decision maker aka ...
import sys
import pygame
import random
from math import*
pygame.init()

screen = pygame.display.set_mode((600,700))
icon = pygame.image.load("images/space.png")
pygame.display.set_caption("space fight")
pygame.display.set_icon(icon)
background = pygame.image.load("images/background.png")


#the random position of the enemy will going to appear 
en_posX = random.randrange(100,500)
en_posY = 50
the_first_img = pygame.image.load("images/startbg.png")
#text
score = 0
text_posX = 0
text_posY = 0
text = pygame.font.Font("golden_metafor/Golden Metafor Regular.ttf",24)
def the_win_start():
    global screen,the_first_img,text
    start = True
    while start:
        
        screen.blit(the_first_img,(0,0))
        score_s = text.render("Press s to start the game press q to quit",True,(255,0,255))
        screen.blit(score_s,(20,300))
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_s:
                    main_fun()
                    start = False
                    
                if ev.key == pygame.K_q:
                    pygame.quit()
        pygame.display.flip()      
class player():
    def __init__(self):
        #player position and other settings
        self.player = pygame.image.load("images/player.png")
        self.player_posX = 250
        self.player_posY = 580
        self.playerXchange = 0
        self.playerYchange = 0
        self.player_speed = 4
#the player function where by it will be used to draw the player    
    def player_fun(self):
        screen.blit(self.player,(self.player_posX,self.player_posY))
        
class enemy():
    def __init__(self):
        #enemy position and other settings
        self.enemy_posX = 250
        self.enemy_posY = 0
        self.enemyXchange = 50
        self.enemyYchange = 15
        self.enemy_speed = 5
        self.enemy_health = 9
        self.num_of_enemy = 5
        self.red = (255,0,0)
        self.rectenemy = pygame.Rect(self.enemy_posX + 17,self.enemy_posY + 5,65,94)
        self.hitbox = (self.enemy_posX +17,self.enemy_posY + 5,65,94)
        self.enemy = pygame.image.load("./images/enemy.png")
    #the enemy function where by it will be used to draw the enemy
    def enemy_fun(self,x,y):
        screen.blit(self.enemy,(x,y))
       
    
class rocket():
    
    def __init__(self):
        #rocket of the player position, speed and other settings
        self.player_posX = 250
        self.player_posY = 580
        self.enemy_posX = 250
        self.enemy_posY = 0
        self.rocket_capacity = 1000
        self.rocket_speed = 10
        self.rocket_posY = self.player_posY
        self.rocket_posX = self.player_posX
        self.rocket_mode = "ready"
        self.red = (255,0,0)
        self.rocket_mode_enemy = "fire"
        self.rocket = pygame.image.load("images/rocket.png")

    #the rocket function to blit rocket on a screen
    def rocket_fun(self,x,y):
        screen.blit(self.rocket,(x + 5,y - 2))




#let put a function that will be used to write the scores
def score_fun(x,y,score):
    global text
    score_s = text.render("Score :"+str(score),True,(255,255,255))
    screen.blit(score_s,(x,y))

 #gameover text
def game_over_fun(x,y):
     global text,score
     high_score =score
     game_over=text.render("GAME OVER /n /n /nYour High score : "+str(high_score),True,(255,255,255))
     screen.blit(game_over,(x,y))
        
#isscollision function is used to detect the collision of between rocket and enemy also used on enemy and player collison and other collision
def iscollision(enemy_posX,rocket_posX,enemy_posY,rocket_posY):
    global score
    collision=sqrt(pow((enemy_posX - rocket_posX),2) + pow((enemy_posY - rocket_posY),2))
    if collision <= 50:
        enemy.enemy_health -= 1
        score += 1
        
        return True
    else:
        return False



def callfunction():
    #function calls in while loop
    score_fun(text_posX,text_posY,score)
    player.player_fun()
    enemy.enemy_fun(enemy.enemy_posX,enemy.enemy_posY)
    score_fun(text_posX,text_posY,score)    
##we make the classes to a variable so that we can be able to use it as we define in the class method
rocket = rocket()       
player = player()
enemy = enemy()



#the main game function

def main_fun():
    global score
    run=True

    while run:
        screen.blit(background,(0,0))
        
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               quit()
               sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                   player.playerXchange = -player.player_speed
                    
                    
                if event.key == pygame.K_RIGHT:
                    player.playerXchange = player.player_speed
                    
                    
                if event.key == pygame.K_DOWN:
                    player.playerYchange = player.player_speed
                    
    
                      
                if event.key == pygame.K_UP:
                    player.playerYchange = -player.player_speed
                if event.key == pygame.K_SPACE:
                    if rocket.rocket_mode == "ready":
                        rocket.rocket_posY = player.player_posY
                        rocket.rocket_posX = player.player_posX
                        rocket.rocket_mode = "fire"
                        rocket.rocket_fun(rocket.rocket_posX,rocket.rocket_posY)
                        rocket.rocket_capacity -= 1
                        
                            
                                
            if event.type == pygame.KEYUP:
                if event.type == pygame.K_LEFT or pygame.K_RIGHT or pygame.K_UP or pygame.K_DOWN:
                    player.playerXchange = 0
                    player.playerYchange = 0
            
                if event.type == pygame.K_SPACE:
                    rocket.rocket_mode = "ready"
                    
        
           
        
        player.player_posX += player.playerXchange
        player.player_posY += player.playerYchange
    
                
        enemy.enemy_posX += enemy.enemy_speed

         #rocket reset        
        if rocket.rocket_mode == "fire":
            rocket.rocket_posY -= rocket.rocket_speed
            rocket.rocket_fun(rocket.rocket_posX,rocket.rocket_posY)
        if rocket.rocket_posY <= -58:
            rocket.rocket_mode = "ready"
                            
                   
        callfunction()
    

        #boundary of the enemy    
        if enemy.enemy_posX >= 500:
            enemy.enemy_speed = -1
            enemy.enemy_posY += 15
        if enemy.enemy_posX <= -15:
            enemy.enemy_speed = 1
            enemy.enemy_posY += 15

     
       
    
        
        

        #playerboundery
        if player.player_posX <= 0:
            player.player_posX = -1
    
        if player.player_posX >= 495:
            player.player_posX = 495
        if player.player_posY <= 0:
            player.player_posY = 0
    
        if player.player_posY >= 600:
            player.player_posY = 600
    
    
        
        #collission detection
        collision_rocket_enemy = iscollision(enemy.enemy_posX,rocket.rocket_posY,enemy.enemy_posY,rocket.rocket_posY)
        
        if collision_rocket_enemy:
            rocket.rocket_mode = "ready"
            rocket.rocket_posY = player.player_posY
            if enemy.enemy_health < 1:
                enemy.enemy_posX = 250
                enemy.enemy_posY = 0
                enemy.enemy_health = 9
       
       

        if enemy.enemy_health < 1:
                enemy.enemy_posX = 250
                enemy.enemy_posY = 0
                enemy.enemy_health = 9
      
                
        #the function to detect if enemy has collide with the player   
        collision_player_enemy = iscollision(enemy.enemy_posX,player.player_posX,enemy.enemy_posY,player.player_posY)
        if collision_player_enemy:
          pygame.quit()
          quit()
          sys.exit()
        pygame.display.flip()
the_win_start()
main_fun()
























