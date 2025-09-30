from list_ import List

superheroes = List()

superheroes.append({"nombre": "Superman", "año": 1938, "aparicion": "Action Comics #1", "casa": "DC Comics", "biografia": "Traje azul y capa roja."})
superheroes.append({"nombre": "Batman", "año": 1939, "aparicion": "Detective Comics #27", "casa": "DC Comics", "biografia": "Héroe con traje de murciélago."})
superheroes.append({"nombre": "Spider-Man", "año": 1962, "aparicion": "Amazing Fantasy #15", "casa": "Marvel Comics", "biografia": "Spider-Man es un superhéroe ficticio creado por Stan Lee y Steve Ditko."})
superheroes.append({"nombre": "Iron Man", "año": 1963, "aparicion": "Tales of Suspense #39", "casa": "Marvel Comics", "biografia": "Usa una armadura tecnológica."})
superheroes.append({"nombre": "Linterna Verde", "año": 1940, "aparicion": "All-American Comics #16", "casa": "DC Comics", "biografia": "Linterna Verde usa un anillo de poder."})
superheroes.append({"nombre": "Flash", "año": 1940, "aparicion": "Flash Comics #1", "casa": "DC Comics", "biografia": "Velocidad sobrehumana."})
superheroes.append({"nombre": "Wolverine", "año": 1974, "aparicion": "The Incredible Hulk #180", "casa": "Marvel Comics", "biografia": "Mutante con garras y factor curativo."})
superheroes.append({"nombre": "Dr.Strange", "año": 1963, "aparicion": "Strange Tales #110", "casa": "DC Comics", "biografia": "Mago supremo."})
superheroes.append({"nombre": "Star-Lord", "año": 1976, "aparicion": "Marvel Preview #4", "casa": "Marvel Comics", "biografia": "Líder de los Guardianes de la Galaxia."})
superheroes.append({"nombre": "Capitana Marvel", "año": 1968, "aparicion": "Marvel Super-Heroes #13", "casa": "Marvel Comics", "biografia": "Poder cósmico."})
superheroes.append({"nombre": "Mujer Maravilla", "año": 1941, "aparicion": "All-Star Comics #8", "casa": "DC Comics", "biografia": "Princesa amazona."})

def order_by_nombre(value): return value["nombre"]
def order_by_casa(value): return value["casa"]
def order_by_año(value): return value["año"]

superheroes.add_criterion("nombre", order_by_nombre)
superheroes.add_criterion("casa", order_by_casa)
superheroes.add_criterion("año", order_by_año)

# a) eliminar Linterna Verde
def remove_linternaverde(value):
    while True:
        index = value.search("Linterna Verde", "nombre")
        if index is not None:
            value.delete_value("Linterna Verde", "nombre")
        else:
            break

# b) año de Wolverine
def wolverine_año(value):
    index = value.search("Wolverine", "nombre")
    if index is not None:
        return value[index]["año"]

# c) cambiar casa de Dr. Strange a Marvel
def DrStrange_cambiarCasa(value):
    index = value.search("Dr.Strange", "nombre")
    if index is not None:
        value[index]["casa"] = "Marvel Comics"

# d) superhéroes con “traje” o “armadura”
def mostrar_superheroesarmadura(value):
    return [item["nombre"] for item in value if "traje" in item["biografia"].lower() or "armadura" in item["biografia"].lower()]

# e) superhéroes anteriores a 1963
def mostrar_superheroes1963(value):
    return [item["nombre"] for item in value if item["año"] < 1963]

# f) casa de Capitana Marvel y Mujer Maravilla
def CapitanaMaravilla(value):
    casas = []
    for nombre in ["Capitana Marvel", "Mujer Maravilla"]:
        index = value.search(nombre, "nombre")
        if index is not None:
            casas.append(value[index]["casa"])
        else:
            casas.append(None)
    return casas

# g) información de Flash y Star-Lord
def flashStar(value):
    resultado = []
    for nombre in ["Flash", "Star-Lord"]:
        index = value.search(nombre, "nombre")
        if index is not None:
            item = value[index]
            resultado.append(f"{item['nombre']} ({item['año']}) - {item['aparicion']} - {item['casa']} - {item['biografia']}")
        else:
            resultado.append(None)
    return resultado

# h) superhéroes que comienzan con B, M o S
def letraBMS(value):
    return [item["nombre"] for item in value if item["nombre"][0] in "BMS"]

# i) contar héroes por casa
def contarcasa(value):
    DC, Marvel = 0, 0
    for item in value:
        if item["casa"] == "DC Comics":
            DC += 1
        elif item["casa"] == "Marvel Comics":
            Marvel += 1
    return f"DC Comics: {DC}, Marvel Comics: {Marvel}"


# --- Ejecuciones ---
remove_linternaverde(superheroes)
print("b)", wolverine_año(superheroes))
DrStrange_cambiarCasa(superheroes)
print("d)", mostrar_superheroesarmadura(superheroes))
print("e)", mostrar_superheroes1963(superheroes))
print("f)", CapitanaMaravilla(superheroes))
print("g)", flashStar(superheroes))
print("h)", letraBMS(superheroes))
print("i)", contarcasa(superheroes))

