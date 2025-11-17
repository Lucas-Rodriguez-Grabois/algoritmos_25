from graph import Graph
from tree import BinaryTree

grafo_star_wars = Graph(is_directed=False)
# Datos de los personajes proporcionados por copilot
personajes_episodios = {
    "Luke Skywalker": 5,
    "Darth Vader": 4,
    "Yoda": 5,
    "Boba Fett": 3,
    "C-3PO": 7,
    "Leia": 5,
    "Rey": 3,
    "Kylo Ren": 3,
    "Chewbacca": 7,
    "Han Solo": 4,
    "R2-D2": 7,
    "BB-8": 3,
}

for personaje, episodios in personajes_episodios.items():
    grafo_star_wars.insert_vertex(personaje)
    pos = grafo_star_wars.search(personaje, 'value')
    if pos is not None:
        grafo_star_wars[pos].other_values = {"episodios": episodios}

#Relaciones de personajes proporcionadas por copilot
relaciones = [
    ("Luke Skywalker", "Darth Vader", 3),
    ("Luke Skywalker", "Yoda", 2),
    ("Luke Skywalker", "Leia", 4),
    ("Luke Skywalker", "Han Solo", 4),
    ("Luke Skywalker", "C-3PO", 5),
    ("Luke Skywalker", "R2-D2", 5),
    ("Luke Skywalker", "Chewbacca", 4),
    ("Darth Vader", "Leia", 2),
    ("Yoda", "C-3PO", 2),
    ("Yoda", "R2-D2", 3),
    ("C-3PO", "R2-D2", 7),
    ("C-3PO", "Leia", 5),
    ("C-3PO", "Han Solo", 4),
    ("C-3PO", "Chewbacca", 5),
    ("C-3PO", "BB-8", 1),
    ("Leia", "Han Solo", 4),
    ("Leia", "Chewbacca", 4),
    ("Leia", "R2-D2", 5),
    ("Leia", "Rey", 1),
    ("Han Solo", "Chewbacca", 5),
    ("Han Solo", "R2-D2", 4),
    ("Han Solo", "Boba Fett", 1),
    ("Han Solo", "Kylo Ren", 1),
    ("Rey", "Kylo Ren", 3),
    ("Rey", "BB-8", 3),
    ("Boba Fett", "Darth Vader", 1),
    ("Chewbacca", "Rey", 2),
]

for origen, destino, peso in relaciones:
    grafo_star_wars.insert_edge(origen, destino, peso)
# ////////////////////////////////////////////////////////////////////
print("1-Árbol de expansión mínimo (contiene C-3PO, Yoda y Leia)")

mst_result = grafo_star_wars.kruskal("C-3PO")
print(f"Árbol de expansión mínimo desde C-3PO:")
print(f"{mst_result}")

if "Yoda" in mst_result and "Leia" in mst_result:
    print(f"El árbol contiene a C-3PO, Yoda y Leia")
print(" ")
# ////////////////////////////////////////////////////////////////////
print("2-Número máximo de episodios compartidos entre dos personajes")

max_episodios = 0
pares_max = []

for vertice in grafo_star_wars:
    personaje1 = vertice.value
    for arista in vertice.edges:
        personaje2 = arista.value
        episodios_compartidos = arista.weight
        
        if episodios_compartidos > max_episodios:
            max_episodios = episodios_compartidos
            pares_max = [(personaje1, personaje2)]
        elif episodios_compartidos == max_episodios:
            
            if (personaje2, personaje1) not in pares_max:
                pares_max.append((personaje1, personaje2))

print(f"Número máximo de episodios compartidos: {max_episodios}")
print(f"Pares de personajes que coinciden con este número:")
for par in pares_max:
    print(f"{par[0]}<->{par[1]}")

print(" ")
# ////////////////////////////////////////////////////////////////////
print("3-Cargando personajes específicos")

personajes_requeridos = [
    "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", 
    "C-3PO", "Leia", "Rey", "Kylo Ren", "Chewbacca", 
    "Han Solo", "R2-D2", "BB-8"
]

print("Personajes cargados:")
for personaje in personajes_requeridos:
    pos = grafo_star_wars.search(personaje, 'value')
    if pos is not None:
        info = grafo_star_wars[pos]
        if info.other_values is not None:
            print(f"{info.value}-{info.other_values['episodios']} episodios")
        else:
            print(f"{info.value}-Sin datos de episodios")
print(" ")
# ////////////////////////////////////////////////////////////////////
print("4-Camino más corto de C-3PO a R2-D2")

camino_c3po_r2d2 = grafo_star_wars.dijkstra("C-3PO")

while camino_c3po_r2d2.size() > 0:
    nodo = camino_c3po_r2d2.pop()
    if nodo[0] == "R2-D2":
        print(f"Destino: {nodo[0]}")
        print(f"Costo total: {nodo[1]} episodios")
        print(f"Viene desde: {nodo[2]}")
        break

camino_completo = grafo_star_wars.dijkstra("C-3PO")
path_to_r2d2 = []

temp_list = []
while camino_completo.size() > 0:
    temp_list.append(camino_completo.pop())

for nodo in temp_list:
    if nodo[0] == "R2-D2":
        current = nodo
        path_to_r2d2.append(current[0])
        
        
        while current[2] is not None:
            for n in temp_list:
                if n[0] == current[2]:
                    current = n
                    path_to_r2d2.append(current[0])
                    break
        break

path_to_r2d2.reverse()
print(f"Camino: {' -> '.join(path_to_r2d2)}")
print(" ")
# ////////////////////////////////////////////////////////////////////
print("5-Camino más corto de Yoda a Darth Vader")

camino_yoda_vader = grafo_star_wars.dijkstra("Yoda")

temp_list_yoda = []
while camino_yoda_vader.size() > 0:
    temp_list_yoda.append(camino_yoda_vader.pop())

# Reconstruir camino a Darth Vader
path_to_vader = []
for nodo in temp_list_yoda:
    if nodo[0] == "Darth Vader":
        current = nodo
        path_to_vader.append(current[0])
        print(f" Destino: {nodo[0]}")
        print(f"Costo total: {nodo[1]} episodios")
        
        while current[2] is not None:
            for n in temp_list_yoda:
                if n[0] == current[2]:
                    current = n
                    path_to_vader.append(current[0])
                    break
        break

path_to_vader.reverse()
print(f"Camino: {' -> '.join(path_to_vader)}")
print(" ")
# ////////////////////////////////////////////////////////////////////
print("6-Personajes que aparecen en los 9 episodios")# Como ningún personaje aparece en los 9 episodios, se buscarán los que aparecen en 7 o más episodios 
personajes_9_episodios = []

for vertice in grafo_star_wars:
    if vertice.other_values is not None and vertice.other_values['episodios'] >= 7:  
        personajes_9_episodios.append(vertice.value)

if personajes_9_episodios:
    print(f"Personajes con mayor presencia (7+ episodios):")
    for personaje in personajes_9_episodios:
        pos = grafo_star_wars.search(personaje, 'value')
        if pos is not None and grafo_star_wars[pos].other_values is not None:
            episodios = grafo_star_wars[pos].other_values['episodios']
            print(f"{personaje}: {episodios} episodios")
else:
    print("No hay personajes que aparezcan en los 9 episodios")
