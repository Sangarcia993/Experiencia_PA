import random
def cachipun(jugador,computador):
    if jugador==1:
        if computador==2:
            print("Ganó el computador")
        elif computador==3:
            print("Ganó el jugador")
        else:
            print("Empate")
    elif jugador==2:
        if computador==3:
            print("Ganó el computador")
        elif computador==1:
            print("Ganó el jugador")
        else:
            print("Empate")
    else:
        if computador==1:
            print("Ganó el computador")
        elif computador==2:
            print("Ganó el jugador")
        else:
            print("Empate")
    
    pass
jugador=int(input("Cachipun (1 es piedra, 2 es papel, 3 es tijera) "))
computador=random.randint(1,3)
print("El computador escogio",computador)
cachipun(jugador,computador)
