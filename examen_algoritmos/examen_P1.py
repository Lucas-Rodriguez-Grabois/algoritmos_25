from list_ import List
# usando nombres del archivo super_heroes_data.py
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

def buscar_capitan_america(lista, indice=0):
    if indice >= len(lista):
        print("Capitan America no esta en la lista")
        return
    if lista[indice] == "Captain America":
        print("Capitan America esta en la lista")
        return
    buscar_capitan_america(lista, indice + 1)

def listar_superheroes(lista, indice=0):
    if indice >= len(lista):
        return
    print(lista[indice])
    listar_superheroes(lista, indice + 1)

buscar_capitan_america(superheroes_lista)
listar_superheroes(superheroes_lista)
