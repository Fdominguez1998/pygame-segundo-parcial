import pygame
import sys
from class_personaje import *
from configuraciones import *
from pygame.locals import *
from modo import *
from class_enemigo import *
from class_disparo import *
from class_nivel import *
from nivel_uno import *
from nivel_dos import *
from nivel_tres import *
from base_de_datos import *


# Inicializar Pygame
pygame.init()
pygame.mixer.init()


##################INGRESE NOMBRE#######################
def ingresar_nombre():
    input_box = pygame.Rect(500, 400, 200, 50)
    color_inactive = pygame.Color(WHITE)
    color_active = pygame.Color(GREEN)
    color = color_inactive
    active = False
    text = ''
    font = pygame.font.Font(None, 50)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == KEYDOWN:
                if active:
                    if event.key == K_RETURN:
                        return text
                    elif event.key == K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        pantalla.fill((30, 30, 30))
        width = 300
        input_box.w = width
        pygame.draw.rect(pantalla, color, input_box, 2)
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        pantalla.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.display.flip()
        pygame.time.delay(30)

################################################################


def mostrar_tabla_puntuaciones():
    pantalla.fill((30, 30, 30))

    font_tabla = pygame.font.Font(None, 36)
    texto_titulo = font_tabla.render("Tabla de Puntuaciones", 1, WHITE)
    rect_titulo = texto_titulo.get_rect(center=(pantalla.get_width() // 2, 50))
    pantalla.blit(texto_titulo, rect_titulo.topleft)

    puntajes = obtener_puntajes()

    # Mostrar los puntajes en la pantalla
    y = 150
    for i, (nombre, puntaje) in enumerate(puntajes, start=1):
        texto_puntaje = font_tabla.render(f"{i}. {nombre}: {puntaje}", 1, WHITE)
        rect_puntaje = texto_puntaje.get_rect(topleft=(100, y))
        pantalla.blit(texto_puntaje, rect_puntaje.topleft)
        y += 50

    pygame.display.flip()



#######################################################################

# Creo la ventana con el tamaño por defecto del monitor activo
pantalla = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h - 60))
pygame.display.set_caption('Pantalla Principal')
reloj = pygame.time.Clock()
reloj.tick(FPS)

# Seteo la fuente de los botones
font = pygame.font.Font(None, 50)

text_init = font.render('Iniciar Juego', True, WHITE)
text_quit = font.render('Salir del Juego', True, WHITE)
text_conf = font.render('Configuracion', True, WHITE)

text_init_rect = text_init.get_rect(center=(500, 400))
text_quit_rect = text_init.get_rect(center=(500, 600))
text_conf_rect = text_init.get_rect(center=(500, 800))


text_puntuaciones = font.render('Tabla de Puntuaciones', True, WHITE)
text_puntuaciones_rect = text_puntuaciones.get_rect(center=(1700, 700))

# Loop principal para el menu
menu_mostrar = True
mostrar_juego = False
corriendo = True


nombre_jugador = None  # Almacenar el nombre del jugador


# Inicializar la base de datos
inicializar_base_de_datos()

nivel_actual = nivel_uno(pantalla)
puntaje_acumulado = 0  # Inicializar el puntaje acumulado

