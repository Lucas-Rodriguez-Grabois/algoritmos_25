from list_ import List
from queue_ import Queue
from super_heroes_data import superheroes as data

def ordenar_nombre(item):
    return item["name"]

def ordenar_nombre_real(item):
    return str(item["real_name"]) if item["real_name"] is not None else ""

def ordenar_por_first_appearance(item):
    return item["first_appearance"]

heroes = List()
for item in data:
    heroes.append(item)

heroes.add_criterion("name", ordenar_nombre)

# Consigna 1
heroes.sort_by_criterion("name")
heroes.show()

# Consigna 2
def posicion_thething_raccoon(lista):
    index1 = lista.search("The Thing", "name")
    index2 = lista.search("Rocket Raccoon", "name")
    return index1, index2

# Consigna 3
def listar_villanos(lista):
    resultado = []
    for item in lista:
        if item["is_villain"]:
            resultado.append(item["name"])
    return resultado

# Consigna 4
def villanos_antes_1980(lista):
    resultado = Queue()
    for item in lista:
        if item["is_villain"] and item["first_appearance"] < 1980:
            resultado.arrive(item["name"])
    return resultado

# Consigna 5
def heroes_con_letras(lista):
    resultado = []
    for item in lista:
        if not item["is_villain"] and item["name"].startswith(("Bl", "G", "My", "W")):
            resultado.append(item["name"])
    return resultado

# Consigna 6
heroes.add_criterion("real name", ordenar_nombre_real)
heroes.sort_by_criterion("real name")

# Consigna 7
def lista_solo_heroes(lista):
    superheroes = List()
    superheroes.add_criterion("first_appearance", ordenar_por_first_appearance)
    for item in lista:
        if not item["is_villain"]:
            superheroes.append(item)
    superheroes.sort_by_criterion("first_appearance")
    return superheroes

# Consigna 8
def antman_cambiar_nombre_real(lista):
    index = lista.search("Ant Man", "name")
    if index is not None:
        if lista[index]["real_name"] != "Scott Lang":
            lista[index]["real_name"] = "Scott Lang"
            print("Nombre real de Ant Man actualizado a Scott Lang.")
        else:
            print("El nombre real ya es Scott Lang.")
    else:
        print("Ant Man no esta en la lista.")

# Consigna 9
def bio_time_traveling_suit(lista):
    resultado = []
    for item in lista:
        if "time-traveling" in item["short_bio"] or "suit" in item["short_bio"]:
            resultado.append(item["name"])
    return resultado

# Consigna 10
def eliminar_electro_baron(lista):
    for nombre in ["Electro", "Baron Zemo"]:
        index = lista.search(nombre, "name")
        if index is not None:
            print(f"Datos de {nombre} antes de eliminar:")
            print(f"Nombre: {lista[index]['name']}, Alias: {lista[index]['alias']}, Real: {lista[index]['real_name']}")
            lista.delete_value(nombre, "name")
            print(f"{nombre} eliminado.")
        else:
            print(f"{nombre} no esta en la lista.")


heroes.show()
print("Posicion de 'The Thing' y 'Rocket Raccoon':", posicion_thething_raccoon(heroes))
print("Villanos:", listar_villanos(heroes))
print("Villanos de antes de 1980:", villanos_antes_1980(heroes))
print("Heroes que empiezan con Bl, G, My o W:", heroes_con_letras(heroes))
print("Listado de heroes ordenados por aparicion:")
lista_solo_heroes(heroes).show()
antman_cambiar_nombre_real(heroes)
eliminar_electro_baron(heroes)
print("Personajes con time-traveling o suit en bio:", bio_time_traveling_suit(heroes))