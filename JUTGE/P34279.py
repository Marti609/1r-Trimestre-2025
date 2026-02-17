hores, minusts, segons = map(int, input().split())
if hores>24 or minusts>60 or segons>60:
    print("Hora no vàlida")
else:
    segons_totals=segons+1
    if segons_totals == 60:
        segons_totals = 0
        minusts+=1
        if minusts == 60:
            minusts = 0
            hores+=1
            if hores == 24:
                hores = 0
    print(f"{hores:02d}:{minusts:02d}:{segons_totals:02d}")