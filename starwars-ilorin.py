import pygame
import time
import random

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Star War Ipata")

BG = pygame.transform.scale(pygame.image.load("stage.jpg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 60
PLAYER_HEIGHT = 80

PLAYER_VEL = 1

def draw(player):
    WIN.blit(BG, (0, 0))

    pygame.draw.rect(WIN, "orange", player)
    pygame.display.update()

def main():
    run = True

    player =  pygame.Rect(200,  HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >=0:
            player.x -= PLAYER_VEL 
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        if keys[pygame.K_UP] and player.y - PLAYER_VEL - player.height <= HEIGHT: #needs fixing 
            player.y -= PLAYER_VEL                                                
        if keys[pygame.K_DOWN] and player.y + PLAYER_VEL + player.height >= 0:    #needs fixing
            player.y += PLAYER_VEL
            
        
        draw(player)

    pygame.quit()

if __name__ == "__main__":
    main()         
