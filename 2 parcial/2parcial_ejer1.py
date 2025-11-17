from tree import BinaryTree

# Datos de Pokémon proporcionada por copilot
pokemones_por_tipo = {
    "Normal": [
        {"nombre": "Snorlax", "numero": 143, "tipo": ["Normal"], "debilidades": ["Lucha"], "megaevolucion": False, "gigamax": True},
        {"nombre": "Eevee", "numero": 133, "tipo": ["Normal"], "debilidades": ["Lucha"], "megaevolucion": False, "gigamax": True},
        {"nombre": "Wooloo", "numero": 831, "tipo": ["Normal"], "debilidades": ["Lucha"], "megaevolucion": False, "gigamax": False}
    ],
    "Fuego": [
        {"nombre": "Charmander", "numero": 4, "tipo": ["Fuego"], "debilidades": ["Agua", "Tierra", "Roca"], "megaevolucion": False, "gigamax": False},
        {"nombre": "Arcanine", "numero": 59, "tipo": ["Fuego"], "debilidades": ["Agua", "Tierra", "Roca"], "megaevolucion": False, "gigamax": False},
        {"nombre": "Scorbunny", "numero": 813, "tipo": ["Fuego"], "debilidades": ["Agua", "Tierra", "Roca"], "megaevolucion": False, "gigamax": False}
    ],
    "Agua": [
        {"nombre": "Squirtle", "numero": 7, "tipo": ["Agua"], "debilidades": ["Eléctrico", "Planta"], "megaevolucion": False, "gigamax": True},
        {"nombre": "Lapras", "numero": 131, "tipo": ["Agua", "Hielo"], "debilidades": ["Eléctrico", "Planta", "Lucha", "Roca"], "megaevolucion": False, "gigamax": True},
        {"nombre": "Sobble", "numero": 816, "tipo": ["Agua"], "debilidades": ["Eléctrico", "Planta"], "megaevolucion": False, "gigamax": False}
    ],
    "Planta": [
        {"nombre": "Bulbasaur", "numero": 1, "tipo": ["Planta", "Veneno"], "debilidades": ["Fuego", "Psíquico", "Volador", "Hielo"], "megaevolucion": True, "gigamax": True},
        {"nombre": "Chikorita", "numero": 152, "tipo": ["Planta"], "debilidades": ["Fuego", "Hielo", "Veneno", "Volador", "Bicho"], "megaevolucion": False, "gigamax": False},
        {"nombre": "Sprigatito", "numero": 906, "tipo": ["Planta"], "debilidades": ["Fuego", "Hielo", "Veneno", "Volador", "Bicho"], "megaevolucion": False, "gigamax": False}
    ],
    "Eléctrico": [
        {"nombre": "Pikachu", "numero": 25, "tipo": ["Eléctrico"], "debilidades": ["Tierra"], "megaevolucion": False, "gigamax": True},
        {"nombre": "Electabuzz", "numero": 125, "tipo": ["Eléctrico"], "debilidades": ["Tierra"], "megaevolucion": False, "gigamax": False},
        {"nombre": "Pawmot", "numero": 923, "tipo": ["Eléctrico", "Lucha"], "debilidades": ["Tierra", "Psíquico", "Hada"], "megaevolucion": False, "gigamax": False}
    ],
    "Hielo": [
        {"nombre": "Articuno", "numero": 144, "tipo": ["Hielo", "Volador"], "debilidades": ["Fuego", "Eléctrico", "Acero", "Roca"], "megaevolucion": False, "gigamax": False},
        {"nombre": "Glaceon", "numero": 471, "tipo": ["Hielo"], "debilidades": ["Fuego", "Lucha", "Roca", "Acero"], "megaevolucion": False, "gigamax": False},
        {"nombre": "Cetitan", "numero": 975, "tipo": ["Hielo"], "debilidades": ["Fuego", "Lucha", "Roca", "Acero"], "megaevolucion": False, "gigamax": False}
    ],
    "Lucha": [
        {"nombre": "Machop", "numero": 66, "tipo": ["Lucha"], "debilidades": ["Volador", "Psíquico", "Hada"], "megaevolucion": False, "gigamax": False},
        {"nombre": "Heracross", "numero": 214, "tipo": ["Bicho", "Lucha"], "debilidades": ["Volador", "Psíquico", "Hada", "Fuego"], "megaevolucion": True, "gigamax": False},
        {"nombre": "Flamigo", "numero": 973, "tipo": ["Volador", "Lucha"], "debilidades": ["Eléctrico", "Psíquico", "Hielo", "Hada"], "megaevolucion": False, "gigamax": False}
    ],
    "Veneno": [
        {"nombre": "Ekans", "numero": 23, "tipo": ["Veneno"], "debilidades": ["Tierra", "Psíquico"], "megaevolucion": False, "gigamax": False},
        {"nombre": "Crobat", "numero": 169, "tipo": ["Veneno", "Volador"], "debilidades": ["Eléctrico", "Psíquico", "Hielo", "Roca"], "megaevolucion": False, "gigamax": False},
        {"nombre": "Grafaiai", "numero": 945, "tipo": ["Veneno", "Normal"], "debilidades": ["Tierra", "Psíquico"], "megaevolucion": False, "gigamax": False}
    ],
    "Tierra": [
        {"nombre": "Sandshrew", "numero": 27, "tipo": ["Tierra"], "debilidades": ["Agua", "Planta", "Hielo"], "megaevolucion": False, "gigamax": False},
        {"nombre": "Phanpy", "numero": 231, "tipo": ["Tierra"], "debilidades": ["Agua", "Planta", "Hielo"], "megaevolucion": False, "gigamax": False},
        {"nombre": "Clodsire", "numero": 980, "tipo": ["Veneno", "Tierra"], "debilidades": ["Agua", "Psíquico", "Hielo", "Tierra"], "megaevolucion": False, "gigamax": False}
    ],
    "Volador": [
        {"nombre": "Pidgeot", "numero": 18, "tipo": ["Normal", "Volador"], "debilidades": ["Eléctrico", "Hielo", "Roca"], "megaevolucion": True, "gigamax": False},
        {"nombre": "Noctowl", "numero": 164, "tipo": ["Normal", "Volador"], "debilidades": ["Eléctrico", "Hielo", "Roca"], "megaevolucion": False, "gigamax": False},
        {"nombre": "Kilowattrel", "numero": 941, "tipo": ["Eléctrico", "Volador"], "debilidades": ["Hielo", "Roca"], "megaevolucion": False, "gigamax": False}
    ],
    "Psíquico": [
        {"nombre": "Abra", "numero": 63, "tipo": ["Psíquico"], "debilidades": ["Bicho", "Fantasma", "Siniestro"], "megaevolucion": False, "gigamax": False},
        {"nombre": "Espeon", "numero": 196, "tipo": ["Psíquico"], "debilidades": ["Bicho", "Fantasma", "Siniestro"], "megaevolucion": False, "gigamax": False},
        {"nombre": "Farigiraf", "numero": 981, "tipo": ["Normal", "Psíquico"], "debilidades": ["Bicho", "Siniestro"], "megaevolucion": False, "gigamax": False}
    ],
    "Bicho": [
        {"nombre": "Caterpie", "numero": 10, "tipo": ["Bicho"], "debilidades": ["Fuego", "Volador", "Roca"], "megaevolucion": False, "gigamax": False},
        {"nombre": "Scyther", "numero": 123, "tipo": ["Bicho", "Volador"], "debilidades": ["Fuego", "Eléctrico", "Hielo", "Volador", "Roca"], "megaevolucion": False, "gigamax": False},
        {"nombre": "Lokix", "numero": 920, "tipo": ["Bicho", "Siniestro"], "debilidades": ["Fuego", "Volador", "Roca", "Hada"], "megaevolucion": False, "gigamax": False}
    ],
    "Roca": [
        {"nombre": "Geodude", "numero": 74, "tipo": ["Roca", "Tierra"], "debilidades": ["Agua", "Planta", "Lucha", "Tierra", "Acero"], "megaevolucion": False, "gigamax": False},
        {"nombre": "Larvitar", "numero": 246, "tipo": ["Roca", "Tierra"], "debilidades": ["Agua", "Planta", "Lucha", "Tierra", "Acero", "Hielo"], "megaevolucion": True, "gigamax": False},
        {"nombre": "Nacli", "numero": 932, "tipo": ["Roca"], "debilidades": ["Agua", "Planta", "Lucha", "Tierra", "Acero"], "megaevolucion": False, "gigamax": False}
    ],
    "Fantasma": [
        {"nombre": "Gastly", "numero": 92, "tipo": ["Fantasma", "Veneno"], "debilidades": ["Tierra", "Psíquico", "Fantasma", "Siniestro"], "megaevolucion": False, "gigamax": True},
        {"nombre": "Misdreavus", "numero": 200, "tipo": ["Fantasma"], "debilidades": ["Fantasma", "Siniestro"], "megaevolucion": False, "gigamax": False},
        {"nombre": "Greavard", "numero": 972, "tipo": ["Fantasma"], "debilidades": ["Fantasma", "Siniestro"], "megaevolucion": False, "gigamax": False}
    ],
    "Dragón": [
        {"nombre": "Dratini", "numero": 147, "tipo": ["Dragón"], "debilidades": ["Hielo", "Dragón", "Hada"], "megaevolucion": False, "gigamax": False},
        {"nombre": "Salamence", "numero": 373, "tipo": ["Dragón", "Volador"], "debilidades": ["Hielo", "Dragón", "Hada", "Roca"], "megaevolucion": True, "gigamax": False},
        {"nombre": "Baxcalibur", "numero": 998, "tipo": ["Dragón", "Hielo"], "debilidades": ["Lucha", "Roca", "Acero", "Dragón", "Hada"], "megaevolucion": False, "gigamax": False}
    ],
    "Siniestro": [
        {"nombre": "Houndoom", "numero": 229, "tipo": ["Siniestro", "Fuego"], "debilidades": ["Agua", "Lucha", "Tierra", "Roca"], "megaevolucion": True, "gigamax": False},
        {"nombre": "Absol", "numero": 359, "tipo": ["Siniestro"], "debilidades": ["Lucha", "Bicho", "Hada"], "megaevolucion": True, "gigamax": False},
        {"nombre": "Chien-Pao", "numero": 1002, "tipo": ["Siniestro", "Hielo"], "debilidades": ["Lucha", "Bicho", "Roca", "Acero", "Fuego", "Hada"], "megaevolucion": False, "gigamax": False}
    ],
    "Acero": [
        {"nombre": "Steelix", "numero": 208, "tipo": ["Acero", "Tierra"], "debilidades": ["Fuego", "Agua", "Lucha", "Tierra"], "megaevolucion": True, "gigamax": False},
        {"nombre": "Metagross", "numero": 376, "tipo": ["Acero", "Psíquico"], "debilidades": ["Fuego", "Tierra", "Fantasma", "Siniestro"], "megaevolucion": True, "gigamax": False},
        {"nombre": "Kingambit", "numero": 983, "tipo": ["Acero", "Siniestro"], "debilidades": ["Fuego", "Lucha", "Tierra"], "megaevolucion": False, "gigamax": False}
    ],
    "Hada": [
        {"nombre": "Clefairy", "numero": 35, "tipo": ["Hada"], "debilidades": ["Veneno", "Acero"], "megaevolucion": False, "gigamax": False},
        {"nombre": "Sylveon", "numero": 700, "tipo": ["Hada"], "debilidades": ["Veneno", "Acero"], "megaevolucion": False, "gigamax": False},
        {"nombre": "Tinkaton", "numero": 957, "tipo": ["Hada", "Acero"], "debilidades": ["Fuego", "Tierra"], "megaevolucion": False, "gigamax": False}
    ]
}

