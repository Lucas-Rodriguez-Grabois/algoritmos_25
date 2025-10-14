from tree import BinaryTree

arbol = BinaryTree()

criaturas = [
    ("Hidra de Lerna", "Heracles"),
    ("Leon de Nemea", "Heracles"),
    ("Cerbero", "Heracles"),
    ("Toro de Creta", "Theseus"),
    ("Cierva Cerinea", "Heracles"),
    ("Jabalí de Erimanto", "Heracles"),
    ("Aves del Estínfalo", "Heracles"),
    ("Talos", "Medea"),
    ("Basilisco", "Perseo"),
    ("Sirenas", "Odiseo"),
    ("Ladón", "Heracles"),
    ("Quimera", "Belerofonte"),
    ("Minotauro", "Theseus"),
    ("Esfinge", "Edipo"),
    ("Medusa", None)
]

for nombre, derrotado_por in criaturas:
    descripcion = input(f"Ingrese descripcion para {nombre}: ")
    capturada = None
    arbol.insert(nombre, {"derrotado_por": derrotado_por, "descripcion": descripcion, "capturada": capturada})

def listar_inorden(arbol):
    def inorden(root):
        if root is not None:
            inorden(root.left)
            print(f"{root.value} - Derrotado por: {root.other_values['derrotado_por']} - Descripcion: {root.other_values['descripcion']}")
            inorden(root.right)
    if arbol.root is not None:
        inorden(arbol.root)

def info_talos(arbol):
    nodo = arbol.search("Talos")
    if nodo is not None:
        print(f"Nombre: {nodo.value}, Derrotado por: {nodo.other_values['derrotado_por']}, Descripcion: {nodo.other_values['descripcion']}, Capturada por: {nodo.other_values['capturada']}")

def top_3_derrotadores(arbol):
    ranking = {}
    def contar_derrotas(root):
        if root is not None:
            derrotador = root.other_values["derrotado_por"]
            if derrotador is not None:
                if derrotador not in ranking:
                    ranking[derrotador] = 1
                else:
                    ranking[derrotador] += 1
            contar_derrotas(root.left)
            contar_derrotas(root.right)
    if arbol.root is not None:
        contar_derrotas(arbol.root)
    top_3 = sorted(ranking.items(), key=lambda x: x[1], reverse=True)[:3]
    for heroe, cantidad in top_3:
        print(f"{heroe}: {cantidad}")

def criaturas_heracles(arbol):
    def buscar_heracles(root):
        if root is not None:
            buscar_heracles(root.left)
            if root.other_values["derrotado_por"] == "Heracles":
                print(root.value)
            buscar_heracles(root.right)
    if arbol.root is not None:
        buscar_heracles(arbol.root)

def criaturas_no_derrotadas(arbol):
    def buscar_no_derrotadas(root):
        if root is not None:
            buscar_no_derrotadas(root.left)
            if root.other_values["derrotado_por"] is None:
                print(root.value)
            buscar_no_derrotadas(root.right)
    if arbol.root is not None:
        buscar_no_derrotadas(arbol.root)

def modificar_captura_heracles(arbol):
    for criatura in ["Cerbero", "Toro de Creta", "Cierva Cerinea", "Jabalí de Erimanto"]:
        nodo = arbol.search(criatura)
        if nodo is not None:
            nodo.other_values["capturada"] = "Heracles"

def buscar_coincidencia(arbol, texto):
    arbol.proximity_search(texto)

def eliminar_basilisco_sirenas(arbol):
    for criatura in ["Basilisco", "Sirenas"]:
        value, other = arbol.delete(criatura)
        if value is not None:
            print(f"{value} eliminado")

def modificar_aves_estinfalo(arbol):
    nodo = arbol.search("Aves del Estínfalo")
    if nodo is not None:
        if "varias" not in nodo.other_values["derrotado_por"]:
            nodo.other_values["derrotado_por"] = "Heracles (varias)"
            print("Aves del Estínfalo modificado")

def modificar_ladon(arbol):
    nodo = arbol.search("Ladón")
    if nodo is not None:
        value, other = arbol.delete("Ladón")
        arbol.insert("Dragón Ladón", other)
        print("Ladón modificado a Dragón Ladón")

def listar_por_nivel(arbol):
    arbol.by_level()

def listar_capturadas_heracles(arbol):
    def buscar_capturadas(root):
        if root is not None:
            buscar_capturadas(root.left)
            if root.other_values["capturada"] == "Heracles":
                print(root.value)
            buscar_capturadas(root.right)
    if arbol.root is not None:
        buscar_capturadas(arbol.root)

print("PUNTO A: Listado inorden:")
listar_inorden(arbol)
print("PUNTO C: Informacion de Talos:")
info_talos(arbol)
print("PUNTO D: Top 3 heroes/dioses con mas derrotas:")
top_3_derrotadores(arbol)
print("PUNTO E: Criaturas derrotadas por Heracles:")
criaturas_heracles(arbol)
print("PUNTO F: Criaturas no derrotadas:")
criaturas_no_derrotadas(arbol)
modificar_captura_heracles(arbol)
print("PUNTO I: Busqueda por coincidencia (ejemplo: 'Le'):")
buscar_coincidencia(arbol, "Le")
print("PUNTO J: Eliminacion de Basilisco y Sirenas:")
eliminar_basilisco_sirenas(arbol)
print("PUNTO K: Modificacion Aves del Estinfalo:")
modificar_aves_estinfalo(arbol)
print("PUNTO L: Modificacion Ladon:")
modificar_ladon(arbol)
print("PUNTO M: Listado por nivel:")
listar_por_nivel(arbol)
print("PUNTO N: Criaturas capturadas por Heracles:")
listar_capturadas_heracles(arbol)