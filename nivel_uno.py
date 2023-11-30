import pygame
from class_personaje import *
from configuraciones import *
from pygame.locals import *
from modo import *
from class_enemigo import *
from class_disparo import *
from class_nivel import *
from plataformas import *


class nivel_uno(nivel):
    def __init__(self, pantalla):
        ##############################INICIALIZACIONES##########################################

        #############Pantalla##########

        ANCHO = pantalla.get_width()
        ALTO = pantalla.get_height()

        
        #Fondo

        fondo = pygame.image.load(r"Imagenes\Fondo\0.png").convert()#Acelera el juego y hace que consuma menos recursos
        fondo = pygame.transform.scale(fondo, (ANCHO, ALTO)) 


        #personaje
        diccionario_animaciones = {}
        diccionario_animaciones["derecha"] = personaje_derecha
        diccionario_animaciones["izquierda"] = personaje_izquierda
        diccionario_animaciones["quieto"] = personaje_quieto
        diccionario_animaciones["salta"] = personaje_salta
        diccionario_animaciones["dispara"] = personaje_dispara
        diccionario_animaciones["muere"] = personaje_muere

        mario = Personaje(diccionario_animaciones, 50,160,(90,80), 15, "quieto")

        #plataformas
        piso = crear_plataforma(False, (ANCHO, 20), (0, 907))


        plataforma_caño = crear_plataforma(True, (150,150), (900, 781), "Imagen juego2\caja.png")

        plataforma_2 = crear_plataforma(True, (800,50), (1100, 610), "Imagen juego2\Plataforma.png")

        plataforma_3 = crear_plataforma(True, (800,50), (100, 470), "Imagen juego2\Plataforma.png")

        portal = crear_plataforma(True, (150,150), (100, 300), "Imagen juego2\portal.png")
        
        

        lista_plataformas = [piso, plataforma_caño , plataforma_2, plataforma_3, portal]

        mario.rectangulo.bottom = piso["rectangulo"].top

        #ENEMIGO
        diccionario_animaciones_enemigo = {"izquierda" : enemigo_camina, "derecha" : enemigo_camina_derecha, "muerto": enemigo_muerto}
        un_enemigo = Enemigo(diccionario_animaciones_enemigo)
        d = {"muerto": diccionario_animaciones_enemigo["muerto"]}
        reescalar_imagenes(d, (50,25))

        un_enemigo.rectangulo.bottom = piso["rectangulo"].top

        lista_enemigos = [un_enemigo]



    
        super().__init__(pantalla, mario, lista_enemigos, lista_plataformas, fondo)