N1 = int(input("Digite el primer digito del rango: "))
N2 = int(input("Digite el ultimo digito del rango: "))

def contar_pares_impares(N1, N2):
    pares = 0
    impares = 0

    for numero in range(N1, N2 + 1):
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    return pares, impares

pares, impares = contar_pares_impares(N1, N2)

print(f"en el rango de{N1} a {N2}: ")
print(f"Hay {pares} numeros pares.")
print(f"Hay {impares} numeros impares.")