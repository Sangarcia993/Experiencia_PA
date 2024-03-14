from random import *

def adivinar_par_o_impar():
    intentos = 0
    correctos = 0
    while True:
        intentos += 1

        numeroviejo = randint(1, 100000000)
        numero = numeroviejo

        if numero % 2 == 0:
            numero =  2
        else:
            numero = 1

        print("Crees que el numero es par (2) o impar (1)? (quit para salir del juego)")
        usuario = input(">>> ")

        if usuario == "quit":
            break
        else:
            usuario = int(usuario)
        
        if usuario == numero:
            print("Felicitaciones, adivinaste correctamente!!!")
            correctos += 1
        else:
            print("Lo siento, :(, no adivinaste la paridad correcta del numero")
        print("El numero era:", numeroviejo)
        
        print("")
        print("Adivinaste correctamente:", correctos)
        print("Intentos:", intentos)
        print("Porcentaje:", str((correctos/intentos)*100) + "%")
        print(f"Intenta llegar a un 60% o mas con un minimo de 5 intentos!")



    pass