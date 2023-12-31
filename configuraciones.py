import pygame
pygame.mixer.init()
# Constantes
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
GREY = (220, 220, 220)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FPS = 60  # Para desacelerar la pantalla

#GIRA IMAGENES 
def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []

    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))


    return lista_girada





#MODIFICA TAMAÑO SPRITE
def reescalar_imagenes(diccionario_animaciones, tamaño):
    for clave in diccionario_animaciones:
        for i in range(len(diccionario_animaciones[clave])):
            superficie = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = pygame.transform.scale(superficie, tamaño)



#Imagenes del Juego
personaje_quieto = [pygame.image.load(r"Imagenes\Megaman\Quieto\0.png")]

personaje_derecha = [pygame.image.load(r"Imagenes\Megaman\Moviendose\0.png"),
                     pygame.image.load(r"Imagenes\Megaman\Moviendose\1.png"),
                     pygame.image.load(r"Imagenes\Megaman\Moviendose\2.png"),
                     pygame.image.load(r"Imagenes\Megaman\Moviendose\3.png"),
                     pygame.image.load(r"Imagenes\Megaman\Moviendose\4.png"),
                     pygame.image.load(r"Imagenes\Megaman\Moviendose\5.png"),
                     pygame.image.load(r"Imagenes\Megaman\Moviendose\6.png"),
                     pygame.image.load(r"Imagenes\Megaman\Moviendose\7.png"),
                     pygame.image.load(r"Imagenes\Megaman\Moviendose\8.png"),
                     pygame.image.load(r"Imagenes\Megaman\Moviendose\9.png")]

personaje_dispara = [pygame.image.load(r"Imagen juego2\24.png")]

personaje_izquierda = girar_imagenes(personaje_derecha, True, False)

personaje_salta = [pygame.image.load(r"Imagenes\Megaman\Saltando\0.png")]

personaje_muere = [pygame.image.load(r"Imagenes\Megaman\Muere\0.png")]






enemigo_camina = [pygame.image.load(r"Imagenes\Enemigos\Caminando\0.png"),
                  pygame.image.load(r"Imagenes\Enemigos\Caminando\1.png"),
                  pygame.image.load(r"Imagenes\Enemigos\Caminando\2.png"),
                  pygame.image.load(r"Imagenes\Enemigos\Caminando\3.png"),
                  pygame.image.load(r"Imagenes\Enemigos\Caminando\4.png")]

enemigo_camina_derecha =girar_imagenes(enemigo_camina, True, False)

enemigo_muerto = [pygame.image.load(r"Imagenes\Enemigos\Muerte\0.png"),
                     pygame.image.load(r"Imagenes\Enemigos\Muerte\0.png"),
                     pygame.image.load(r"Imagenes\Enemigos\Muerte\0.png"),
                     pygame.image.load(r"Imagenes\Enemigos\Muerte\0.png")]


###SONIDOS###
sonido_disparo = pygame.mixer.Sound("Audio/Sonidos/0001 [1].wav")
sonido_disparo_enemigo = pygame.mixer.Sound("Audio/Sonidos/0002 [1].wav")


###MUSICA###
pygame.mixer.music.load("Audio/Musica/30. Dr. Wily 3.mp3")

