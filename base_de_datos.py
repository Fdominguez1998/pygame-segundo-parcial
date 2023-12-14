
import sqlite3

def inicializar_base_de_datos():
    conexion = sqlite3.connect('puntajes.db')
    cursor = conexion.cursor()

    # Crea la tabla de puntajes si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS puntajes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            puntaje INTEGER
        )
    ''')

    # Guarda los cambios
    conexion.commit()

    # Cierra la conexión
    conexion.close()


def guardar_puntaje(nombre, puntaje):
    conexion = sqlite3.connect('puntajes.db')
    cursor = conexion.cursor()

    # Inserta el puntaje en la tabla
    cursor.execute('INSERT INTO puntajes (nombre, puntaje) VALUES (?, ?)', (nombre, puntaje))

    # Guarda los cambios
    conexion.commit()

    # Cierra la conexión
    conexion.close()


def obtener_puntajes():
    conexion = sqlite3.connect('puntajes.db')
    cursor = conexion.cursor()

    # Selecciona todos los puntajes ordenados por puntaje descendente
    cursor.execute('SELECT nombre, puntaje FROM puntajes ORDER BY puntaje DESC')

    # Recupera los resultados
    puntajes = cursor.fetchall()

    # Cierra la conexión
    conexion.close()

    return puntajes


