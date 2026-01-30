#Diseñar un programa que al introducir un número calcule la letra correspondiente, teniendo en cuenta los siguientes puntos:
dni=input("Introduce tu DNI: ")
longitud_dni=len(dni)
intentos=[]
letras=["T","R","w","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]

if not len(dni)==8:
    print("el valor introducido no cumple con la longitud correcta")
elif not dni .isnumeric:
    print("el valor introducido debe ser numerico")
    