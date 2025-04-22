# # El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
# # otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
# # objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
# # ayuda de la fuerza” realizar las siguientes actividades:

# # a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
# # queden más objetos en la mochila;

# # b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
# # car para encontrarlo;

# # c. Utilizar un vector para representar la mochila.


def buscar_sable(mochila,obj_sac=0):

    if (len(mochila) == obj_sac):
        print('no esta el sable')
        return

    if mochila[0]=='sable de luz':
        print(f'se enconto el sable de luz despues de sacar {obj_sac} objetos')  
    else:
        return(buscar_sable(mochila[1:],obj_sac+1))
    
mochila=['botella','sable de luz','pistola']

buscar_sable(mochila)
