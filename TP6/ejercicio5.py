from graph import Graph

grafo_red = Graph(is_directed=False)

nodos_red = {
    "Red Hat": "pc",
    "Debian": "pc",
    "Ubuntu": "pc",
    "PC": "pc",
    "Notebook": "notebook",
    "Guarani": "servidor",
    "Mint": "pc",
    "Arch": "pc",
    "Fedora": "pc",
    "Manjaro": "pc",
    "Parrot": "pc",
    "MongoDB": "servidor",
    "Router 1": "router",
    "Router 2": "router",
    "Router 3": "router",
    "Switch 1": "switch",
    "Switch 2": "switch",
    "Impresora": "impresora"
}

for nodo, tipo_nodo in nodos_red.items():
    grafo_red.insert_vertex(nodo)
    pos = grafo_red.search(nodo, 'value')
    if pos is not None:
        grafo_red[pos].other_values = {"tipo": tipo_nodo}

print(f"{len(nodos_red)} nodos insertados")

conexiones = [
    ("Red Hat", "Router 1", 9),
    ("Red Hat", "Switch 1", 15),
    ("Debian", "Switch 1", 17),
    ("Ubuntu", "Switch 1", 13),
    ("PC", "Switch 1", 12),
    ("Notebook", "Switch 1", 29),
    ("Switch 1", "Router 1", 37),
    ("Router 1", "Guarani", 50),
    ("Router 1", "Router 2", 48),
    ("Router 1", "Switch 2", 63),
    ("Router 1", "Impresora", 80),
    ("Router 2", "Mint", 22),
    ("Router 2", "Manjaro", 40),
    ("Router 2", "Parrot", 11),
    ("Router 2", "Switch 2", 56),
    ("Switch 2", "Arch", 9),
    ("Switch 2", "Fedora", 9),
    ("Switch 2", "MongoDB", 14),
    ("Router 3", "Guarani", 50),
    ("Router 3", "MongoDB", 55),
    ("Router 3", "Switch 2", 38),
]

for origen, destino, peso in conexiones:
    grafo_red.insert_edge(origen, destino, peso)

print(f"{len(conexiones)} conexiones insertadas")

print("B) RECORRIDO EN PROFUNDIDAD (DFS) desde Notebook")
print("Recorrido DFS (Deep Search):")
grafo_red.deep_sweep("Notebook")

print("C) CAMINO MÁS CORTO: PC → Impresora")

camino_pc_impresora = grafo_red.dijkstra("PC")

temp_list = []
while camino_pc_impresora.size() > 0:
    temp_list.append(camino_pc_impresora.pop())

path_pc_impresora = []
costo_total = 0
for nodo in temp_list:
    if nodo[0] == "Impresora":
        current = nodo
        path_pc_impresora.append(current[0])
        costo_total = current[1]
        
        while current[2] is not None:
            for n in temp_list:
                if n[0] == current[2]:
                    current = n
                    path_pc_impresora.append(current[0])
                    break
        break

path_pc_impresora.reverse()

if path_pc_impresora:
    print(f"Camino encontrado:")
    print(f"Ruta: {' → '.join(path_pc_impresora)}")
    print(f"Latencia total: {costo_total} ms")
else:
    print("No hay camino disponible")

print("D) ÁRBOL DE EXPANSIÓN MÍNIMO (MST)")

print("\nCalculando MST con algoritmo de Kruskal desde Router 1...")
mst_result = grafo_red.kruskal("Router 1")

print(f"Árbol de expansión mínimo:")
print(f"{mst_result}")

print("E) CAMINO MÁS CORTO: PC (no notebook) → Guarani")

camino_pc_guarani = grafo_red.dijkstra("PC")

temp_list_guarani = []
while camino_pc_guarani.size() > 0:
    temp_list_guarani.append(camino_pc_guarani.pop())

