import pygame
from modo import *





class nivel:
    def __init__(self, pantalla, personaje,lista_enemigos, lista_plataformas, fondo):
        self.pantalla = pantalla
        self.personaje = personaje
        self.plataformas = lista_plataformas
        self.fondo = fondo
        self.enemigos = lista_enemigos

        self.flag_disparo = False
        self.tiempo_ultimo_disparo = 0

    def update(self, lista_eventos):
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    print(evento.pos)
        self.controles()
        self.actualizar_pantalla()
        self.dibujar_rectangulos()  # Agrega esta línea para dibujar los rectángulos en el modo debug

        


    def actualizar_pantalla(self):
        self.pantalla.blit(self.fondo, (0,0))
        
        for plataforma in self.plataformas:
             self.pantalla.blit(plataforma.superficie, plataforma.rectangulo)
            #  plataforma.teletransportar(self.personaje)
            # #  print(plataforma.teletransportar(self.personaje))
        
        for enemigo in  self.enemigos:
            if not enemigo.esta_muerto:
                enemigo.verificar_colision_personaje(self.personaje)
                enemigo.actualizar(self.pantalla)
                enemigo.actualizar_proyectiles(self.pantalla)


        self.personaje.verificar_colision_enemigo(self.enemigos, self.pantalla)
        
        
        

        for enemigo in  self.enemigos:
            if enemigo.esta_muerto:
                self.enemigos.remove(enemigo)

        
        
        self.personaje.actualizar(self.pantalla, self.plataformas)
        self.personaje.actualizar_proyectiles(self.pantalla)
        
        


    #movimientos personaje
    def controles(self):
        teclas = pygame.key.get_pressed()

        if self.personaje.esta_muerto:
            self.personaje.que_hace = "muerto"
        else:
            if teclas[pygame.K_RIGHT]:
                self.personaje.que_hace = "derecha"
                self.flag_disparo = True
            elif teclas[pygame.K_LEFT]:
                self.personaje.que_hace = "izquierda"
                self.flag_disparo = True
            elif self.flag_disparo and teclas[pygame.K_UP]:
                self.personaje.que_hace = "salta"
            else:
                self.personaje.que_hace = "quieto"
                self.flag_disparo = True

            self.personaje.manejar_disparo(teclas)

            if self.flag_disparo and teclas[pygame.K_UP]:
                self.personaje.que_hace = "salta"

            # if self.flag_disparo and teclas[pygame.K_x]:
            #     tiempo_actual = pygame.time.get_ticks()
            #     if tiempo_actual - self.tiempo_ultimo_disparo >= 500:
            #         self.personaje.lanzar_proyectil()
            #         self.flag_disparo = False
            #         self.tiempo_ultimo_disparo = tiempo_actual
    
    def dibujar_rectangulos(self):
    # MODO DEBUG
        if obtener_modo():
            pygame.draw.rect(self.pantalla, "pink", self.personaje.rectangulo, 3)
            
            for enemigo in self.enemigos:
                if not enemigo.esta_muerto:
                    pygame.draw.rect(self.pantalla, "green", enemigo.rectangulo, 3)
                
            for plataforma in self.plataformas:
                pygame.draw.rect(self.pantalla, "red", plataforma.rectangulo, 3)

    def enemigos_muertos(self):
        return all(enemigo.esta_muerto for enemigo in self.enemigos)
                
        