while corriendo:
    reloj.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_mostrar = False
            mostrar_juego = False
            running = False
            sys.exit()

    if menu_mostrar:
        
        fondo_menu = pygame.Surface(pantalla.get_size())
        fondo_menu = fondo_menu.convert()
        fondo_menu.fill((0, 0, 0))  # Color negro

        fondo2_menu = pygame.image.load("Imagenes\Fondo\menu.png").convert()
        fondo2_menu = pygame.transform.scale(fondo2_menu, (600,500))

        titulo_menu = pygame.image.load(r"Imagenes\Fondo\titulo2.png").convert()
        titulo_menu = pygame.transform.scale(titulo_menu, (1200,300))

        font = pygame.font.Font(None, 36)
        texto_titulo = font.render("Menú Principal", 1, (0, 0, 0))
        rect_titulo = texto_titulo.get_rect(center=(pantalla.get_width() // 2, 100))

        pantalla.blit(fondo_menu, (0, 0))
        pantalla.blit(titulo_menu, (380, 50))
        pantalla.blit(fondo2_menu, (texto_titulo.get_rect(center=(pantalla.get_width() // 2, 300))))

        #boton para iniciar el juego
        pygame.draw.rect(pantalla, GREEN, text_init_rect)
        pantalla.blit(text_init, text_init_rect)    
        
        # Botón para salir del juego
        pygame.draw.rect(pantalla, RED, text_quit_rect)
        pantalla.blit(text_quit, text_quit_rect)
        
        pygame.draw.rect(pantalla, BLUE, text_conf_rect)
        pantalla.blit(text_conf, text_conf_rect)

        #boton para ver tabla de puntuaciones
        pygame.draw.rect(pantalla, RED, text_puntuaciones_rect)
        pantalla.blit(text_puntuaciones, text_puntuaciones_rect)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
           
            if text_init_rect.collidepoint(mouse_pos):
                nombre_jugador = ingresar_nombre()
                menu_mostrar = False
                mostrar_juego = True
                pygame.mixer.music.play(-1, 0.0)
                #print(f"Nombre del jugador: {nombre_jugador}")  # Puedes imprimir el nombre o almacenarlo según tus necesidades

            elif text_quit_rect.collidepoint(mouse_pos):
                menu_mostrar = False
                mostrar_juego = False
                pygame.quit()
                sys.exit()

             # Verificar si se hace clic en la opción de la tabla de puntuaciones
            elif text_puntuaciones_rect.collidepoint(mouse_pos):
                mostrar_tabla_puntuaciones()  # Implementa esta función más adelante

    elif mostrar_juego:
        
        if mostrar_juego:
            nivel_actual.update(pygame.event.get())


            # Verificar si el personaje ha muerto
            if nivel_actual.personaje.esta_muerto:
                # Actualizar el puntaje acumulado al morir
                puntaje_acumulado += nivel_actual.personaje.puntaje_total
                # Llamar al método morir que mostrará el puntaje acumulado
                nivel_actual.personaje.morir(pantalla, nombre_jugador)

                # Reiniciar el juego o volver al menú principal
                puntaje_acumulado = 0  # Reinicia el puntaje acumulado
                menu_mostrar = True
                mostrar_juego = False

            
            # Verificar si todos los enemigos están muertos
            if nivel_actual.enemigos_muertos():
                # Cambiar al siguiente nivel
                puntaje_acumulado += nivel_actual.personaje.puntaje_total
                if isinstance(nivel_actual, nivel_uno):
                    nivel_actual = nivel_dos(pantalla)
                    
                elif isinstance(nivel_actual, nivel_dos):
                    nivel_actual = nivel_tres(pantalla)

                elif isinstance(nivel_actual, nivel_tres):
                    # Guardar el puntaje al finalizar un nivel
                    guardar_puntaje(nombre_jugador, puntaje_acumulado)
            
                    # Puedes reiniciar el juego o hacer lo que sea necesario después de completar el nivel
                    # Por ejemplo, regresar al menú principal
                    puntaje_acumulado = 0  # Reinicia el puntaje acumulado
                    menu_mostrar = True
                    mostrar_juego = False

    # Obtener los 10 mejores puntajes
    puntajes = obtener_puntajes()

    # Imprimir los puntajes en la consola (puedes modificar esto según tu interfaz)
    print("Puntajes:")
    for i, (nombre, puntaje) in enumerate(puntajes, start=1):
        print(f"{i}. {nombre}: {puntaje}")


        pygame.display.update()

    pygame.display.flip()
    

pygame.quit()
sys.exit()