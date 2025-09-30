from list_ import List

jedis = List()

jedis.append({"nombre": "Yoda", "maestro": None, "sables": ["verde"], "especie": "desconocida"})
jedis.append({"nombre": "Luke Skywalker", "maestro": "Yoda", "sables": ["verde", "azul"], "especie": "humano"})
jedis.append({"nombre": "Ahsoka Tano", "maestro": "Anakin Skywalker", "sables": ["verde", "blanco"], "especie": "togruta"})
jedis.append({"nombre": "Kit Fisto", "maestro": None, "sables": ["verde"], "especie": "nautolán"})
jedis.append({"nombre": "Obi-Wan Kenobi", "maestro": "Qui-Gon Jinn", "sables": ["azul"], "especie": "humano"})
jedis.append({"nombre": "Anakin Skywalker", "maestro": "Obi-Wan Kenobi", "sables": ["azul"], "especie": "humano"})
jedis.append({"nombre": "Qui-Gon Jinn", "maestro": "Conde Dooku", "sables": ["verde"], "especie": "humano"})
jedis.append({"nombre": "Mace Windu", "maestro": None, "sables": ["violeta"], "especie": "humano"})
jedis.append({"nombre": "Plo Koon", "maestro": None, "sables": ["naranja"], "especie": "kel dor"})
jedis.append({"nombre": "Aayla Secura", "maestro": "Quinlan Vos", "sables": ["azul"], "especie": "twilek"})
jedis.append({"nombre": "Rey", "maestro": "Leia Organa", "sables": ["amarillo"], "especie": "humano"})

def order_by_nombre(value): return value["nombre"]
def order_by_especie(value): return value["especie"]

jedis.add_criterion("nombre", order_by_nombre)
jedis.add_criterion("especie", order_by_especie)

# a) listado ordenado por nombre y por especie
def listado_ordenado(value):
    print("Ordenado por nombre:")
    value.sort_by_criterion("nombre")
    for j in value:
        print(j["nombre"])
    print("\nOrdenado por especie:")
    value.sort_by_criterion("especie")
    for j in value:
        print(f"{j['nombre']} - {j['especie']}")

# b) info de Ahsoka Tano y Kit Fisto
def info_Ahsoka_Kit(value):
    resultado = []
    for nombre in ["Ahsoka Tano", "Kit Fisto"]:
        index = value.search(nombre, "nombre")
        if index is not None:
            resultado.append(value[index])
    return resultado

# c) padawans de Yoda y Luke
def padawans_yoda_luke(value):
    resultado = []
    for maestro in ["Yoda", "Luke Skywalker"]:
        alumnos = [j["nombre"] for j in value if j["maestro"] == maestro]
        resultado.append({maestro: alumnos})
    return resultado

# d) jedis humanos y twilek
def humanos_twilek(value):
    return [j["nombre"] for j in value if j["especie"] in ["humano", "twilek"]]

# e) jedis que empiezan con A
def jedis_con_A(value):
    return [j["nombre"] for j in value if j["nombre"].startswith("A")]

# f) jedis con más de un sable
def mas_de_un_sable(value):
    return [j["nombre"] for j in value if len(j["sables"]) > 1]

# g) jedis con sable amarillo o violeta
def amarillo_violeta(value):
    return [j["nombre"] for j in value if "amarillo" in j["sables"] or "violeta" in j["sables"]]

# h) padawans de Qui-Gon Jinn y Mace Windu
def padawans_QuiGon_Mace(value):
    resultado = []
    for maestro in ["Qui-Gon Jinn", "Mace Windu"]:
        alumnos = [j["nombre"] for j in value if j["maestro"] == maestro]
        resultado.append({maestro: alumnos})
    return resultado

listado_ordenado(jedis)
print("b)", info_Ahsoka_Kit(jedis))
print("c)", padawans_yoda_luke(jedis))
print("d)", humanos_twilek(jedis))
print("e)", jedis_con_A(jedis))
print("f)", mas_de_un_sable(jedis))
print("g)", amarillo_violeta(jedis))
print("h)", padawans_QuiGon_Mace(jedis))
