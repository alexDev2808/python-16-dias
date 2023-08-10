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
jugador_x_cambio = 0


# Funcion del jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Loop de juego
se_ejecuta = True

while se_ejecuta:
    # rgb
    pantalla.fill((205, 144, 228))

#    Iterar eventos
    for evento in pygame.event.get():

        # Evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Evento presionar flechas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio -= 0.4
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio += 0.4

        # Evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

#   Modificar ubicacion
    jugador_x += jugador_x_cambio

    # mantener dentro del borde
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    jugador(jugador_x, jugador_y)

    # actualizar
    pygame.display.update()

