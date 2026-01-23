#80. Utilizando listas, crea un programa que te permita determinar si un número es decimal o no. 
valor=int(input("Introduce un numero: "))

if isinstance(valor, float):
    print(f"es decimal {valor}")
elif isinstance(valor, int):
    print(f"es entero {valor}")

