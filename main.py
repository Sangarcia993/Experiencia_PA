from juegos.adivinar_numero import adivinar_numero
from juegos.cachipun import cachipun
from juegos.memoria import memoria
from juegos.juego_del_dado import juego_del_dado
from juegos.adivinar_par_o_impar import adivinar_par_o_impar

def menu():
    juegos = {
        '1': cachipun,
        '2': adivinar_numero,
        '3': juego_del_dado,
        '4': adivinar_par_o_impar,
        '5': memoria
    }

    while True:
        print("\nMenú de juegos:")
        print("1. Cachipun")
        print("2. Adivinar número")
        print("3. Juego del dado")
        print("4. Adivinar par o impar")
        print("5. Memoria")
        print("6. Salir")
        opcion = input("Elige una opción: ")
        if opcion in juegos:
            juegos[opcion]()
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 6.")

if __name__ == "__main__":
    menu()