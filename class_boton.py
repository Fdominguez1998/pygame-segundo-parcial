import pygame

class Boton:
    def __init__(self, texto, x, y, ancho, alto, color_normal, color_resaltado, accion=None):
        self.texto = texto
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.color_normal = color_normal
        self.color_resaltado = color_resaltado
        self.color_actual = self.color_normal
        self.accion = accion

    def actualizar(self, eventos):
        for evento in eventos:
            if evento.type == pygame.MOUSEMOTION:
                if self.rect.collidepoint(evento.pos):
                    self.color_actual = self.color_resaltado
                else:
                    self.color_actual = self.color_normal
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(evento.pos) and self.accion:
                    self.accion()

    def dibujar(self, pantalla, font):
        pygame.draw.rect(pantalla, self.color_actual, self.rect)
        texto = font.render(self.texto, True, (255, 255, 255))
        rect_texto = texto.get_rect(center=self.rect.center)
        pantalla.blit(texto, rect_texto)