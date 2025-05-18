from stack import Stack

personaje = Stack()
personaje.push({'nombre': 'Iron Man', 'pelicula': 9})
personaje.push({'nombre': 'Thor', 'pelicula': 9})
personaje.push({'nombre': 'Capitan America', 'pelicula': 9})
personaje.push({'nombre': 'Groot', 'pelicula': 6})
personaje.push({'nombre': 'Rocket Raccoon', 'pelicula': 6})
personaje.push({'nombre': 'Viuda Negra', 'pelicula': 9})

def determinar_posicion(pila: Stack) -> None:
    aux=Stack()
    posicion=1  
    rocket_=None
    groot_=None

    while pila.size() > 0:
        person = pila.pop()
        aux.push(person)

        if person['nombre'] == 'Rocket Raccoon':
            rocket_=posicion
        elif person['nombre'] == 'Groot':
            groot_=posicion

        posicion += 1

    while aux.size() > 0:
        pila.push(aux.pop())

    print(f"Posición de Rocket Raccoon: {rocket_}")
    print(f"Posición de Groot: {groot_}")


def participacion(pila: Stack) -> None:
    aux=Stack()
    encontrado=False

    while pila.size() > 0:
        person=pila.pop()
        aux.push(person)

        if person['pelicula'] > 5:
            print(f"{person['nombre']} participó en {person['pelicula']} películas.")
            encontrado=True

    while aux.size() > 0:
        pila.push(aux.pop())

    if not encontrado:
        print("No se encontraron personajes con más de 5 películas.")


def peliculas_viuda_negra(pila: Stack) -> None:
    aux = Stack()
    encontrado = False

    while pila.size() > 0:
        person = pila.pop()
        aux.push(person)

        if person['nombre'] == 'Viuda Negra':
            print(f"Viuda Negra participó en {person['pelicula']} películas.")
            encontrado = True

    while aux.size() > 0:
        pila.push(aux.pop())

    if not encontrado:
        print("Viuda Negra no se encontró en la pila.")


def nombres(pila: Stack) -> None:
    aux = Stack()
    encontrado = False

    while pila.size() > 0:
        person = pila.pop()
        aux.push(person)

        if person['nombre'][0] in ['C', 'D', 'G']:
            print(f"{person['nombre']} comienza con C, D o G.")
            encontrado = True

    while aux.size() > 0:
        pila.push(aux.pop())

    if not encontrado:
        print("No se encontraron personajes cuyos nombres empiecen con C, D o G.")

print("DETERMINAR LA POSICION")
determinar_posicion(personaje)
print("PARTICIPACION EN MAS DE 5 PELICULAS")
participacion(personaje)
print("PARTICIPACION DE VIUDA NEGRA")
peliculas_viuda_negra(personaje)
print("NOMBRES QUE EMPIECEN CON C, D Y G")
nombres(personaje)
