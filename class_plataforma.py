import pygame


class Plataforma():
    def __init__(self,es_visible, tamaño, posicion, path,tipo):
        self.es_visible = es_visible
        self.tamaño = tamaño
        self.posicion = posicion
        self.path = path
        self.tipo = tipo
        self.superficie = None
        self.rectangulo = None

        
        if es_visible:
            self.superficie = pygame.image.load(path)
            self.superficie = pygame.transform.scale(self.superficie, tamaño)
        else:
            self.superficie = pygame.Surface(tamaño)

        self.rectangulo = self.superficie.get_rect()

        x,y = posicion

        self.rectangulo.x = x
        self.rectangulo.y = y

    
    # def teletransportar(self, personaje):
    #     # print(self.rectangulo)
    #     # print(personaje.rectangulo)
    #     if self.tipo == "PORTAL":
    #         return personaje.rectangulo.colliderect(self.rectangulo)
        
    #     return False