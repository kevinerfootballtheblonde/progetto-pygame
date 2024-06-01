import pygame, sys, os
from pygame.locals import*
from random import randint
os.system("cls")
pygame.init()


sfondo = pygame.image.load("immagini//sfondo.jpg")
uccello =pygame.image.load("immagini//uccello.png")
uccello = pygame.transform.scale(uccello, (40, 40))
uccello_rect = uccello.get_rect()
uccello_rect = uccello_rect.scale_by(30,30)
base = pygame.image.load("immagini//base.png")
gameover = pygame.image.load("immagini//gameover.png")
gameover = pygame.transform.scale(gameover, (200, 100))
tubogiù = pygame.image.load("immagini//tubosu.png")
# tubogiù = pygame.transform.scale(tubogiù, (200, 200))
tubosù = pygame.image.load("immagini//tubogiu.png")
# tubosù = pygame.transform.scale(tubosù, (200, 200))

window_size= (288, 470)
screen= pygame.display.set_mode(window_size)
clock=pygame.time.Clock()
fps= 50
vel_avanz = 3
Font = pygame.font.SysFont("Comic Sans MS", 50, bold = True)

class Tubi:
    def __init__(self):
        self.x = 200
        self.y = randint(-75, 0)
        self.collide_recta = pygame.rect.Rect(self.x,  self.y, 90, self.y+120)
    
    def avanza_e_disegna(self):
        self.x -= vel_avanz
        self.collide_recta.x -= vel_avanz
        screen.blit(tubogiù,(self.x,self.y+210))
        screen.blit(tubosù, (self.x, self.y - 210))
    
    def fra_i_tubi(self,uccello,uccellox):
        tollera = 5
        uccello_lato_dx = uccellox + uccello.get_width() - tollera
        uccello_lato_sx = uccellox + tollera
        tubisx = self.x
        tubidx = self.x + tubogiù.get_width()
        if uccello_lato_dx > tubisx and uccello_lato_sx < tubidx:
            return True


def disegna_oggetti(): 
    screen.blit(sfondo, (0,0))
    for t in tubi:
        t.avanza_e_disegna()
    screen.blit(uccello, (uccellox, uccelloy))
    screen.blit(base,(basex,400))
    punti_render = Font.render(str(punti), 1,(255,255,255))
    screen.blit(punti_render,(139,0))

def aggiorna(): 
    pygame.display.update()
    clock.tick(fps)

def inizio(): 
    global uccellox, uccelloy, uccello_vely
    global basex
    global tubi
    global punti
    global fra_i_tubi 
    uccellox, uccelloy= 60, 150
    uccello_vely = 0
    basex = 0
    punti = 0
    tubi = []
    fra_i_tubi = False
    tubi.append(Tubi())

def perso():
    disegna_oggetti()
    screen.blit(gameover,(50,180))
    aggiorna()
    rinizio = False
    while not rinizio:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                inizio()
                rinizio = True
            if event.type == pygame.QUIT:
                pygame.quit()

inizio()

while True:
    basex -= vel_avanz
    if basex < -45:
        basex = 0
    uccello_vely += 1
    uccelloy += uccello_vely

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            uccello_vely = -10

        if event.type == QUIT:
            pygame.quit()

    if tubi[-1].x < 100 :
        tubi.append(Tubi())
    
    for t in tubi:
        t.collisione(uccello,uccellox,uccelloy)
    
    if not fra_i_tubi:
        for t in tubi:
            if t.fra_i_tubi(uccello,uccellox):
                fra_i_tubi = True
                break
    
    if fra_i_tubi:
        fra_i_tubi = False
        for t in tubi:
            if t.fra_i_tubi(uccello,uccellox):
                fra_i_tubi = True
                break
        if not fra_i_tubi:
            punti += 1
    if uccelloy > 380:
        perso()

    disegna_oggetti()
    aggiorna()