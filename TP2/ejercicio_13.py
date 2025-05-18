from stack import Stack 


traje = Stack()
traje.push({'modelo': 'Mark I', 'pelicula': 'Iron Man 1', 'estado': 'Destruida'})
traje.push({'modelo': 'Mark I', 'pelicula': 'Iron Man 2', 'estado': 'Impecable'})
traje.push({'modelo': 'Mark I', 'pelicula': 'Iron Man 3', 'estado': 'Destruida'})
traje.push({'modelo': 'Mark II', 'pelicula': 'Iron Man 1', 'estado': 'Destruida'})
traje.push({'modelo': 'Mark II', 'pelicula': 'Iron Man 2', 'estado': 'Impecable'})
traje.push({'modelo': 'Mark II', 'pelicula': 'Iron Man 3', 'estado': 'Destruida'})
traje.push({'modelo': 'Mark II (Casco)', 'pelicula': 'Avengers: Endgame', 'estado': 'Impecable'})
traje.push({'modelo': 'Mark II (Casco)', 'pelicula': 'Deadpool And Wolverine', 'estado': 'Impecable'})
traje.push({'modelo': 'Mark III', 'pelicula': 'Iron Man 1', 'estado': 'Impecable'})
traje.push({'modelo': 'Mark III', 'pelicula': 'Iron Man 2', 'estado': 'Impecable'})
traje.push({'modelo': 'Mark III', 'pelicula': 'Iron Man 3', 'estado': 'Impecable'})
traje.push({'modelo': 'Mark IV', 'pelicula': 'Iron Man 2', 'estado': 'Destruida'})
traje.push({'modelo': 'Mark IV', 'pelicula': 'Iron Man 3', 'estado': 'Destruida'})
traje.push({'modelo': 'Mark V', 'pelicula': 'Iron Man 2', 'estado': 'Destruida'})
traje.push({'modelo': 'Mark V', 'pelicula': 'Iron Man 3', 'estado': 'Impecable'})
traje.push({'modelo': 'Mark V', 'pelicula': 'Deadpool And Wolverine', 'estado': 'Impecable'})
traje.push({'modelo': 'Mark LXXXV', 'pelicula': 'Avengers: Endgame', 'estado': 'Dañada'})
traje.push({'modelo': 'Mark XLVII', 'pelicula': 'Spider-Man: Homecoming', 'estado': 'Impecable'})
traje.push({'modelo': 'Mark XLVI', 'pelicula': 'Capitan America: Civil War', 'estado': 'Dañada'})
traje.push({'modelo': 'Mark XLIV', 'pelicula': 'Avengers: Age of Ultron', 'estado': 'Impecable'})

def buscar_markXLIV(pila:Stack):
    encontrado=False
    aux=Stack()
    while pila.size()>0:
        buscar=pila.pop()
        if buscar['modelo']== 'Mark XLIV':
            print(f"el modelo fue encontrado en {buscar["pelicula"]}")
            encontrado=True
        aux.push(buscar)
    while aux.size()>0:
        pila.push(aux.pop())
    if encontrado==False:
        print("Hulkbuster no encontrado.")

def armaduras_dañadas(pila: Stack) -> None:
    aux= Stack()
    print("Modelos dañados:")
    while pila.size() > 0:
        buscar = pila.pop()
        if buscar["estado"] == "Dañado":
            print(buscar["modelo"])
        aux.push(buscar)
    while aux.size() > 0:
        pila.push(aux.pop())

def eliminar_modelo_destruido(pila: Stack) -> None:
    aux = Stack()
    print("Eliminando modelos destruidos:")
    while pila.size() > 0:
        buscar = pila.pop()
        if buscar["estado"] != "Destruido":
            aux.push(buscar)
        else:
            print(f"Modelo eliminado: {buscar["modelo"]}")
    while aux.size() > 0:
        pila.push(aux.pop())

def armaduras_utilizadas(pila: Stack) -> None:
    aux = Stack()
    encontrada = False
    print("Modelos utilizados en 'Spider-Man: Homecoming' y 'Capitan America: Civil War':")
    while pila.size() > 0:
        buscar = pila.pop()
        if buscar is None:
            continue
        aux.push(buscar)
        if buscar['pelicula'] == 'Spider-Man: Homecoming' or buscar['pelicula'] == 'Capitan America: Civil War':
            print(buscar['modelo'])
            encontrada = True
    while aux.size() > 0:
        pila.push(aux.pop())
    if not encontrada:
        print("No se encontraron armaduras en las películas especificadas.")

print("BUSCAR MARK XLIV")
buscar_markXLIV(traje)
print("MOSTAR MODELOS DAÑADOS")
armaduras_dañadas(traje)
print("ELIMINAR MODELOS DESTRUIDOS")
eliminar_modelo_destruido(traje)
print("ARMADURAS UTILIZADAS EN PELICULAS")
armaduras_utilizadas(traje)