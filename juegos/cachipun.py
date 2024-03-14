import random



def cachipun():
    intentos = 0
    correctos = 0

    while True:
        intentos += 1
        jugador=(input("Cachipun (1 es piedra, 2 es papel, 3 es tijera, quit para salir del juego) \n>>> "))

        if jugador == "quit":
            break
        else:
            jugador = int(jugador)

        computador=random.randint(1,3)
        print("El computador escogio",computador, "\n")

        if jugador==1:
            if computador==2:
                print("Ganó el computador")
            elif computador==3:
                print("Ganó el jugador")
                correctos += 1
            else:
                print("Empate")
        elif jugador==2:
            if computador==3:
                print("Ganó el computador")
            elif computador==1:
                print("Ganó el jugador")
                correctos += 1
            else:
                print("Empate")
        else:
            if computador==1:
                print("Ganó el computador")
            elif computador==2:
                print("Ganó el jugador")
                correctos += 1
            else:
                print("Empate")
        
        print("")
        print("Victorias:", correctos)
        print("Intentos:", intentos)
        print("Porcentaje:", str((correctos/intentos)*100) + "%")
        print(f"Intenta llegar a un 40% o mas con un minimo de 5 intentos!\n")
        
        

