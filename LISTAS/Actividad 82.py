#82. Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine la palabra
import random

lista=["casa", "balcon", "hola", "fuster", "torre"]
palaba_random=random.choice(lista)
intento=input("Introduce la palabra secreta: ")

if intento==palaba_random:
    print("Acertaste")
else:
    print("Sigue jugando")
    while intento!=palaba_random:
        intento=input("Introduce la palabra secreta: ")
        if intento==palaba_random:
            print("Acertaste")
            break
        else:
            print("Sigue jugando")





            