# Los tres árboles
arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

# Cargo los pokemones

for tipo_categoria, pokemons in pokemones_por_tipo.items():
    for pokemon in pokemons:
        arbol_nombre.insert(pokemon["nombre"], pokemon)
        arbol_numero.insert(pokemon["numero"], pokemon)
        for tipo in pokemon["tipo"]:
            arbol_tipo.insert(tipo, pokemon)
# ////////////////////////////////////////////////////////////////////
print("1. BÚSQUEDA DE POKÉMON POR NÚMERO Y NOMBRE")#Mas adelante se usara el arbol tipo

numero_buscar = 25
pos = arbol_numero.search(numero_buscar)
if pos:
    print(f"  Pokémon #{numero_buscar}:")
    print(f"  Nombre: {pos.other_values['nombre']}")
    print(f"  Tipo(s): {', '.join(pos.other_values['tipo'])}")
    print(f"  Debilidades: {', '.join(pos.other_values['debilidades'])}")
    print(f"  Megaevolución: {'Sí' if pos.other_values['megaevolucion'] else 'No'}")
    print(f"  Gigamax: {'Sí' if pos.other_values['gigamax'] else 'No'}")

print("")
nombre_buscar = "Bulbasaur"
pos = arbol_nombre.search(nombre_buscar)
if pos:
    print(f"  Pokémon '{nombre_buscar}':")
    print(f"  Número: {pos.other_values['numero']}")
    print(f"  Tipo(s): {', '.join(pos.other_values['tipo'])}")
    print(f"  Debilidades: {', '.join(pos.other_values['debilidades'])}")
    print(f"  Megaevolución: {'Sí' if pos.other_values['megaevolucion'] else 'No'}")
    print(f"  Gigamax: {'Sí' if pos.other_values['gigamax'] else 'No'}")
