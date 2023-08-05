import pygame, sys
from pygame.locals import *
from modul import Map


width = 800
height = 700
buttonW = 75
buttonH = 30
buttonBigW = 110
margin = 36
space = 20
center = [width/2, height/2]

black = (0,0,0)
grey = (120,120,120)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
pink = (255,0,255)

pygame.init()
pygame.display.set_caption("SLAM environment-making GUI")
screen = pygame.display.set_mode((width,height))
screen.fill(grey)
FPS = pygame.time.Clock()

canvas00 = (100, 100)
canvas = pygame.Rect(canvas00, (width-2*canvas00[0], height-2*canvas00[1]))
font = pygame.font.Font(size=25)
load = [margin, margin, buttonW, buttonH]
save = [margin+buttonW+space, margin, buttonW, buttonH]
robot = [margin, height-(margin+buttonH), buttonBigW, buttonH]
input_rect = pygame.Rect(robot[0], robot[1]+buttonH, buttonBigW, buttonH)
landmarks = [margin+buttonBigW+space, height-(margin+buttonH), buttonW, buttonH]
waypoints = [margin+2*buttonBigW+2*space, height-(margin+buttonH), buttonW, buttonH]

loadT = pygame.image.load('load.png')
loadT = pygame.transform.scale(loadT, (buttonW, buttonH))
loadTM = pygame.image.load('loadM.png')
loadTM = pygame.transform.scale(loadTM, (buttonW, buttonH))

saveT = pygame.image.load('save.png')
saveT = pygame.transform.scale(saveT, (buttonW, buttonH))
saveTM = pygame.image.load('saveM.png')
saveTM = pygame.transform.scale(saveTM, (buttonW, buttonH))

robotT = pygame.image.load('r.png')
robotT = pygame.transform.scale(robotT, (buttonBigW, buttonH))
robotTM = pygame.image.load('rM.png')
robotTM = pygame.transform.scale(robotTM, (buttonBigW, buttonH))

landmarksT = pygame.image.load('lm.png')
landmarksT = pygame.transform.scale(landmarksT, (buttonBigW, buttonH))
landmarksTM = pygame.image.load('lmM.png')
landmarksTM = pygame.transform.scale(landmarksTM, (buttonBigW, buttonH))

waypointsT = pygame.image.load('wp.png')
waypointsT = pygame.transform.scale(waypointsT, (buttonBigW, buttonH))
waypointsTM = pygame.image.load('wpM.png')
waypointsTM = pygame.transform.scale(waypointsTM, (buttonBigW, buttonH))

robotW = 20
robotH = 30
triangle = pygame.image.load('robot.png')
triangle0 = pygame.transform.scale(triangle, (robotH, robotW))

mapa = Map()
switch = ""
user_text = ""
phi = 0

  
while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if (event.type == pygame.KEYDOWN) and (switch == "r"):
            if event.key == pygame.K_RETURN:
                switch = ""
            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
                phi = mapa.add(switch, phi = user_text)
            else:
                user_text += event.unicode
                phi = mapa.add(switch, phi = user_text)
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if((margin <= mouse[0] <= margin+buttonW) and (margin <= mouse[1]<= margin + buttonH)):
                mapa.load()
                switch = ""
                user_text = str(mapa.x3)
                phi = mapa.x3
            elif((save[0] <= mouse[0] <= save[0]+buttonW) and (margin <= mouse[1]<= margin + buttonH)):
                mapa.save()
                switch = ""
            elif((margin <= mouse[0] <= margin+buttonBigW) and (robot[1] <= mouse[1]<= robot[1] + buttonH)):
                switch = "r"
            elif((landmarks[0] <= mouse[0] <= landmarks[0]+buttonBigW) and (landmarks[1] <= mouse[1]<= landmarks[1] + buttonH)):
                switch = "l"
            elif((waypoints[0] <= mouse[0] <= waypoints[0]+buttonBigW) and (waypoints[1] <= mouse[1]<= waypoints[1] + buttonH)):
                switch = "w"
            elif((canvas00[0] <= mouse[0] <= width-canvas00[0]) and (canvas00[1] <= mouse[1]<= width-canvas00[1])):
                if (switch == "l") or (switch == "w"):
                    d = {}
                    d = {"l": mapa.lm, "w": mapa.wp}
                    distances = []
                    minimum = 100000
                    for j in d[switch]:
                        a = j[0] + center[0]
                        b = -j[1] + center[1]
                        s = ((a-mouse[0])**2 + (b-mouse[1])**2)**0.5
                        distances.append(s)
                        if s < minimum:
                            minimum = s
                    if minimum < 5:
                        index = distances.index(minimum)
                        mapa.remove(switch, index)
                    else:
                        mapa.add(switch, mouse[0]-center[0], mouse[1]-center[1])
     
    screen.fill(grey)
    pygame.draw.rect(screen, white, canvas)    
    triangle = pygame.transform.rotate(triangle0, phi)
    screen.blit(triangle, (center[0] - triangle.get_width()/2, center[1] - triangle.get_height()/2))
    screen.blit(loadT, (load[0], load[1]))
    screen.blit(landmarksT, (landmarks[0], landmarks[1]))
    screen.blit(saveT, (save[0], save[1]))
    screen.blit(waypointsT, (waypoints[0], waypoints[1]))
    screen.blit(robotT, (robot[0], robot[1]))
    
    xwp0 = center[0]
    ywp0 = center[1]
    for waypoint in mapa.wp:
        xwp = center[0] + waypoint[0]
        ywp = center[1] - waypoint[1]
        pygame.draw.circle(screen, red, (xwp, ywp), 5)
        pygame.draw.line(screen, pink, (xwp0, ywp0), (xwp, ywp), 2)
        xwp0 = xwp
        ywp0 = ywp
        
    for landmark in mapa.lm:
        xlm = center[0] + landmark[0] - 5
        ylm = center[1] - landmark[1] - 5
        pygame.draw.rect(screen, blue, (xlm, ylm, 10, 10))
                
    mouse = pygame.mouse.get_pos()
        
    if((margin <= mouse[0] <= margin+buttonW) and (margin <= mouse[1]<= margin + buttonH)):
        screen.blit(loadTM, (load[0], load[1]))
    elif((save[0] <= mouse[0] <= save[0]+buttonW) and (margin <= mouse[1]<= margin + buttonH)):
        screen.blit(saveTM, (save[0], save[1]))
    elif((margin <= mouse[0] <= margin+buttonBigW) and (robot[1] <= mouse[1]<= robot[1] + buttonH)):
        screen.blit(robotTM, (robot[0], robot[1]))
    elif((landmarks[0] <= mouse[0] <= landmarks[0]+buttonBigW) and (landmarks[1] <= mouse[1]<= landmarks[1] + buttonH)):
        screen.blit(landmarksTM, (landmarks[0], landmarks[1]))
    elif((waypoints[0] <= mouse[0] <= waypoints[0]+buttonBigW) and (waypoints[1] <= mouse[1]<= waypoints[1] + buttonH)):
        screen.blit(waypointsTM, (waypoints[0], waypoints[1]))
          
    if switch == "r":
        pygame.draw.rect(screen, white, input_rect)  
        text_surface = font.render(user_text, True, black)
        screen.blit(text_surface, (input_rect.x+10, input_rect.y+10))
    
    pygame.display.update()
    FPS.tick(30)
