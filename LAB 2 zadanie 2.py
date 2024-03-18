import pygame
import sys

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Figura")

class BlackCircleWithYellowSquare:
    def __init__(self, circle_radius, square_side_length):
        self.x = width // 2  # Centrum ekranu po osi X
        self.y = height // 2  # Centrum ekranu po osi Y
        self.circle_radius = circle_radius
        self.square_side_length = square_side_length

    def draw(self):
        # Rysowanie białego tła
        screen.fill((255, 255, 255))

        # Rysowanie czarnego koła
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.circle_radius)

        # Rysowanie żółtego kwadratu wewnątrz koła
        square_x = self.x - self.square_side_length / 2
        square_y = self.y - self.square_side_length / 2
        pygame.draw.rect(screen, (255, 255, 0), (square_x, square_y, self.square_side_length, self.square_side_length))


# Główna pętla programu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Tworzenie i rysowanie pierwszej figury
    figure = BlackCircleWithYellowSquare(90, 90)  # Zmienione rozmiary koła i kwadratu
    figure.draw()

    pygame.display.flip()
