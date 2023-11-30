import pygame
from class_personaje import *
from configuraciones import *
from pygame.locals import *
from modo import *
from class_enemigo import *
from class_disparo import *
from class_nivel import *
from nivel_uno import *
from nivel_dos import *
from menu import *

##############################INICIALIZACIONES##########################################

#############Pantalla##########

ANCHO, ALTO = 1920, 1020
FPS = 30  # Para desacelerar la pantalla

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))  # En pixeles
pygame.display.set_caption("JUEGO MEGAMAN")

# Mostrar el menú antes de iniciar el juego
#mostrar_menu(PANTALLA)

###Nivel###
nivel_actual = nivel_uno(PANTALLA)
segundo_nivel = nivel_dos(PANTALLA)

bandera = True
while bandera:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    for evento in eventos :
        if evento.type == QUIT:
            bandera = False
    
    nivel_actual.update(eventos)
    pygame.display.update()
    
    


pygame.quit()
