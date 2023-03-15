import pygame, sys
from pygame.locals import *
from modul import Map

width = 800
height = 700
buttonW = 100
buttonH = 30
margin = 30
space = 20

black = (0,0,0)
grey = (200,200,200)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
purple = (190,0,190)

pygame.init()
pygame.display.set_caption("SLAM environment-making GUI")
screen = pygame.display.set_mode((width,height))
screen.fill(black)
FPS = pygame.time.Clock()

canvas00 = (100, 100)
canvas = pygame.Rect(canvas00, (width-2*canvas00[0], height-2*canvas00[1]))
font = pygame.font.SysFont('Arial', 25)
load = [margin, margin, buttonW, buttonH]
save = [margin+buttonW+space, margin, buttonW, buttonH]
robot = [margin, height-(margin+buttonH), buttonW, buttonH]
landmarks = [margin+buttonW+space, height-(margin+buttonH), buttonW, buttonH]
waypoints = [margin+2*buttonW+2*space, height-(margin+buttonH), buttonW, buttonH]
loadT = font.render('load', True , purple)
saveT = font.render('save', True , purple)
robotT = font.render('robot', True , green)
landmarksT = font.render('landmarks', True , blue)
waypointsT = font.render('waypoints', True , red)

mapa = Map()
switch = ""

while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if((margin <= mouse[0] <= margin+buttonW) and (margin <= mouse[1]<= margin + buttonH)):
                mapa.load()
                switch = ""
            elif((save[0] <= mouse[0] <= save[0]+buttonW) and (margin <= mouse[1]<= margin + buttonH)):
                mapa.save()
                switch = ""
            elif((margin <= mouse[0] <= margin+buttonW) and (robot[1] <= mouse[1]<= robot[1] + buttonH)):
                switch = "r"
            elif((landmarks[0] <= mouse[0] <= landmarks[0]+buttonW) and (landmarks[1] <= mouse[1]<= landmarks[1] + buttonH)):
                switch = "l"
            elif((waypoints[0] <= mouse[0] <= waypoints[0]+buttonW) and (waypoints[1] <= mouse[1]<= waypoints[1] + buttonH)):
                switch = "w"
            elif((canvas00[0] <= mouse[0] <= width-canvas00[0]) and (canvas00[1] <= mouse[1]<= width-canvas00[1])):
                d = {}
                d = {"l": mapa.lm, "w": mapa.wp}
                index = 0
                indexF = int
                minimum = 100000
                for j in d[switch]:
                    a = j[0] + mapa.x[0] + canvas00[0]
                    b = -j[1] + mapa.x[1] + canvas00[1]
                    s = ((a-mouse[0])**2 + (b-mouse[1])**2)**0.5
                    if s < minimum:
                        minimum = s
                        indexF = index
                    index = index + 1
                if minimum < 5:
                    mapa.remove(switch, indexF)
                else:
                    mapa.add(switch, mouse[0]-canvas00[0], mouse[1]-canvas00[1])
     
    screen.fill(black)
    pygame.draw.rect(screen, white, canvas)
    pygame.draw.rect(screen, white, load)
    pygame.draw.rect(screen, white, save)
    pygame.draw.rect(screen, white, robot)
    pygame.draw.rect(screen, white, landmarks)
    pygame.draw.rect(screen, white, waypoints)
    
    if mapa.x:
        x = mapa.x[0] + canvas00[0]
        y = mapa.x[1] + canvas00[1]
        pygame.draw.polygon(screen, green, [(x, y), [x-10, y+30],[x+10, y+30]])
    
    for waypoint in mapa.wp:
        xwp = x + waypoint[0]
        ywp = y - waypoint[1]
        pygame.draw.circle(screen, red, (xwp, ywp), 5)
        
    for landmark in mapa.lm:
        xlm = x + landmark[0] - 5
        ylm = y - landmark[1] - 5
        pygame.draw.rect(screen, blue, (xlm, ylm, 10, 10))
                
    mouse = pygame.mouse.get_pos()
        
    if((margin <= mouse[0] <= margin+buttonW) and (margin <= mouse[1]<= margin + buttonH)):
        pygame.draw.rect(screen, grey, load)
    elif((save[0] <= mouse[0] <= save[0]+buttonW) and (margin <= mouse[1]<= margin + buttonH)):
        pygame.draw.rect(screen, grey, save)
    elif((margin <= mouse[0] <= margin+buttonW) and (robot[1] <= mouse[1]<= robot[1] + buttonH)):
        pygame.draw.rect(screen, grey, robot)
    elif((landmarks[0] <= mouse[0] <= landmarks[0]+buttonW) and (landmarks[1] <= mouse[1]<= landmarks[1] + buttonH)):
        pygame.draw.rect(screen, grey, landmarks)
    elif((waypoints[0] <= mouse[0] <= waypoints[0]+buttonW) and (waypoints[1] <= mouse[1]<= waypoints[1] + buttonH)):
        pygame.draw.rect(screen, grey, waypoints)
    
    screen.blit(loadT, (load[0]+32, load[1]+6))
    screen.blit(saveT, (save[0]+31, save[1]+6))
    screen.blit(robotT, (robot[0]+28, robot[1]+6))
    screen.blit(landmarksT, (landmarks[0]+5, landmarks[1]+6))
    screen.blit(waypointsT, (waypoints[0]+6, waypoints[1]+6))
    
    pygame.display.update()
    FPS.tick(30)
