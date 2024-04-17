import pygame
from pygame.locals import *
pygame.init()
# Button Intialization
# Color buttons
buttonr,rb = Rect(0,1,100,100),False
buttono,ob = Rect(0,101,100,100),False
buttony,yb = Rect(0,201,100,100),False
buttong,gb = Rect(0,301,100,100),False
buttonb,bb = Rect(0,401,100,100),False
buttonp,pb = Rect(0,501,100,100),False
buttonw,wb = Rect(900,201,100,100),True

# Functionality Buttons
fmouse,fm = Rect(900,401,100,100),False
sflake,sf = Rect(900,301,100,100),True
reversegravity,rg = Rect(900,501,100,100),False
startrect = Rect(300,350,400,100)
exitrect = Rect(900,1,100,100)

button_array = [[(0,1,100,100),False,(200,0,0),(100,0,0)],[(0,101,100,100),False,(255,165,0),(190,115,0)],[(0,201,100,100),False,(255,225,0),(200,190,0)],[(0,301,100,100),False,(0,225,0),(0,128,0)],[(0,401,100,100),False,(0,0,255),(0,0,128)],[(0,501,100,100),False,(159,0,197),(70,0,70)],[(900,201,100,100),True,(255,255,255),(200,200,200)],[(900,401,100,100),False,(170,170,170),(100,100,100)],[(900,301,100,100),True,(170,170,170),(100,100,100)],[(900,501,100,100),False,(170,170,170),(100,100,100)]]
colors = ['red','orange','yellow','green','blue','purple','white']