#83. Modifica el código del ejercicio anterior para que el programa permita repetir x partidas (hasta que el usuario lo decida). Tienes que controlar una puntuación de cada partida de la siguiente manera, si la palabra la aciertas a la primera son 8 puntos, si la aciertas a la segunda 7 puntos y así sucesivamente.
import random

lista=["casa", "balcon", "hola", "fuster", "torre"]
palabra_random=random.choice(lista)
intento=input("Introduce la palabra secreta: ")
puntuacion=0

if intento==palabra_random:
    print("Acertaste")
else:
    print("Sigue jugando")
    while intento!=palabra_random:
        intento=input("Introduce la palabra secreta: ")
        if intento==palabra_random:
            print("Acertaste")
            break
        else:
            print("Sigue jugando")
respuesta=input("Deseas repetir si/no: ")

while respuesta=="si":
    import random

    lista=["casa", "balcon", "hola", "fuster", "torre"]
    palabra_random=random.choice(lista)
    intento=input("Introduce la palabra secreta: ")
    puntuacion=0

    if intento==palabra_random:
        print("Acertaste")
    else:
        print("Sigue jugando")
    while intento!=palabra_random:
        intento=input("Introduce la palabra secreta: ")
        if intento==palabra_random:
            print("Acertaste")
            break
        else:
            print("Sigue jugando")
    respuesta=input("Deseas repetir si/no: ")
