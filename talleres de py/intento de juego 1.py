import pygame
import random
import sys

# Inicialización de pygame
pygame.init()

# Configuraciones de pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Atrapar Objetos")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 100, 255)
VERDE = (0, 255, 0)

# Reloj para controlar FPS
clock = pygame.time.Clock()
FPS = 60

# Cargar sonidos
# pygame.mixer.music.load("fondo.wav")  # Sonido de fondo
# pygame.mixer.music.play(-1)  # -1 para que suene en bucle
# sonido_perder = pygame.mixer.Sound("perder.wav")  # Sonido al perder

# Jugador (el que atrapa)
jugador = pygame.Rect(375, 550, 60, 20)
velocidad_jugador = 7

# Obstáculos (gusanos negros)
obstaculos = [pygame.Rect(random.randint(0, ANCHO-40), random.randint(100, 400), 40, 20) for _ in range(5)]

# Objetos que caen
objetos = []
contador_caidos = 0  # Si 3 objetos caen, pierdes
tiempo_nuevo_objeto = pygame.USEREVENT + 1
pygame.time.set_timer(tiempo_nuevo_objeto, 1500)  # Cada 1.5 seg cae uno nuevo

# Fondo opcional: pantalla.fill() se sobreescribirá con esta imagen si la tienes
# fondo = pygame.image.load("fondo_juego.png")  # Debe ser 800x600

# Función para mostrar mensaje de derrota
def mostrar_mensaje(texto):
    fuente = pygame.font.SysFont(None, 60)
    mensaje = fuente.render(texto, True, ROJO)
    rect = mensaje.get_rect(center=(ANCHO//2, ALTO//2))
    pantalla.blit(mensaje, rect)
    pygame.display.flip()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()

# Bucle principal
while True:
    pantalla.fill((200, 230, 255))  # Fondo celeste claro
    # pantalla.blit(fondo, (0, 0))  # Si tienes imagen de fondo

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == tiempo_nuevo_objeto:
            objeto = pygame.Rect(random.randint(0, ANCHO-30), 0, 30, 30)
            objetos.append(objeto)

    # Movimiento del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jugador.left > 0:
        jugador.x -= velocidad_jugador
    if teclas[pygame.K_RIGHT] and jugador.right < ANCHO:
        jugador.x += velocidad_jugador

    # Verificar colisión con bordes (izquierda/derecha no pierdes, solo si sales verticalmente)
    if jugador.left <= 0 or jugador.right >= ANCHO:
        pass  # Puedes poner límites si quieres
    if jugador.top <= 0 or jugador.bottom >= ALTO:
        sonido_perder.play()
        mostrar_mensaje("¡Perdiste! Saliste del borde")

    # Dibujar jugador
    pygame.draw.rect(pantalla, AZUL, jugador)

    # Dibujar y verificar colisión con obstáculos
    for obs in obstaculos:
        pygame.draw.rect(pantalla, NEGRO, obs)
        if jugador.colliderect(obs):
            sonido_perder.play()
            mostrar_mensaje("¡Colisionaste con un gusano negro!")

    # Mover objetos y verificar colisiones
    for objeto in list(objetos):
        objeto.y += 5
        pygame.draw.ellipse(pantalla, VERDE, objeto)

        if objeto.colliderect(jugador):
            objetos.remove(objeto)  # Lo atrapaste
        elif objeto.y > ALTO:
            objetos.remove(objeto)
            contador_caidos += 1
            if contador_caidos >= 3:
                sonido_perder.play()
                mostrar_mensaje("¡Perdiste! Dejaste caer 3 objetos")

    # Mostrar contador de fallos
    fuente = pygame.font.SysFont(None, 30)
    texto = fuente.render(f"Objetos caídos: {contador_caidos}/3", True, NEGRO)
    pantalla.blit(texto, (10, 10))

    pygame.display.update()
    clock.tick(FPS)
