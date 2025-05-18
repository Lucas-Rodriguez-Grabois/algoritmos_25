from typing import Any, Optional  

class Stack:
    # Clase que implementa una pila (estructura LIFO)

    def __init__(self):
        # Constructor: crea una lista vacía para almacenar los elementos de la pila
        self.__elements = []

    def push(self, value: Any) -> None:
        # Agrega un elemento al tope de la pila
        self.__elements.append(value)

    def pop(self) -> Optional[Any]:
        # Quita y devuelve el elemento del tope de la pila
        # Si está vacía, retorna None
        return (
            self.__elements.pop()
            if self.__elements
            else None
        )

    def size(self) -> int:
        # Retorna la cantidad de elementos en la pila
        return len(self.__elements)

    def on_top(self) -> Optional[Any]:
        # Devuelve el valor en el tope de la pila sin quitarlo
        # Si la pila está vacía, retorna None
        return (
            self.__elements[-1]
            if self.__elements
            else None
        )

    def show(self):
        # Muestra el contenido de la pila sin alterar su orden
        aux_stack = Stack()  # Creamos una pila auxiliar

        while self.size() > 0:
            value = self.pop()     # Quitamos el tope
            print(value)           # Lo imprimimos
            aux_stack.push(value)  # Lo pasamos a la pila auxiliar

        while aux_stack.size() > 0:
            self.push(aux_stack.pop())  # Restauramos los elementos a la pila original

