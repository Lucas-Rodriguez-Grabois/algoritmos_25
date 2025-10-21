from heap import HeapMax

cola_impresion = HeapMax()

# a. Cargue tres documentos de empleados
print("a. cargue tres documentos de empleados")
cola_impresion.arrive('Doc_Empleado_1', 1)
cola_impresion.arrive('Doc_Empleado_2', 1)
cola_impresion.arrive('Doc_Empleado_3', 1)
print("Estado de la cola (elementos internos del heap):", cola_impresion.elements)

# b. Imprima el primer documento de la cola
print("b. imprima el primer documento de la cola")
doc_impreso_b = cola_impresion.attention()
print(f"   Impreso: {doc_impreso_b[1]} (Prioridad: {doc_impreso_b[0]})")
print("Estado de la cola:", cola_impresion.elements)

# c. Cargue dos documentos del staff de TI
print("c. cargue dos documentos del staff de TI.")
cola_impresion.arrive('Doc_TI_1', 2)
cola_impresion.arrive('Doc_TI_2', 2)
print("Estado de la cola:", cola_impresion.elements)

# d. Cargue un documento del gerente
print("d. Cargue un documento del gerente:")
cola_impresion.arrive('Doc_Gerente_1', 3)
print("Estado de la cola:", cola_impresion.elements)

# e. Imprima los dos primeros documentos de la cola
print("e. Imprima los dos primeros documentos de la cola:")
doc_impreso_e1 = cola_impresion.attention()
print(f"   Impreso (1/2): {doc_impreso_e1[1]} (Prioridad: {doc_impreso_e1[0]})")
doc_impreso_e2 = cola_impresion.attention()
print(f"   Impreso (2/2): {doc_impreso_e2[1]} (Prioridad: {doc_impreso_e2[0]})")
print("Estado de la cola:", cola_impresion.elements)

# f. Cargue dos documentos de empleados  y uno de gerente
print("f. cargue dos documentos de empleados y uno de gerente:")
cola_impresion.arrive('Doc_Empleado_4', 1)
cola_impresion.arrive('Doc_Empleado_5', 1)
cola_impresion.arrive('Doc_Gerente_2', 3)
print("Estado de la cola:", cola_impresion.elements)

# g. Imprima todos los documentos de la cola de impresión
print("g. Imprima todos los documentos de la cola de impresión")
while cola_impresion.size() > 0:
    doc_final = cola_impresion.attention()
    print(f"   Impreso: {doc_final[1]} (Prioridad: {doc_final[0]})")

print("Estado final de la cola:", cola_impresion.elements)