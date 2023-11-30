import pygame


class disparo:
    def __init__(self, x, y, direccion):
        self.superficie = pygame.image.load(r"Imagen juego2\25.png")
        self.superficie = pygame.transform.scale(self.superficie, (30,20))
        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.x = x
        self.rectangulo.centery = y
        self.direccion = direccion

    
    def actualizar(self, pantalla):
        if self.direccion == "derecha" or self.direccion == "quieto":
            self.rectangulo.x += 10
        elif self.direccion == "izquierda":
            self.rectangulo.x -= 10

        pantalla.blit(self.superficie, self.rectangulo)
    
    def verificar_colision_enemigo(self, enemigo):
        return self.rectangulo.colliderect(enemigo.rectangulo)