path_pc_guarani = []
costo_guarani = 0
for nodo in temp_list_guarani:
    if nodo[0] == "Guarani":
        current = nodo
        path_pc_guarani.append(current[0])
        costo_guarani = current[1]
        
        while current[2] is not None:
            for n in temp_list_guarani:
                if n[0] == current[2]:
                    current = n
                    path_pc_guarani.append(current[0])
                    break
        break

path_pc_guarani.reverse()

if path_pc_guarani:
    print(f"Camino encontrado:")
    print(f"Ruta: {' → '.join(path_pc_guarani)}")
    print(f"Latencia total: {costo_guarani} ms")
else:
    print("No hay camino disponible")

print("F) CAMINO MÁS CORTO: Switch → MongoDB")

camino_switch_mongodb = grafo_red.dijkstra("Switch 1")

temp_list_mongodb = []
while camino_switch_mongodb.size() > 0:
    temp_list_mongodb.append(camino_switch_mongodb.pop())

path_switch_mongodb = []
costo_mongodb = 0
for nodo in temp_list_mongodb:
    if nodo[0] == "MongoDB":
        current = nodo
        path_switch_mongodb.append(current[0])
        costo_mongodb = current[1]
        
        while current[2] is not None:
            for n in temp_list_mongodb:
                if n[0] == current[2]:
                    current = n
                    path_switch_mongodb.append(current[0])
                    break
        break

path_switch_mongodb.reverse()

if path_switch_mongodb:
    print(f"Camino encontrado:")
    print(f"Ruta: {' → '.join(path_switch_mongodb)}")
    print(f"Latencia total: {costo_mongodb} ms")
else:
    print("No hay camino disponible")

print("G) CAMBIAR CONEXIÓN: Impresora con Router 2")

print("1. Eliminando conexión: Impresora ↔ Router 1 (peso: 80)")
grafo_red.delete_edge("Impresora", "Router 1", 'value')

print("2. Agregando nueva conexión: Impresora ↔ Router 2 (peso: 50)")
grafo_red.insert_edge("Impresora", "Router 2", 50)

print("Conexión actualizada")

print("Recalculando camino más corto: PC → Impresora")
camino_pc_impresora_nuevo = grafo_red.dijkstra("PC")

temp_list_nuevo = []
while camino_pc_impresora_nuevo.size() > 0:
    temp_list_nuevo.append(camino_pc_impresora_nuevo.pop())

path_pc_impresora_nuevo = []
costo_nuevo = 0
for nodo in temp_list_nuevo:
    if nodo[0] == "Impresora":
        current = nodo
        path_pc_impresora_nuevo.append(current[0])
        costo_nuevo = current[1]
        
        while current[2] is not None:
            for n in temp_list_nuevo:
                if n[0] == current[2]:
                    current = n
                    path_pc_impresora_nuevo.append(current[0])
                    break
        break

path_pc_impresora_nuevo.reverse()

if path_pc_impresora_nuevo:
    print(f"Nuevo camino encontrado:")
    print(f"Ruta: {' → '.join(path_pc_impresora_nuevo)}")
    print(f"Latencia total: {costo_nuevo} ms")
    print(f"Mejora: {costo_total - costo_nuevo} ms" if costo_total > costo_nuevo else f"  Desmejorado: {costo_nuevo - costo_total} ms")

print("H) VALIDACIÓN: GRAFO NO DIRIGIDO")

print(f"Grafo configurado como: {'Dirigido' if grafo_red.is_directed else 'No Dirigido'}")
print("Las conexiones funcionan en ambas direcciones")

print("RESUMEN DE LA RED")

print("Nodos por tipo:")
tipos_contador = {}
for nodo, tipo in nodos_red.items():
    if tipo not in tipos_contador:
        tipos_contador[tipo] = 0
    tipos_contador[tipo] += 1

for tipo, cantidad in sorted(tipos_contador.items()):
    print(f"  • {tipo.capitalize()}: {cantidad}")

print(f"Total de nodos: {len(nodos_red)}")
print(f"Total de conexiones: {len(conexiones)}")