print(" ")    
# ////////////////////////////////////////////////////////////////////
print("2. BÚSQUEDA POR PROXIMIDAD DE NOMBRE")
print("Pokémon que comienzan con 'Bul':")
arbol_nombre.proximity_search("Bul")

print("Pokémon que comienzan con 'Cha':")
arbol_nombre.proximity_search("Cha")
print(" ")
# ////////////////////////////////////////////////////////////////////
print("3. POKÉMON POR TIPO") #Usando el árbol por tipo

def mostrar_pokemon_por_tipo_arbol(tipo_buscar):
    print(f"Buscando Pokémon de tipo '{tipo_buscar}' en el árbol...")
    
    def buscar_en_arbol(root, tipo_buscar, resultados):
        if root is not None:
            buscar_en_arbol(root.left, tipo_buscar, resultados)
            if root.value == tipo_buscar:
                nombre_pokemon = root.other_values['nombre']
                if nombre_pokemon not in resultados:
                    resultados.append(nombre_pokemon)
            buscar_en_arbol(root.right, tipo_buscar, resultados)
    
    resultados = []
    if arbol_tipo.root is not None:
        buscar_en_arbol(arbol_tipo.root, tipo_buscar, resultados)
    
    if resultados:
        print(f"Se encontraron {len(resultados)} Pokémon:")
        for nombre in sorted(resultados):
            print(f"{nombre}")
    else:
        print(f"No se encontraron Pokémon de tipo '{tipo_buscar}'")
    
    return resultados

