import random
def adivinar_numero(computador,jugador):
    if computador==jugador:
        print("Si era el numero, felicitaciones")
    else:
        print("No")
    pass
computador=random.randint(1,10)
jugador=int(input("Adivina el numero del computador "))
adivinar_numero(computador,jugador)
print("El numero del computador era", computador)
