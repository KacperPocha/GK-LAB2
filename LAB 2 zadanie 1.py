import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("First Game")

# Deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZOLTY = (255, 255, 0)

def draw_skewed_octagon(surface, color, center, size, angle_offset, skew, vertical_offset, flatten, horizontal_flip, horizontal_offset):
    points = []
    for i in range(8):
        angle = math.radians(45 * i + angle_offset)
        x = center[0] + size * math.cos(angle) + skew * math.sin(angle) + horizontal_offset
        if horizontal_flip:
            x = 2 * center[0] - x  # Odwracanie horyzontalne
        y = (center[1] + size * math.sin(angle) + vertical_offset) * flatten
        points.append((x, y))
    pygame.draw.polygon(surface, color, points)

octagon_size = 100 #rozmiar
octagon_angle = 0 #kąt pochylenia
skew = 0  #wartość przechylenia
vertical_offset = 0  #przesunięcie wertykalne
flatten = 1.0  #wartość spłaszczenia
horizontal_flip = False  #obrót horyzontalnt
horizontal_offset = 0 #przesunięcie horyzontalne

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        octagon_size = max(50, octagon_size - 10)
        octagon_angle = 0
        skew = 0 
        vertical_offset = 0 
        flatten = 1.0  
        horizontal_flip = False  
        horizontal_offset = 0 
    if keys[pygame.K_2]:
        octagon_angle += 45
        octagon_size = 100
        skew = 0  
        vertical_offset = 0 
        flatten = 1.0 
        horizontal_flip = False  
        horizontal_offset = 0 
    if keys[pygame.K_3]:
        octagon_size = 100
        octagon_angle = 180
        skew = 0 
        vertical_offset = 0 
        flatten = 1.0  
        horizontal_flip = False  
        horizontal_offset = 0 
    if keys[pygame.K_4]:
        skew = 40 
        octagon_size = 100
        octagon_angle = 0
        vertical_offset = 0 
        flatten = 1.0 
        horizontal_flip = False  
        horizontal_offset = 0 
    if keys[pygame.K_5]:
        vertical_offset = -200 
        flatten = 0.2  
        octagon_size = 100
        octagon_angle = 0
        skew = 0 
        horizontal_flip = False  
        horizontal_offset = 0 
    if keys[pygame.K_6]:
        octagon_size = 100
        octagon_angle = 240
        skew = -50 
        vertical_offset = 0 
        flatten = 1.0  
        horizontal_flip = False  
        horizontal_offset = 0 
    if keys[pygame.K_7]:
        octagon_size = 100
        octagon_angle = 180
        skew = 0  
        vertical_offset = 0  
        flatten = 1.0  
        horizontal_flip = True 
        horizontal_offset = 0 
    if keys[pygame.K_8]:
        octagon_size = 100
        vertical_offset = 750  
        horizontal_offset = -50
        flatten = 0.4  
        octagon_angle = 45
        skew = 90
        horizontal_flip = False
    if keys[pygame.K_9]:
        octagon_size = 100
        octagon_angle = 180
        skew = 70
        vertical_offset = 0  
        flatten = 1.0  
        horizontal_flip = False  
        horizontal_offset = 180
    if keys[pygame.K_0]:
        octagon_size = 100
        octagon_angle = 0
        skew = 0  
        vertical_offset = 0  
        flatten = 1.0  
        horizontal_flip = False  
        horizontal_offset = 0 

    win.fill(ZOLTY)
    draw_skewed_octagon(win, CZERWONY, (300, 300), octagon_size, octagon_angle, skew, vertical_offset, flatten, horizontal_flip, horizontal_offset)


    pygame.display.update()
