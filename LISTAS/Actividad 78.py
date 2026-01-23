#78. A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir
lista1 = ["a", "b", "D", "x", "r", "X", "3", "h", "w", "2", "i"]

print(lista1)

valor_desplazado=input("Introduce el valor que se desplazó: ")

if valor_desplazado in lista1:
    indice_original=lista1.index(valor_desplazado)
    print(f"El valor '{valor_desplazado}' estaba originalmente en la posición {indice_original}.")
    
    nueva_posicion = input(f"Introduce la nueva posición (0-{len(lista1)-1}) de '{valor_desplazado}': ")
    
    if nueva_posicion.isdigit():
        nueva_posicion=int(nueva_posicion)
        if 0<=nueva_posicion<len(lista1):
            lista_desplazada=lista1.copy()
            lista_desplazada.pop(indice_original)
            lista_desplazada.insert(nueva_posicion, valor_desplazado)
            print("Lista después del desplazamiento:", lista_desplazada)
        else:
            print("Error: la nueva posición está fuera del rango de la lista.")
    else:
        print("Error: la nueva posición debe ser un número entero.")
else:
    print(f"El valor '{valor_desplazado}' no se encuentra en la lista original.")

print("Índices originales:")
for i, elemento in enumerate(lista1):
    print(f"{i}: {elemento}")
    
