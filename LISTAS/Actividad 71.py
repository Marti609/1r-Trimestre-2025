#71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en esta lista no deben almacenarse las letras que se han introducido repetidas.


milista=[]
letrasrepetidas=[]
while True:
    letra=input("Introduce una letra: ")
    if len(letra)==1:
        print("Introduce solo una letra.")   
    elif letra in milista:
        print(f"La letra {letra} ya se había introducido.")
        if letra not in letrasrepetidas:
            letrasrepetidas.append(letra)
    else:
        milista.append(letra)
    respuesta=input("¿Deseas repetir? (si/no): ")
    if respuesta=="si":
        break
print("Letras introducidas:", milista)
print("Letras repetidas:", letrasrepetidas)


