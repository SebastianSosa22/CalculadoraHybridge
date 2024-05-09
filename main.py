from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada


def menu():
    print("Calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Suma avanzada")
    print("6. Salir")
    opcion = int(input("Elija una opción: "))
    return opcion


def main():
    while True:
        opcion = menu()
        if opcion == 1:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("Resultado:", sumar(a, b))
        elif opcion == 2:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("Resultado:", restar(a, b))
        elif opcion == 3:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("Resultado:", multiplicar(a, b))
        elif opcion == 4:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("Resultado:", dividir(a, b))
        elif opcion == 5:
            numeros = map(float, input(
                "Ingrese los números separados por espacio: ").split())
            print("Resultado:", suma_avanzada(*numeros))
        elif opcion == 6:
            print("Gracias por usar la calculadora.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()
