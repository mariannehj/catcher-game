# -*- coding: utf-8 -*-
import pygame as pg
import sys, random

# Konstanter
WIDTH = 400
HEIGHT = 600

# Størrelsen til vinduet
SIZE = (WIDTH, HEIGHT)

# Frames per second (bilder per sekund)
FPS = 60

# Farger (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (130, 130, 130)
LIGHTBLUE = (120, 120, 255)

# Initiere pygame
pg.init()

# Lager en overflate (surface) vi kan tegne på
surface = pg.display.set_mode(SIZE)

# Lager en klokke
clock = pg.time.Clock()

# Variabel som styrer om spillet skal kjøres
run = True

# Verdier for spilleren
w = 60 # bredde
h = 80 # høyde

# Startposisjon
x = WIDTH//2
y = HEIGHT - h - 10

# Henter bilde til spilleren
player_img = pg.image.load('bucket.png')

# Henter bilde for bakgrunn
background_img = pg.image.load('background_snow_2-3.png')

# Tilpasser bakgrunnsbilde til vår skjermstørrelse
background_img = pg.transform.scale(background_img, SIZE)


# Henter font
font = pg.font.SysFont('Arial', 26)

# Antall poeng
poeng = 0

# Funksjon som viser antall poeng
def display_points():
    text_img = font.render(f"Antall poeng: {poeng}", True, WHITE)
    surface.blit(text_img, (20, 10))


class Ball:
    def __init__(self):
        self.r = 10
        #self.x = WIDTH//2
        self.x = random.randint(self.r, WIDTH-self.r)
        self.y = -self.r
        
    def update(self):
        self.y += 5
    
    def draw(self):
        pg.draw.circle(surface, WHITE, (self.x, self.y), self.r)


# Lager et ball-objekt
ball = Ball()


# Spill-løkken
while run:
    # Sørger for at løkken kjører i korrekt hastighet
    clock.tick(FPS)
    
    # Går gjennom henselser (events)
    for event in pg.event.get():
        # Sjekker om vi ønsker å lukke vinduet
        if event.type == pg.QUIT:
            run = False # Spillet skal avsluttes
            
            
    # Fyller skjermen med en farge
    #surface.fill(LIGHTBLUE)
    
    # Bruker bakgrunnsbildet
    surface.blit(background_img, (0,0))
    
    # Hastigheten til spilleren
    vx = 0
    
    # Henter knappene fra tastaturet som trykkes på
    keys = pg.key.get_pressed()
    
    # Sjekker om ulike taster trykkes på
    if keys[pg.K_LEFT]:
        vx = -5
        
    elif keys[pg.K_RIGHT]:
        vx = 5

    # Oppdaterer posisjonen til rektangelet
    x += vx
    
    
    # Ball
    ball.update()
    ball.draw()
    
    # Sjekker kollisjon
    if ball.y > y and x < ball.x < x+w:
        poeng += 1 # Øker antall poeng
        ball = Ball()
        
    # Sjekker om vi ikke klarer å fange ballen
    if ball.y + ball.r > HEIGHT:
        print("Du klarte ikke å fange ballen")
        print(f"Du fikk {poeng} poeng")
        run = False # Game over
    
    # Spiller
    #pg.draw.rect(surface, GREY, [x, y, w, h])
    surface.blit(player_img, (x, y))
    
    # Viser antall poeng på skjermen
    display_points()

    # "Flipper" displayet for å vise hva vi har tegnet
    pg.display.flip()


# Avslutter pygame
pg.quit()
sys.exit()





