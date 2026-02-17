a, b=map(int, input().split()) 
if b == 0:
    print("No es pot dividir per 0")
elif b>0:
    cocient, resto = divmod(a, b)
    print(f"{cocient} {resto}")
