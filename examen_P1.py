from list_ import List

# Cargar los nombres de superheroes
superheroes_lista = List()
for hero in [
    "Hulk",
    "Black Widow",
    "Iron Man",
    "Storm",
    "Scarlet Witch",
    "Adam Warlock",
    "Angel",
    "Ant Man",
    "Beast",
    "Beta Ray Bill",
    "Black Bolt",
    "Black Panther",
    "Cable",
    "Captain America",
    "Captain Britain"
]:
    superheroes_lista.append(hero)

# Funcion recursiva para buscar a Capitan America
def buscar_capitan_america(lista, indice=0):
    if indice >= len(lista):
        print("Capitan America no esta en la lista")
        return
    if lista[indice] == "Captain America":
        print("Capitan America esta en la lista")
        return
    buscar_capitan_america(lista, indice + 1)

# Funcion recursiva para listar superheroes
def listar_superheroes(lista, indice=0):
    if indice >= len(lista):
        return
    print(lista[indice])
    listar_superheroes(lista, indice + 1)

# Probar las funciones
buscar_capitan_america(superheroes_lista)
listar_superheroes(superheroes_lista)