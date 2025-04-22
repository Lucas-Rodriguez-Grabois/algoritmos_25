# # Desarrollar una función que permita convertir un número romano en un número decimal.
def calcular_romano(num_r,i=0,total=0):
    romanos = {
        'I': 1, 
        'V': 5, 
        'X': 10,
        'L': 50, 
        'C': 100, 
        'D': 500, 
        'M': 1000
    }
    if i >= len(num_r) - 1:
        return total + romanos[num_r[i]]
    if romanos[num_r[i]] < romanos[num_r[i+1]]:
        return calcular_romano(num_r, i + 1, total - romanos[num_r[i]])
    else:
        return calcular_romano(num_r, i + 1, total + romanos[num_r[i]])

numero_romano = 'I'
print(calcular_romano(numero_romano))