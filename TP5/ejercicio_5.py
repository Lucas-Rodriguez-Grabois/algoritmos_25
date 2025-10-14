from tree import BinaryTree
from super_heroes_data import superheroes as data

arbol = BinaryTree()
arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()

for hero in data:
    arbol.insert(hero["name"], {"is_villain": hero["is_villain"]})

def listar_villanos(arbol):
    def villanos_ordenados(root):
        if root is not None:
            villanos_ordenados(root.left)
            if root.other_values["is_villain"]:
                print(root.value)
            villanos_ordenados(root.right)
    if arbol.root is not None:
        villanos_ordenados(arbol.root)

def heroes_con_c(arbol):
    def buscar_c(root):
        if root is not None:
            buscar_c(root.left)
            if root.value.startswith("C") and not root.other_values["is_villain"]:
                print(root.value)
            buscar_c(root.right)
    if arbol.root is not None:
        buscar_c(arbol.root)

def contar_superheroes(arbol):
    def contar_heroes(root):
        count = 0
        if root is not None:
            if not root.other_values["is_villain"]:
                count += 1
            count += contar_heroes(root.left)
            count += contar_heroes(root.right)
        return count
    total = 0
    if arbol.root is not None:
        total = contar_heroes(arbol.root)
    return total

def corregir_doctor_strange(arbol):
    def buscar_doctor(root):
        if root is not None:
            if root.value.startswith("Dr") and root.value != "Doctor Strange":
                print(f"Corregiendo {root.value} a Doctor Strange")
                value, other = arbol.delete(root.value)
                arbol.insert("Doctor Strange", other)
            buscar_doctor(root.left)
            buscar_doctor(root.right)
    if arbol.root is not None:
        buscar_doctor(arbol.root)

def listar_heroes_descendente(arbol):
    def heroes_descendente(root):
        if root is not None:
            heroes_descendente(root.right)
            if not root.other_values["is_villain"]:
                print(root.value)
            heroes_descendente(root.left)
    if arbol.root is not None:
        heroes_descendente(arbol.root)

def contar_nodos(arbol):
    def contar(root):
        count = 0
        if root is not None:
            count += 1
            count += contar(root.left)
            count += contar(root.right)
        return count
    total = 0
    if arbol.root is not None:
        total = contar(arbol.root)
    return total

arbol.divide_tree(arbol_heroes, arbol_villanos)

print("Villanos ordenados alfabeticamente:")
listar_villanos(arbol)
print("Superheroes que empiezan con C:")
heroes_con_c(arbol)
print("Cantidad de superheroes:", contar_superheroes(arbol))
corregir_doctor_strange(arbol)
print("Superheroes ordenados descendente:")
listar_heroes_descendente(arbol)
print("Nodos en arbol de heroes:", contar_nodos(arbol_heroes))
print("Nodos en arbol de villanos:", contar_nodos(arbol_villanos))
print("Barrido ordenado de heroes:")
arbol_heroes.in_order()
print("Barrido ordenado de villanos:")
arbol_villanos.in_order()