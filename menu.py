# menu.py

import pygame
from pygame.locals import *
from class_boton import Boton

def mostrar_menu(pantalla):
    fondo_menu = pygame.Surface(pantalla.get_size())
    fondo_menu = fondo_menu.convert()
    fondo_menu.fill((0, 0, 0))  # Color blanco

    fondo2_menu = pygame.image.load("Imagenes\Fondo\menu.png").convert()
    fondo2_menu = pygame.transform.scale(fondo2_menu, (600,500))

    titulo_menu = pygame.image.load(r"Imagenes\Fondo\titulo2.png").convert()
    titulo_menu = pygame.transform.scale(titulo_menu, (1200,300))

    font = pygame.font.Font(None, 36)
    # texto_titulo = font.render("Menú Principal", 1, (0, 0, 0))
    # rect_titulo = texto_titulo.get_rect(center=(pantalla.get_width() // 2, 100))

    boton_jugar = Boton("Jugar", 200, 400, 200, 80, (0, 255, 0), (0, 200, 0), iniciar_juego)
    boton_salir = Boton("Salir", 200, 500, 200, 80, (255, 0, 0), (200, 0, 0), salir_juego)

    botones = [boton_jugar, boton_salir]

    bandera_menu = True
    while bandera_menu:
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == QUIT:
                pygame.quit()
                quit()

        for boton in botones:
            boton.actualizar(eventos)

        pantalla.blit(fondo_menu, (0, 0))
        # pantalla.blit(texto_titulo, rect_titulo)
        fondo_menu.blit(titulo_menu, (380, 50))
        fondo_menu.blit(fondo2_menu, (700, 350))
        for boton in botones:
            boton.dibujar(pantalla, font)

        pygame.display.flip()

def iniciar_juego():
    print("Iniciar juego")  # Aquí deberías colocar la lógica para iniciar el juego


def salir_juego():
    pygame.quit()
    quit()
