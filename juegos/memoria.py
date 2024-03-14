from random import *
import time

def memoria():
    lista = []
    while True:
        print("Bienvendio al juego de la memoria, donde la habilidad si importa (no como en otros juegos...)")
        dificul = int(input("Que dificultad quieres (escribe un numero del 1 al 100!!)\n>>> "))

        if dificul == 1:
            print("Fome")
            print("Si quieres jugar asi... Te deseo surte")
            lista = [randint(0, 100000000000)]
        else:
            for i in range(0, dificul):
                lista.append(randint(1, 100))

        listalinda = str(lista[0])
        lista.pop(0)
        for i in lista:
            listalinda = listalinda + " " + str(i)

        

        print("Atento a la lista de numeros!")

        
        timpo = [5, 4, 3, 2, 1]
        for i in range(0, 5):
            print(f"Lista en:", timpo[i], end="\r")
            time.sleep(1)
        
        if dificul != 1:
            for i in range(0, 5):
                print(f"Aqui esta la lista ({timpo[i]}):", listalinda, end="\r")
                time.sleep(1)
        else:
            for i in range(0, 5):
                print(f"Aqui esta la lista ({timpo[i]}):", listalinda, end="\r")
                time.sleep(0.3)
        
        print("Listo, cual era la lista? (escribe los numero separado por 1 espacio)")
        respuesta = input(">>> ")
        if respuesta == listalinda:
            print("Felicitaciones, quieres volver a jugar (si o no)")
            seguitr = input(">>> ")
            if seguitr == "si":
                lista = []
            else:
                break
        else:
            print("Pucha :( esa no era la lista, la lista era:", listalinda)
            print("Quieres volver a jugar? (si o no)")
            seguitr = input(">>> ")
            if seguitr == "si":
                lista = []
            else:
                break
    pass