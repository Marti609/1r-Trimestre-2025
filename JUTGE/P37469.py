n=int(input())
hores = n // 3600      
minuts = (n % 3600) // 60         
segons = n % 60
print(f"{hores} {minuts} {segons}")