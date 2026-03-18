import random
import time
tiempo = time.time()
historial_ganadas = []
historial_perdidas = []
lista_palabras = ["python", "programacion", "ahorcado", "desarrollo", "inteligencia", "computadora", "juego", "palabra", "adivinar", "letra"]
intentos = 8
aciertos = []
fallos = []
print("¡Bienvenido al juego del Ahorcado! Tienes 8 intentos para adivinar la palabra oculta.")
time.sleep(2)
palabra = random.choice(lista_palabras)
tablero = ""
for l in palabra:       
    if l in aciertos:
        tablero += l + " "
    else:
        tablero += "_ "

while intentos > 0:
    print(f"{intentos} intentos restantes")
    print(tablero)

    letra = input("Adivina una letra: ").lower()

    if len(letra) != 1 or not letra.isalpha():
        print("Introduce solo una letra.")
        continue

    if letra in aciertos or letra in fallos:
        print("Ya has usado esa letra. Intenta con otra.")
        continue

    if letra in palabra:
        print("¡Correcto!")
        aciertos.append(letra)

        tablero = ""
        for letra_palabra in palabra:
            if letra_palabra in aciertos:
                tablero += letra_palabra + " "
            else:
                tablero += "_ "
    else:
        print("¡Incorrecto!")
        fallos.append(letra)
        intentos -= 1

    if all(letra in aciertos for letra in palabra):
        print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
        print(f"Fallos: {fallos}")
        print(f"Aciertos: {aciertos}")
        historial_ganadas.append(palabra)
        fin = time.time()  
        print(f"Tiempo transcurrido: {fin - tiempo:.2f} segundos")
        break

else:
    print(f"Fallos: {fallos}")
    print(f"Aciertos: {aciertos}")
    print(f"Has perdido. La palabra era: {palabra}")
    historial_perdidas.append(palabra)
    fin = time.time()  
    print(f"Tiempo transcurrido: {fin - tiempo:.2f} segundos")

respuesta_historial = input("¿Quieres ver tu historial de partidas s/n? ").lower()

if respuesta_historial == "s":
    print(f"Palabras acertadas: {historial_ganadas}")
    print(f"Palabras perdidas: {historial_perdidas}")
        
respuesta = input("Quieres jugar otra partida s/n? ").lower()

while respuesta == "s":
    juego_complicado = input("¿Quieres jugar una partida complicada s/n? ").lower()
    if juego_complicado == "s":
        intentos = 4
        print("¡Modo difícil! Tienes 4 intentos.")
    else:
        intentos = 8
        print("Modo normal. Tienes 8 intentos.")
    tiempo = time.time()
    aciertos = []
    fallos = []
    palabra = random.choice(lista_palabras)
    tablero = ""
    for l in palabra:       
        if l in aciertos:
            tablero += letra + " "
        else:
            tablero += "_ "

    while intentos > 0:
        print(f"{intentos} intentos restantes")
        print(tablero)
        letra = input("Adivina una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Introduce solo una letra.")
            continue

        if letra in aciertos or letra in fallos:
            print("Ya has usado esa letra.")
            continue

        if letra in palabra:
            print("¡Correcto!")
            aciertos.append(letra)
            tablero = ""
            for letra_palabra in palabra:
                if letra_palabra in aciertos:
                    tablero += letra_palabra + " "
                else:
                    tablero += "_ "
        else:
            print("¡Incorrecto!")
            fallos.append(letra)
            intentos -= 1

        if all(letra in aciertos for letra in palabra):
            print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
            historial_ganadas.append(palabra)
            break
    else:
        print(f"Has perdido. La palabra era: {palabra}")
        historial_perdidas.append(palabra)

    respuesta_historial = input("¿Quieres ver tu historial s/n? ").lower()
    if respuesta_historial == "s":
        print(f"Palabras acertadas: {historial_ganadas}")
        print(f"Palabras perdidas: {historial_perdidas}")
            
    respuesta = input("Quieres jugar otra partida s/n? ").lower()
print("¡Hasta la próxima!")
