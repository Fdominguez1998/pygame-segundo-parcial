import pygame

def crear_plataforma(es_visible, tamaño, posicion, path=""): #devuelve dicionario
    plataforma = {}
    if es_visible:
        plataforma["superficie"] = pygame.image.load(path)
        plataforma["superficie"] = pygame.transform.scale(plataforma["superficie"], tamaño)
    else:
        plataforma["superficie"] = pygame.Surface(tamaño)

    plataforma["rectangulo"] = plataforma["superficie"].get_rect()

    x,y = posicion

    plataforma["rectangulo"].x = x
    plataforma["rectangulo"].y = y

    return plataforma