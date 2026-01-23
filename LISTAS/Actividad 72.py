#72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y no deben almacenarse en la lista
def normalizar(letra):
    letra=letra.lower()  
    reemplazos={'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    return reemplazos.get(letra, letra)  

letrasnuevas=[]
letrasrepetidas=[]

while True:
    letra=input("Introduce una letra: ").strip()
    if len(letra)==1:
        print("Introduce solo una letra .")
    letranormal=normalizar(letra)
    if letranormal in letrasnuevas:
        print(f"La letra {letra} ya se había introducido.")
        if letranormal not in letrasrepetidas:
            letrasrepetidas.append(letranormal)
    else:
        letrasnuevas.append(letranormal)
    respuesta= input("¿Deseas repetir? (si/no): ").lower()
    if respuesta=='si':
        break

print(f"Letras introducidas: {letrasnuevas}")
print(f"Letras repetidas: {letrasrepetidas}")