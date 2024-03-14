import random, time
def juego_del_dado():
    print("Hola! Bienvendio al juego de dado donde lo mas importante es ser habil al momento de apretar enter\n")
    turno = 0

    TotalP = 0
    TotalC = 0

    while True:
        if turno == 0:
            lol = input("Te toca tirar el dado... Vamos! Apreta enter")

            numero = random.randint(1, 6)
            TotalP += numero

            print("Has tirado el dado:")
            print("-------")
            print("| ", numero," |")
            print("-------")

            print("\nTu total es:", TotalP)
            print("Total del computador es:", TotalC)
            print("Ahora le toca al computador")
            turno += 1
        else:
            turno -= 1
            print("\n\nVOY A TIRAR EL DADO")
            numero = random.randint(0, 10)
            for i in range(numero):
                print(f"." * i, end="\r")
                time.sleep(1)
            
            numero = random.randint(1, 6)
            TotalC += numero

            print("He tirado el dado:")
            print("-------")
            print("| ", numero," |")
            print("-------")

            print("\nTu total es:", TotalP)
            print("Total del computador es:", TotalC)
            print("")
        
        if TotalC >= 30:
            time.sleep(2)
            print("Ha ganado el computador!!")
            break
        elif TotalP >= 30:
            time.sleep(2)
            print("Has ganado TU!!! Ha que ha tomado mucha habilidad...")
            break
    pass