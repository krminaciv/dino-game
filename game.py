import pygame
from sys import exit
import random

pygame.init()
screen = pygame.display.set_mode((800, 500))
screen.fill('Grey')
pygame.display.set_caption('Dino Runner')
clock = pygame.time.Clock()

font = pygame.font.Font("graphic/PixelFont.ttf", 46)
score_font = pygame.font.Font("graphic/PixelFont.ttf", 25)
title_text = 'Welcome'
title_surf = font.render(title_text, True, (44,44,44))
score_text = '0'
score_surf = score_font.render(score_text, True, (44,44,44))
ground = pygame.image.load("graphic/ground.png").convert_alpha()
cactus1_surf = pygame.image.load("graphic/cactus-big.png").convert_alpha()
cactus2_surf = pygame.image.load("graphic/cactus-small.png").convert_alpha()
dino_surf = pygame.image.load("graphic/dino.png").convert_alpha()

title = title_surf.get_rect(center = (400, 150))
score = score_surf.get_rect(midright = (720, 50))
cactus1 = cactus1_surf.get_rect(bottomleft = (820, 420))
cactus2 = cactus2_surf.get_rect(bottomleft = (1100, 420))
dino = dino_surf.get_rect(bottomleft = (80, 405))

running = False
score_count = 0
frame_count = 0
dino_jump = 0

while True:

     for event in pygame.event.get():
          if event.type == pygame.QUIT: 
               pygame.quit()
               exit()
          if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE and running is False: 
                    running = True
                    title_text = ''
                    title_surf = font.render(title_text, True, (44,44,44))
                    dino.x = 80
                    cactus1.x = 820
                    cactus2.x = 1100
                    score_count = 0
               if event.key == pygame.K_SPACE and running:
                    if dino.bottom == 405:
                         dino_jump = -20

     screen.fill('Grey')
     screen.blit(title_surf, title)
     screen.blit(score_surf, score)

     for block in range(8):
          screen.blit(ground, (block*100,400))

     screen.blit(cactus1_surf, cactus1)
     screen.blit(cactus2_surf, cactus2)
     screen.blit(dino_surf, dino)

     if running:
          cactus1.x -= 5
          if cactus1.x < 0: cactus1.x = 800
          cactus2.x -= 5
          if cactus2.x < 0: cactus2.x = 1100
          if abs(cactus1.bottomleft[0] - cactus2.bottomleft[0]) < 150:
               if cactus1.x > cactus2.x : cactus1.x += 200
               if cactus2.x > cactus1.x : cactus2.x += 200

          dino_jump += 1
          dino.y += dino_jump
          if dino.bottom >= 405: dino.bottom = 405

          frame_count += 1
          if frame_count >= 5:
               score_count += 1
               frame_count = 0
          score_text = str(score_count)
          score_surf = score_font.render(score_text, True, (44,44,44))



     if dino.colliderect(cactus1) or dino.colliderect(cactus2):
          #print("game over")
          title_text = 'Game Over'
          title_surf = font.render(title_text, True, (44,44,44))
          title = title_surf.get_rect(center = (400, 100))
          running = False


     pygame.display.update()
     clock.tick(60)


