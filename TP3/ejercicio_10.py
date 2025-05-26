from stack import Stack
from queue_ import Queue  

notificaciones = Queue()
notificaciones.arrive(("11:43", "facebook", "tenes un nuevo amigo"))
notificaciones.arrive(("11:50", "twitter", "Python te reeposteo"))
notificaciones.arrive(("15:57", "twitter", "Nuevo seguidor"))
notificaciones.arrive(("15:20", "facebook", "Te han etiquetado"))

def elim_facebook(cola: Queue) -> None:
    cola_aux = Queue()
    while cola.size() > 0:
        notif = cola.attention()
        hora, app, mensaje = notif
        if app != "facebook":
            cola_aux.arrive(notif)
    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())

def mensaje_python(cola: Queue) -> None:
    cola_aux = Queue()
    print("Notificaciones de twitter con 'Python':")
    while cola.size() > 0:
        notif = cola.attention()
        hora, app, mensaje = notif
        if app == "twitter" and "Python" in mensaje:
            print(f"{hora} - {mensaje}")
        cola_aux.arrive(notif)
    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())

def almacenar_hora(cola: Queue, hora_inicio: str, hora_fin: str) -> int:
    pila = Stack()
    n = cola.size()
    for _ in range(n):
        notif = cola.on_front()
        hora, app, mensaje = notif
        if hora_inicio <= hora <= hora_fin:
            pila.push(notif)
        cola.move_to_end()
    return pila.size()

print("Cola original:")
notificaciones.show()

print("Punto A ")
elim_facebook(notificaciones)
notificaciones.show()

print("Punto B ")
mensaje_python(notificaciones)

print("Punto C")
print(f"Cantidad de notificaciones en el rango: {almacenar_hora(notificaciones, "11:43", "15:57")}")
