import pygame

# Inicializar a pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e icono
pygame.display.set_caption("Invasion Espacial")
icono = pygame.image.load('alien.png')
pygame.display.set_icon(icono)


# Jugador
img_jugador = pygame.image.load("rocket.png")
jugador_x = 368
jugador_y = 536


def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Loop de juego
se_ejecuta = True

while se_ejecuta:
    # rgb
    pantalla.fill((205, 144, 228))
    jugador_x += 0.1

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

    jugador(jugador_x, jugador_y)

    pygame.display.update()

