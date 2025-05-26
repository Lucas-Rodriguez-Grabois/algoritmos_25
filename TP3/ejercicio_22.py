from queue_ import Queue

class Personaje:
    def __init__(self, identidad, superheroe, genero):
        self.identidad = identidad  
        self.superheroe = superheroe  
        self.genero = genero  

    def __str__(self):
        return f"{self.identidad} - {self.superheroe} - {self.genero}"

mcu = Queue()
mcu.arrive(Personaje("Tony Stark", "Iron Man", "M"))
mcu.arrive(Personaje("Steve Rogers", "Capitán América", "M"))
mcu.arrive(Personaje("Natasha Romanoff", "Black Widow", "F"))
mcu.arrive(Personaje("Carol Danvers", "Capitana Marvel", "F"))
mcu.arrive(Personaje("Scott Lang", "Ant-Man", "M"))

def capitana_marvel(cola: Queue) -> str:
    for _ in range(cola.size()):
        personaje = cola.on_front()
        if personaje.superheroe == "Capitana Marvel":
            return personaje.identidad
        cola.move_to_end()
    return "No encontrado"

def superheroes_femeninos(cola: Queue) -> None:
    print("Superhéroes femeninos:")
    for _ in range(cola.size()):
        personaje = cola.on_front()
        if personaje.genero == "F":
            print(personaje.superheroe)
        cola.move_to_end()

def personajes_masculinos(cola: Queue) -> None:
    print("Personajes masculinos:")
    for _ in range(cola.size()):
        personaje = cola.on_front()
        if personaje.genero == "M":
            print(personaje.identidad)
        cola.move_to_end()

def scott_lang(cola: Queue) -> str:
    for _ in range(cola.size()):
        personaje = cola.on_front()
        if personaje.identidad == "Scott Lang":
            return personaje.superheroe
        cola.move_to_end()
    return "No encontrado"

def nombres_con_letra(cola: Queue, letra: str) -> None:
    print(f"Personajes cuyos nombres comienzan con '{letra}':")
    for _ in range(cola.size()):
        personaje = cola.on_front()
        if personaje.identidad.startswith(letra) or personaje.superheroe.startswith(letra):
            print(personaje)
        cola.move_to_end()

def carol_danvers(cola: Queue) -> None:
    for _ in range(cola.size()):
        personaje = cola.on_front()
        if personaje.identidad == "Carol Danvers":
            print(f"Carol Danvers está en la cola. Su superhéroe es: {personaje.superheroe}")
            return
        cola.move_to_end()
    print("Carol Danvers no está en la cola.")

print("Cola original:")
mcu.show()
print("Punto A")
print(f"El nombre del personaje de Capitana Marvel es: {capitana_marvel(mcu)}")
print("Punto B")
superheroes_femeninos(mcu)
print("Punto C")
personajes_masculinos(mcu)
print("Punto D")
print(f"El superhéroe de Scott Lang es: {scott_lang(mcu)}")
print("Punto E")
nombres_con_letra(mcu, "S")
print("Punto F")
carol_danvers(mcu)