mostrar_pokemon_por_tipo_arbol("Fantasma")
mostrar_pokemon_por_tipo_arbol("Fuego")
mostrar_pokemon_por_tipo_arbol("Acero")
mostrar_pokemon_por_tipo_arbol("Eléctrico")
print(" ")
# ////////////////////////////////////////////////////////////////////
print("4. LISTADOS ORDENADOS ASCENDENTEMENTE")
print("Por NÚMERO")
arbol_numero.in_order()

print("Por NOMBRE")
arbol_nombre.in_order()

print("Por NIVEL")
def listado_por_nivel_nombre():
    from queue_ import Queue
    tree_queue = Queue()
    if arbol_nombre.root is not None:
        tree_queue.arrive(arbol_nombre.root)
        while tree_queue.size() > 0:
            node = tree_queue.attention()
            print(f"Nivel {node.hight}: {node.value}")
            if node.left is not None:
                tree_queue.arrive(node.left)
            if node.right is not None:
                tree_queue.arrive(node.right)

listado_por_nivel_nombre()
print(" ")
# ////////////////////////////////////////////////////////////////////
print("5. POKÉMON DÉBILES FRENTE A TIPOS ESPECÍFICOS")
debil_a_electrico = []
debil_a_roca = []

for tipo_categoria, pokemons in pokemones_por_tipo.items():
    for pokemon in pokemons:
        if "Eléctrico" in pokemon["debilidades"]:
            debil_a_electrico.append(pokemon["nombre"])
        if "Roca" in pokemon["debilidades"]:
            debil_a_roca.append(pokemon["nombre"])

print(f"Pokémon débiles ante Jolteon (Eléctrico): {len(debil_a_electrico)}")
for nombre in sorted(debil_a_electrico):
    print(f"{nombre}")

print(f"Pokémon débiles ante Lycanroc y Tyrantrum (Roca): {len(debil_a_roca)}")
for nombre in sorted(debil_a_roca):
    print(f" {nombre}")
print(" ")
# ////////////////////////////////////////////////////////////////////
print("6. CANTIDAD DE POKÉMON POR TIPO")
contador_tipos = {}
for tipo_categoria, pokemons in pokemones_por_tipo.items():
    for pokemon in pokemons:
        for tipo in pokemon["tipo"]:
            if tipo not in contador_tipos:
                contador_tipos[tipo] = 0
            contador_tipos[tipo] += 1

print("Tipos de Pokémon y sus cantidades:")
for tipo in sorted(contador_tipos.keys()):
    print(f"  {tipo}: {contador_tipos[tipo]} Pokémon")
print(" ")
# ////////////////////////////////////////////////////////////////////
print("7. POKÉMON CON MEGAEVOLUCIÓN")
def contar_megaevolucion():
    count = 0
    lista_mega = []
    for tipo_categoria, pokemons in pokemones_por_tipo.items():
        for pokemon in pokemons:
            if pokemon["megaevolucion"]:
                count += 1
                lista_mega.append(pokemon["nombre"])
    return count, lista_mega

total_mega, lista_mega = contar_megaevolucion()
print(f"Total de Pokémon con Megaevolución: {total_mega}")
print("Listado:")
for nombre in sorted(lista_mega):
    print(f"{nombre}")
print(" ")
# ////////////////////////////////////////////////////////////////////
print("8. POKÉMON CON FORMA GIGAMAX")
def contar_gigamax():
    count = 0
    lista_gigamax = []
    for tipo_categoria, pokemons in pokemones_por_tipo.items():
        for pokemon in pokemons:
            if pokemon["gigamax"]:
                count += 1
                lista_gigamax.append(pokemon["nombre"])
    return count, lista_gigamax

total_gigamax, lista_gigamax = contar_gigamax()
print(f"Total de Pokémon con forma Gigamax: {total_gigamax}")
print("Listado:")
for nombre in sorted(lista_gigamax):
    print(f"{nombre}")
