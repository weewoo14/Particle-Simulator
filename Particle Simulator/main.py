# Setup Python ----------------------------------------------- #
import pygame, sys, random
from buttons import *
from text import *
from buttoncheck import *

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Particle Simulator')
screen = pygame.display.set_mode((1000, 600),0,32)
# Particle Intialization
particles = []
defaultcolor = ['white']

# Music
pygame.mixer.init()
pygame.mixer.music.load("musicloop.mp3")
pygame.mixer.music.play(-1,0.0)

# Running
running = False
# Loop ------------------------------------------------------- #
while True:
    # Background --------------------------------------------- #
    screen.fill((0,0,0))
    # Buttons ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        # Checking the colored buttons
        if event.type == pygame.MOUSEBUTTONDOWN:
           for i in range(len(colors)):
              if Rect(button_array[i][0]).collidepoint(event.pos):
                 if colors[i] in defaultcolor and len(defaultcolor) >= 2:
                    defaultcolor.remove(colors[i])
                    button_array[i][1] = False
                 elif colors[i] in defaultcolor and len(defaultcolor) == 1:
                    defaultcolor.remove(colors[i])
                    defaultcolor.append('black')
                    button_array[i][1] = False
                 else:
                    defaultcolor.append(colors[i])
                    button_array[i][1] = True
        # Checking the functionality buttons
        if event.type == pygame.MOUSEBUTTONDOWN:
            if fmouse.collidepoint(event.pos):
                button_array[7][1] = True
                button_array[8][1] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if sflake.collidepoint(event.pos):
                button_array[7][1] = False
                button_array[8][1] = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if reversegravity.collidepoint(event.pos):
                if button_array[-1][1]:
                    button_array[-1][1] = False
                else:
                    button_array[-1][1] = True
        if event.type == pygame.MOUSEBUTTONDOWN:
          if startrect.collidepoint(event.pos):
            running = True
        if event.type == pygame.MOUSEBUTTONDOWN:
          if exitrect.collidepoint(event.pos):
            running = False
            particles = []
            defaultcolor = ['white']
    px,py = pygame.mouse.get_pos()
    if running:
      if len(defaultcolor) == 2 and 'black' in defaultcolor:
        defaultcolor.remove('black')

      for rect,on,color1,color2 in button_array:
          pygame.draw.rect(screen,check(color1,color2,rect,px,py,on),Rect(rect))

      # Check Exit Button
      if 900 <= px <= 1000 and 0 <= py <= 101:
        pygame.draw.rect(screen,(255,0,0),exitrect)
      else:
        pygame.draw.rect(screen,(139,0,0),exitrect)
      if button_array[7][1]:
          particles.append([[random.randint(px-20,px+20),random.randint(py-10,py+10)],[(random.randint(60,80)/10)-1],random.randint(1,5),(random.randint(10,30)/100),random.choice(defaultcolor)])
          particles.append([[random.randint(px-20,px+20),random.randint(py-10,py+10)],[(random.randint(60,80)/10)-1],random.randint(1,5),(random.randint(10,30)/100),random.choice(defaultcolor)])
          for particle in particles:
              if button_array[-1][1]:
                  particle[0][1] -=particle[1][0]
              else:
                  particle[0][1] += particle[1][0]
              particle[0][0] += particle[3]
              particle[2]-=0.003
              pygame.draw.circle(screen,particle[4],(int(particle[0][0]),int(particle[0][1])),int(particle[2]))
              if particle[2] <= 0:
                  particles.remove(particle)
      else:
          if button_array[-1][1]:
              particles.append([[random.randint(0,1000),900],[(random.randint(60,80)/10)-1],random.randint(1,5),(random.randint(10,30)/100),random.choice(defaultcolor)])
              particles.append([[random.randint(0,1000),900],[(random.randint(60,80)/10)-1],random.randint(1,5),(random.randint(10,30)/100),random.choice(defaultcolor)])
              for particle in particles:
                  particle[0][1] -= particle[1][0]
                  particle[0][0] += particle[3]
                  particle[2]-=0.003
                  pygame.draw.circle(screen,particle[4],(int(particle[0][0]),int(particle[0][1])),int(particle[2]))
                  if particle[2] <= 0:
                      particles.remove(particle)
                  elif particle[0][1] <= 0:
                      particles.remove(particle)
          else:
              particles.append([[random.randint(0,1000),0],[(random.randint(60,80)/10)-1],random.randint(1,5),(random.randint(10,30)/100),random.choice(defaultcolor)])
              particles.append([[random.randint(0,1000),900],[(random.randint(60,80)/10)-1],random.randint(1,5),(random.randint(10,30)/100),random.choice(defaultcolor)])
              for particle in particles:
                  particle[0][1] +=particle[1][0]
                  particle[0][0] += particle[3]
                  particle[2]-=0.003
                  pygame.draw.circle(screen,particle[4],(int(particle[0][0]),int(particle[0][1])),int(particle[2]))
                  if particle[2] <= 0:
                      particles.remove(particle)
                  elif particle[0][1] >= 901:
                      particles.remove(particle)
      # Array Removal
      if len(particles) >= 300:
          for i in range(100):
              particles.pop(0)
      # Text to Screen
      screen.blit(red,(buttonr.x+20,buttonr.y-15))
      screen.blit(orange,(buttono.x+17,buttono.y-15))
      screen.blit(yellow,(buttony.x+19,buttony.y-25))
      screen.blit(green,(buttong.x+17,buttong.y-15))
      screen.blit(blue,(buttonb.x+20,buttonb.y-15))
      screen.blit(purple,(buttonp.x+19,buttonp.y-15))
      screen.blit(white,(buttonw.x+5,buttonw.y-15))
  
      screen.blit(snowflake,(sflake.x,sflake.y-15))
      screen.blit(follow_mouse,(fmouse.x-10,fmouse.y-15))
      screen.blit(reverse_gravity,(reversegravity.x-5,reversegravity.y-15))
      screen.blit(exit_text,(exitrect.x+15,exitrect.y-15))
    else:
      # Check Start Menu Button
      if 350 <= px <= 750 and 350 <= py <= 450:
          pygame.draw.rect(screen,(0,255,0),startrect)
      else:
          pygame.draw.rect(screen,(25,180,25),startrect)
      screen.blit(start_text,(startrect.x+90,startrect.y-15))
      screen.blit(title_text,(200,50))
    # Update ------------------------------------------------- #
    pygame.display.update()
    mainClock.tick(30)