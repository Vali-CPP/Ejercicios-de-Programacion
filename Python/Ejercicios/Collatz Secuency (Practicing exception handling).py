
def Collatz(number):
    if (number % 2) == 0:
        number = number // 2
        print(number)
        if number != 1:
            Collatz(number)
        return number
    else:
        number = 3 * number + 1
        print(number)
        if number != 1:
            Collatz(number)
        return number



try:
    prueba = int(input("Ingrese un numero: "))
    Collatz(prueba)
except ValueError:
     print("Ingrese un entero por favor.")
