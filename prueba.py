N1 = int(input("Digite el primer valor: ")) 
N2 = int(input("Digite el segundo valor: "))

opcion = 0
while True:
    print("""
    Hola, ¿Qué quieres hacer?

    1) Sumar los valores.
    2) Restar los valores.
    3) Multiplicar los valores.
    4) Dividir los valores.
    5) Calcular el porcentaje del primer valor respecto al segundo.
    6) Cambiar los valores elegidos.
    7) Cerrar el programa.
    """)

    opcion = int(input("¡Elija una opción! "))

    if opcion == 1:
        resultado = (N1 + N2)
        print("El resultado de su suma es: ", resultado)

    elif opcion == 2:
        resultado = (N1 - N2)
        print("El resultado de su resta es: ", resultado)

    elif opcion == 3:
        resultado = (N1 * N2)
        print("El resultado de la multiplicación es: ", resultado)

    elif opcion == 4:
        if N2 != 0:
            resultado = (N1 / N2)
            print("El resultado de la división es: ", resultado)
        else:
            print("SINTASIXERROR: No se puede dividir entre cero.")

    elif opcion == 5:
        if N2 != 0:
            porcentaje = ((N1 / N2) * 100)
            print(f"El {N1} es el {porcentaje:.2f}% de {N2}.")
        else:
            print("SINTASIXERROR: No se puede calcular el porcentaje con un divisor cero.")

    elif opcion == 6:
        N1 = int(input("Digite el primer valor: "))
        N2 = int(input("Digite el segundo valor: "))

    elif opcion == 7:
        print("Cerrando el programa.")
        break

    else:
        print("SINTASIXERROR.")
