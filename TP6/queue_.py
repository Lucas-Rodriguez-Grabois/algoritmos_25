from typing import Any, Optional

class Queue:

    def __init__(self):
        # Inicializa una lista privada para almacenar los elementos de la cola
        self.__elements = []

    def arrive(self, value: Any) -> None:
        # Agrega un elemento al final de la cola
        self.__elements.append(value)

    def attention(self) -> Optional[Any]:
        # Atiende (elimina y devuelve) el primer elemento de la cola
        # Si la cola está vacía, devuelve None
        return (
            self.__elements.pop(0)
            if self.__elements
            else None
        )

    def size(self) -> int:
        # Devuelve el número de elementos en la cola
        return len(self.__elements)
    
    def on_front(self) -> Optional[Any]:
        # Devuelve el primer elemento de la cola sin eliminarlo
        # Si está vacía, devuelve None
        return (
            self.__elements[0]
            if self.__elements
            else None
        )

    def move_to_end(self) -> Optional[Any]:
        # Toma el primer elemento de la cola, lo elimina
        # y lo vuelve a insertar al final (recirculación)
        if self.__elements:
            value = self.attention()
            self.arrive(value)
            return value

    def show(self):
        # Muestra todos los elementos de la cola en orden,
        # sin alterar su orden final. Lo logra recirculando todos los elementos.
        for i in range(len(self.__elements)):
            print(self.move_to_end())
