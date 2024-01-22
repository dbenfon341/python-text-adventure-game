# Lista de objetos para utilizar en la aventura
# Es una versión prematura probando clases en Python
# No se como va a salir el experimento, pero se intenta.


class Espada:
    def __init__(self, nombre, ataque, durabilidad, descripcion):
        self.nombre = nombre
        self.ataque = ataque
        self.durabilidad = durabilidad
        self.descripcion = descripcion

class Daga:
    def __init__(self, nombre, ataque, durabilidad, descripcion):
        self.nombre = nombre
        self.ataque = ataque
        self.durabilidad = durabilidad
        self.descripcion = descripcion

class Armadura:
    def __init__(self, nombre, defensa, descripcion):
        self.nombre = nombre
        self.defensa = defensa
        self.descripcion = descripcion

class Consumible:
    def __init__(self, nombre, recuperacion, descripcion):
        self.nombre = nombre
        self.recuperacion = recuperacion
        self.descripcion = descripcion


# Diferentes tipos de objetos:
######################################
# Armas:
# Espadas:
espada_normal = Espada("Espada Normal", 10, 100, "Una espada común.")
espada_fuego = Espada("Espada de fuego", 20, 100, "Una espada con el poder elemental del fuego.")
espada_hielo = Espada("Espada de hielo", 20, 100, "Una espada con el poder elemental del hielo.")
espada_legendaria = Espada("Espada legendaria", 50, 100, "Esta espada brilla con una luz característica. Parece ser muy poderosa.")
espada_veneno = Espada("Espada venenosa", 20, 100, "Una espada cubierta con veneno.")

# Dagas:
daga_normal = Daga("Daga Normal", 10, 100, "Una daga común.")
daga_fuego = Daga("Daga de fuego", 20, 100, "Una daga con el poder elemental del fuego.")
daga_hielo = Daga("Daga de hielo", 20, 100, "Una daga con el poder elemental del hielo.")
daga_legendaria = Daga("Daga legendaria", 50, 100, "Esta daga brilla con una luz característica. Parece ser muy poderosa.")
daga_veneno = Daga("Daga venenosa", 20, 100, "Una daga cubierta con veneno.")

######################################
# Armaduras:
armadura_tela = Armadura("Armadura de tela", 5, "Armadura ligera creada con tela.")
armadura_piel = Armadura("Armadura de piel", 10, "Una armadura hecha de piel. Es muy resistente.")
armadura_malla = Armadura("Armadura de malla", 20, "Armadura de mallas.")
armadura_placas = Armadura("Armadura de placas", 50, "Una armadura de placas. Es extremadamente resistente.")

# Consumibles:
pan = Consumible("Pan", 10, "Pan duro que restaura energía.")
pocion = Consumible("Poción", 20, "Una poción que restaura la salud.")
superpocion = Consumible("Super poción", 50, "Una poción que restaura la mitad de la salud.")
elixir = Consumible("Elixir", 100, "Este brebaje restaura la salud por completo.")