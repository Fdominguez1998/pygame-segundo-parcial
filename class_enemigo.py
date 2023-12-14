from configuraciones import *
from class_disparo import *

class Enemigo:
    def __init__(self, animaciones, heroe, que_hace, punto_inicial, punto_final, velocidad, velocidad_detectado):
        self.hero = heroe
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, (90,80))
        # self.rectangulo = self.animaciones["izquierda"][0].get_rect()
        self.rectangulo = pygame.Rect(punto_inicial, 824, 100, 85)
        self.contador_pasos = 0
        self.que_hace = que_hace

        self.animacion_actual = animaciones["izquierda"]
        self.esta_muerto = False
        self.esta_muriendo = False
        self.vida = 100
        self.direccion = 1 
        
        self.velocidad_patrulla = velocidad
        self.velocidad_detectado = velocidad_detectado

        #inteligencia artificial
        self.cambio_direccion_timer = pygame.time.get_ticks()
        self.cambio_direccion_intervalo = 2000  # Cambiar la dirección cada 2000 milisegundos (2 segundos)
        
        self.tiempo_ultimo_disparo = 0
        self.lista_proyectiles = []

        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

        #sonidos#
        self.sonido_disparo = sonido_disparo_enemigo

    def animar(self, pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        if self.direccion == 1:
            self.animacion_actual = self.animaciones["derecha"]
        else:
            self.animacion_actual = self.animaciones["izquierda"]

        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rectangulo)
        self.contador_pasos += 1

        if self.esta_muriendo and self.contador_pasos == largo:
            self.esta_muerto = True

        

       
                

    def cambiar_direccion(self):
        self.direccion *= -1  # Cambiar la dirección invirtiendo el valor actual        

    
    def avanzar(self):
        # Ajustar la velocidad según la dirección
        
        self.rectangulo.x += self.velocidad * self.direccion

    def actualizar(self, pantalla):
        self.ia()
        self.animar(pantalla)
        self.avanzar()

    def ia(self):
        distancia_horizontal = abs(self.hero.rectangulo.x - self.rectangulo.x)
        y_heroe = self.hero.rectangulo.y
        y_enemigo = self.rectangulo.y

        if distancia_horizontal < ((25 * pygame.display.get_surface().get_width()) / 100) and abs(
                y_heroe - y_enemigo) < 100:
            if self.hero.rectangulo.x > self.rectangulo.x:
                self.que_hace = "derecha"
            else:
                self.que_hace = "izquierda"
            self.lanzar_proyectil()
            self.velocidad = self.velocidad_detectado
        else:
            if self.rectangulo.x <= self.punto_inicial:
                self.direccion = 1
            elif self.rectangulo.x >= self.punto_final:
                self.direccion = -1
            self.velocidad = self.velocidad_patrulla

        self.rectangulo.x += self.velocidad * self.direccion



    def lanzar_proyectil(self):
        tiempo_actual = pygame.time.get_ticks()

        if tiempo_actual - self.tiempo_ultimo_disparo >= 1000:
            # Verificar la posición del héroe antes de disparar
            if (self.direccion == 1 and self.hero.rectangulo.x > self.rectangulo.x) or \
               (self.direccion == -1 and self.hero.rectangulo.x < self.rectangulo.x):
                x = None
                margen = 10
                y = self.rectangulo.centery

                if self.que_hace == "derecha" or self.que_hace == "quieto":
                    x = self.rectangulo.right - margen
                elif self.que_hace == "izquierda":
                    x = self.rectangulo.left - 100 + margen

                if x is not None:
                    nuevo_proyectil = disparo(x, y, self.direccion, 15, r"Imagen juego2\25.png")
                    self.lista_proyectiles.append(nuevo_proyectil)

                    self.sonido_disparo.play()

                self.tiempo_ultimo_disparo = tiempo_actual

    
    def actualizar_proyectiles(self, pantalla):
        i = 0
        while i < len(self.lista_proyectiles):
            p = self.lista_proyectiles[i]
            p.actualizar(pantalla)

            # Actualizar posición del proyectil en función de su dirección
            p.rectangulo.x += p.velocidad * p.direccion

            if p.rectangulo.centerx < 0 or p.rectangulo.centerx > pantalla.get_width():
                self.lista_proyectiles.pop(i)
            else:
                i += 1

    def manejar_disparo(self, teclas):
        flag_disparo, tiempo_ultimo_disparo
        if flag_disparo and teclas[pygame.K_x]:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - tiempo_ultimo_disparo >= 500:
                self.lanzar_proyectil()
                flag_disparo = False
                tiempo_ultimo_disparo = tiempo_actual

    def verificar_colision_personaje(self, personaje):
        for p in self.lista_proyectiles:
            if p.verificar_colision_personaje(personaje):
                personaje.vida -= 20
                personaje.puntaje_total -= 200  # Restar puntos al puntaje total
                
                self.lista_proyectiles.remove(p)

                if personaje.vida <= 0:
                    personaje.esta_muerto = True
                    personaje.animacion_actual = personaje.animaciones["muere"]

        


    
    
    