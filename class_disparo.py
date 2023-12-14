import pygame


class disparo:
    def __init__(self, x, y, direccion, velocidad, imagen_proyectil):
        self.superficie = pygame.image.load(imagen_proyectil)
        self.superficie = pygame.transform.scale(self.superficie, (30,20))
        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.x = x
        self.rectangulo.centery = y
        self.direccion = direccion
        self.velocidad = velocidad
        

    
    def actualizar(self, pantalla):
        if self.direccion == "derecha" or self.direccion == "quieto":
            self.rectangulo.x += self.velocidad
        elif self.direccion == "izquierda":
            self.rectangulo.x -= self.velocidad

        pantalla.blit(self.superficie, self.rectangulo)
    
    def verificar_colision_enemigo(self, enemigo):
        return self.rectangulo.colliderect(enemigo.rectangulo)
    
    def verificar_colision_personaje(self, personaje):
        return self.rectangulo.colliderect(personaje.rectangulo)

