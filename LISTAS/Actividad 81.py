#81. A partir de una lista definida, busca el método apropiado para que se visualice un valor de la lista al azar.
import random

lista=["casa", "balcon", "hola", "fuster", "torre"]
valor_aleatorio=random.choice(lista)

print(valor_aleatorio)