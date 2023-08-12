import math
import pygame
import random

# Inicializar a pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e icono
pygame.display.set_caption("Invasion Espacial")
icono = pygame.image.load('alien.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load("Fondo.jpg")


# Jugador
img_jugador = pygame.image.load("rocket.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# Enemigo
img_enemigo = pygame.image.load("space-ship.png")
enemigo_x = random.randint(0, 736)
enemigo_y = random.randint(50, 200)
enemigo_x_cambio = 0.5
enemigo_y_cambio = 50

# Variables de bala
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 3
bala_visible = False

# Puntaje
puntaje = 0


# Funcion del jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Funcion del enemigo
def enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))


# Funcion disparar bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


# Funcion detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False


# Loop de juego
se_ejecuta = True

while se_ejecuta:
    # rgb
    # pantalla.fill((205, 144, 228))

    # Imagen de fondo
    pantalla.blit(fondo, (0, 0))

#    Iterar eventos
    for evento in pygame.event.get():

        # Evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -1
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 1
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        # Evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

#   Modificar ubicacion del jugador
    jugador_x += jugador_x_cambio

    # mantener dentro del borde al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # Modificar ubicacion del enemigo
    enemigo_x += enemigo_x_cambio

    # mantener dentro del borde al enemigo
    if enemigo_x <= 0:
        enemigo_x_cambio = 1
        enemigo_y += enemigo_y_cambio
    elif enemigo_x >= 736:
        enemigo_x_cambio = -1
        enemigo_y += enemigo_y_cambio

    # Movimiento bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    # colision
    colision = hay_colision(enemigo_x, enemigo_y, bala_x, bala_y)
    if colision:
        bala_y = 500
        bala_visible = False
        puntaje += 1
        print(puntaje)
        enemigo_x = random.randint(0, 736)
        enemigo_y = random.randint(50, 200)

    jugador(jugador_x, jugador_y)
    enemigo(enemigo_x, enemigo_y)

    # actualizar
    pygame.display.update()

