import os



def funcion1():
    # Limpiar pantalla
    os.system('cls')
    print("Dame dos números para sumar: ")
    num1 = int(input("Primer numero: "))
    num2 = int(input("Segundo numero: "))
    print("Suma de {} + {} es igual a {}".format(num1,num2, num1 + num2))

def funcion2():
    os.system('cls')
    print("Dame dos números para restar: ")
    num1 = int(input("Primer numero: "))
    num2 = int(input("Segundo numero: "))
    print("Resta de {} - {} es igual a {}".format(num1,num2, num1 - num2))
    

def funcion3():
    os.system('cls')
    print("Dame dos números para multiplicar: ")
    num1 = int(input("Primer número: "))
    num2 = int(input("Segundo número: "))
    print("Multiplicación de {} * {} es igual a {}".format(num1,num2, num1 * num2))

def funcion4():
    os.system('cls')
    print("Dame dos números dividir: ")
    num1 = int(input("Primer número: "))
    num2 = int(input("Segundo número: "))
    print("División de {} / {} es igual a {}".format(num1,num2, num1 / num2))


def run():
    while True:
        print("\nMenú de opciones: ")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        opcion = int(input("\nIngrese la opción seleccionada: "))
        if opcion == 1:
            funcion1()
        if opcion == 2:
            funcion2()
        if opcion == 3: 
            funcion3()
        if opcion == 4: 
            funcion4()
        if opcion == 5: 
            break

if __name__ == "__main__":
    run()
