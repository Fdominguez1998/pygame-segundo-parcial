import pygame
from class_personaje import *
from configuraciones import *
from pygame.locals import *
from modo import *
from class_enemigo import *
from class_disparo import *
from class_nivel import *
from class_plataforma import *


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

        megaman = Personaje(diccionario_animaciones, 50,160,(90,80), 5, "quieto")

        #plataformas
        piso = Plataforma(False, (ANCHO, 20), (0, 907), "", "SUELO")


        plataforma_caño = Plataforma(True, (150,150), (900, 781), "Imagen juego2\caja.png", "OBSTACULO")

        plataforma_2 = Plataforma(True, (800,50), (1100, 610), "Imagen juego2\Plataforma.png", "ELEVACION")

        

        
        
        

        lista_plataformas = [piso, plataforma_caño , plataforma_2]

        megaman.rectangulo.bottom = piso.rectangulo.top

        #ENEMIGO
        diccionario_animaciones_enemigo = {}
        diccionario_animaciones_enemigo["derecha"] = enemigo_camina_derecha
        diccionario_animaciones_enemigo["izquierda"] = enemigo_camina
        diccionario_animaciones_enemigo["muerto"] = enemigo_muerto
        
        un_enemigo = Enemigo(diccionario_animaciones_enemigo, megaman, "izquierda", 1200, 1700, 3, 3)

        muerto = {"muerto": diccionario_animaciones_enemigo["muerto"]}
        reescalar_imagenes(muerto, (50,25))

        un_enemigo.rectangulo.bottom = plataforma_2.rectangulo.top

        lista_enemigos = [un_enemigo]



    
        super().__init__(pantalla, megaman, lista_enemigos, lista_plataformas, fondo)