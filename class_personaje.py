from configuraciones import *
from class_enemigo import *
from class_disparo import *

class Personaje:
    def __init__(self,animaciones, pos_x, pos_y, tamaño, velocidad, que_hace):
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, tamaño)
        self.rectangulo = pygame.Rect(pos_x,pos_y, *tamaño) #primera forma
        # self.rectangulo = self.animaciones["quieto"][0].get_rect() #De esta forma, toma el rectangulo de la imagen
        self.rectangulo.x = pos_x
        self.rectangulo.y = pos_y
        self.velocidad = velocidad
        self.que_hace = que_hace
        self.contador_pasos = 0        
        self.animacion_actual = self.animaciones[self.que_hace]

        self.gravedad = 3
        self.desplazamiento_y = 0
        self.potencia_salto = -30
        self.limite_velocidad_salto = 20
        self.esta_saltando = False

        self.esta_muerto = False
        self.vida = 100
    
        self.lista_proyectiles =[]

    def aplicar_gravedad(self, pantalla, lista_plataformas):
        if self.esta_saltando:
            self.animar(pantalla)
            self.rectangulo.y+= self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad <self.limite_velocidad_salto:
                self.desplazamiento_y += self.gravedad
                
        for plataforma in lista_plataformas:
            if self.rectangulo.colliderect(plataforma["rectangulo"]):
                self.esta_saltando = False
                self.desplazamiento_y = 0
                self.rectangulo.bottom = plataforma["rectangulo"].top
                break
            else:
                self.esta_saltando = True

    def desplazar(self):
        velocidad_actual = self.velocidad
        if self.que_hace == "izquierda":
            velocidad_actual *= -1
        
        self.rectangulo.x += velocidad_actual

    def animar(self, pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rectangulo)
        self.contador_pasos += 1

    #Que hace el personaje
    def actualizar(self, pantalla, lista_plataformas):
        match self.que_hace:
            case "derecha":
                if not self.esta_saltando and not self.esta_muerto:
                    self.animacion_actual = self.animaciones["derecha"]
                    self.animar(pantalla)
                self.desplazar()
            case "izquierda":
                if not self.esta_saltando and not self.esta_muerto:
                    self.animacion_actual = self.animaciones["izquierda"]
                    self.animar(pantalla)
                self.desplazar()
            case "quieto":
                if not self.esta_saltando and not self.esta_muerto:
                    self.animacion_actual = self.animaciones["quieto"]
                    self.animar(pantalla)
            case "salta":
                if not self.esta_saltando and not self.esta_muerto:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
                    self.animacion_actual = self.animaciones["salta"]

            case "dispara":
                if not self.esta_saltando and not self.esta_muerto:
                    self.animacion_actual = self.animaciones["dispara"]
                    self.animar(pantalla)

            case "muere":
                if self.esta_muerto:
                    self.animacion_actual = self.animaciones["muere"]
                    self.animar(pantalla)

        self.actualizar_proyectiles(pantalla)
        self.aplicar_gravedad(pantalla, lista_plataformas)
    
    def verificar_colision_enemigo(self, lista_enemigos, pantalla):

       # Verifica colisión del personaje con el enemigo
        for enemigo in lista_enemigos:
            if self.rectangulo.colliderect(enemigo.rectangulo) and not enemigo.esta_muerto:
                self.esta_muerto = True
                
                self.animacion_actual = self.animaciones["muere"]
                self.animar(pantalla)

        # Verificar colisión de los proyectiles con el enemigo  
        for p in self.lista_proyectiles:
            for enemigo in lista_enemigos:
                if not enemigo.esta_muerto and p.verificar_colision_enemigo(enemigo):
                    enemigo.vida -= 25
                    print(enemigo.vida)
                    #enemigo.rectangulo.y += 10
                    self.lista_proyectiles.remove(p)
                    if enemigo.vida == 0:
                        enemigo.esta_muriendo = True
                        enemigo.animacion_actual = enemigo.animaciones["muerto"]
                        enemigo.animar(pantalla)
                

    def lanzar_proyectil(self):
        
        x = None
        margen = 10
        y = self.rectangulo.centery

        if self.que_hace =="derecha" or self.que_hace == "quieto":
            x = self.rectangulo.right - margen
        elif self.que_hace == "izquierda":
            x = self.rectangulo.left - 100 + margen
        
        if x is not None:
            nuevo_proyectil = disparo(x, y, self.que_hace)
            self.lista_proyectiles.append(nuevo_proyectil)

    
    def actualizar_proyectiles(self, pantalla):
        i = 0
        while i < len(self.lista_proyectiles):
            p = self.lista_proyectiles[i]
            p.actualizar(pantalla)
            if p.rectangulo.centerx < 0 or p.rectangulo.centerx > pantalla.get_width():
                self.lista_proyectiles.pop(i)
            else:
                i += 1

    def manejar_disparo(self, teclas):
        global flag_disparo, tiempo_ultimo_disparo
        if flag_disparo and teclas[pygame.K_x]:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - tiempo_ultimo_disparo >= 500:
                self.lanzar_proyectil()
                flag_disparo = False
                tiempo_ultimo_disparo = tiempo_actual
           
            




# caracteristicas
# atributo
#         rectangulo
#         animaciones
#         tamaño
#         posicion
#         velocidad

# acciones
# metodos
#         correr
#         caminar
#         saltar
#         agacharse
#         agacharse
#         animar
#         atacar