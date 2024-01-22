# Intento de "Text Adventure Game"
# Por ahora bastante simplificado.
# 29/12/2023

from os import system, name
import random

def clear():
    if name == 'nt':
        _ = system('cls')

# Constantes sobre el nombre del juego y la versión
NOMBRE_JUEGO = 'Entre sombras y joyas'
VER_JUEGO = '1.0'


# Mapa cueva
# -----------------------------------------------
# |       |       |                             |
# |       |       |                             |
# |       |       |                             |
# |       |       |                             |
# |               |                             |
# |-------|       |                             |
# |-------|       |------------|        |-------|
# |                                             |
# -----------------------------------------------


# Tamaño del mapa (10x10)
# Constantes para la creación del mapa y la lógica de los muros y posición del jugador
MAP_WIDTH = 10
MAP_HEIGHT = 10
MUROS = '╔', '═', '╗', '╝', '╚', '╦', '╠', '║'
JUGADOR_X = 1
JUGADOR_Y = 1

descripciones_entorno = {
    (1, 1): "Estas en una especie de pasillo. Tu única opción es andar hacia el sur. Parece que hay algo en la pared de la derecha.",
    (1, 2): "Estás en un pasillo oscuro. Tienes dos paredes de piedra a tu derecha y izquierda. Puedes avanzar hacia el norte o hacia el sur.",
    (1, 3): "Estás en un pasillo oscuro. Tienes dos paredes de piedra a tu derecha y izquierda. Puedes avanzar hacia el norte o hacia el sur.",
}

mapa = [
    ["╔", "═", "╦", "═", "╦", "═", "═", "═", "═", "╗"],
    ["║", " ", "║", " ", "║", " ", " ", " ", " ", "║"],
    ["║", " ", "║", " ", "║", " ", " ", " ", " ", "║"],
    ["║", " ", "║", " ", "║", " ", " ", " ", " ", "║"],
    ["║", " ", " ", " ", "║", " ", " ", " ", " ", "║"],
    ["║", " ", " ", " ", "║", " ", " ", " ", " ", "║"],
    ["╠", "═", "╗", " ", "║", " ", " ", " ", " ", "║"],
    ["╠", "═", "╝", " ", "╚", "═", "═", " ", "═", "╣"],
    ["║", " ", " ", " ", " ", " ", " ", " ", " ", "║"],
    ["╚", "═", "═", "═", "═", "═", "═", "═", "═", "╝"]
]

# Constantes del spawn de enemigos y otros:

spawn_enemigo = 'E'
spawn_boss = 'B'
cofre = 'C'

#Definimos el menu y las opciones posibles

def mostrar_menu():
    print(f"Bienvenido a {NOMBRE_JUEGO} {VER_JUEGO}")
    print("1. Jugar")
    print("2. Como jugar")
    print("3. Sobre el juego")
    print("4. Salir")


def escojer_opcion(opcion):
    if opcion == 1:
        clear()
        print("Comenzando partida...")
    elif opcion == 2:
        clear()
        print("Mostrando opciones...")
    elif opcion == 3:
        clear()
        print("La narrativa se desarrolla en el imaginario mundo de Theia.")
        print("Rofuem, un reconocido ladrón en la bulliciosa ciudad de Az'Ka-hem, cae en una cueva al norte de la ciudad por una pequeña grieta")
        print("que no vio mientras escapaba después de apoderarse de una preciada joya roja del palacio real.")
        print("Pronto descubrirá que haber sido capturado habría sido una mejor suerte que terminar en ese lugar...")
    elif opcion == 4:
        clear()
        print("Saliendo del juego.")
    else:
        clear()
        print("Opción no válida. Por favor, elige una opción del menú.")

# Funcion para imprimir el mapa

def print_map():
    for y, row in enumerate(mapa):
        for x, col in enumerate(row):
            if x == JUGADOR_X and y == JUGADOR_Y:
                print('P', end=' ')
            else:
                print(col, end=' ')
        print()
    current_description = descripciones_entorno.get((JUGADOR_X, JUGADOR_Y))
    if current_description:
        print(current_description)

# Con esta funcion empezamos el juego. Obtenemos las variables definidas fuera de la funcion y le decimos que pueden ser
# modificadas dentro de ella. Imprime el mapa y permite moverte por el tablero.

def empezar_juego():
    global JUGADOR_X, JUGADOR_Y

    while True:
        clear()
        print_map()
        direction = input("Introduce la dirección (w/a/s/d para arriba/izquierda/abajo/derecha, q para salir): ").lower()
        next_x, next_y = JUGADOR_X, JUGADOR_Y
        if direction == 'w':
            next_y -= 1
        elif direction == 'a':
            next_x -= 1
        elif direction == 's':
            next_y += 1
        elif direction == 'd':
            next_x += 1
        elif direction == 'q':
            break
        else:
            print("Movimiento inválido")
            continue
    
        if 0 <= next_y < len(mapa) and 0 <= next_x < len(mapa[0]) and mapa[next_y][next_x] not in MUROS:
            JUGADOR_X, JUGADOR_Y = next_x, next_y
        else:
            print("No puedes moverte ahí.")

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Elige una opcion: "))
            escojer_opcion(opcion)
            if opcion == 4:
                break
            elif opcion == 1:
                empezar_juego()
        except ValueError:
            clear()
            print("Por favor, ingresa una opción válida.")


if __name__ == '__main__':
    main()