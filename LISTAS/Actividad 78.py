#78. A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir
lista1=["a","b","D","x","r","X","3","h","w","2","i"]
print(lista1)
valor=int(input("Que valor quieres eliminar: "))

while True:
    if valor.isdigit():
        if valor=="2":
            lista1.remove("2")
        elif valor=="3":
            lista1.remove("3")
        else:
            print("Introduce un valor que este en la lista")
            break
    elif valor.isalpha():
        if valor=="r":
            lista1.remove("r")
    
