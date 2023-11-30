from configuraciones import *

class Enemigo:
    def __init__(self, animaciones):
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, (90,80))
        # self.rectangulo = self.animaciones["izquierda"][0].get_rect()
        self.rectangulo = pygame.Rect(1200, 824, 100, 85)
        self.contador_pasos = 0

        self.animacion_actual = animaciones["izquierda"]
        self.esta_muerto = False
        self.esta_muriendo = False
        self.vida = 100
        self.direccion = 1
        #inteligencia artificial
        self.cambio_direccion_timer = pygame.time.get_ticks()
        self.cambio_direccion_intervalo = 2000  # Cambiar la dirección cada 2000 milisegundos (2 segundos)
        

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
        velocidad = 5  # Puedes ajustar este valor según la velocidad deseada
        self.rectangulo.x += velocidad * self.direccion

    def actualizar(self, pantalla):
        self.ia()
        self.animar(pantalla)
        self.avanzar()

    def ia(self):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.cambio_direccion_timer > self.cambio_direccion_intervalo:
            self.cambiar_direccion()
            self.cambio_direccion_timer = tiempo_actual
        if self.direccion == 1:
            ia_derecha = True
        else:
            ia_derecha = False
        ia_izquierda = not ia_derecha
    
    