import random
def adivinar_numero():
    computador = random.randint(1,10)

    while True:
        jugador=(input("Adivina el numero del computador (para salir del juego: quit)\n>>> "))

        if jugador == "quit":
            break
        else:
            jugador = int(jugador)

        if computador==jugador:
            print("Si era el numero, felicitaciones\nSigamos jugnado!2")
            computador = random.randint(1,10)
        else:
            print("Intenta denuevo, tu puedes!")
        pass

