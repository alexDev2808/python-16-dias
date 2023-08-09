import pygame

# Inicializar a pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e icono
pygame.display.set_caption("Invasion Espacial")
icono = pygame.image.load('alien.png')
pygame.display.set_icon(icono)

# Loop de juego
se_ejecuta = True

while se_ejecuta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

    pantalla.fill((205, 144, 228))
    pygame.display.update()

