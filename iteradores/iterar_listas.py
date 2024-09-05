animales = ["gato", "perro", "loro", "cocodrilo"]
numeros = [52,16,14,72]

""" for animal in animales:
    print(f"Ahora la variable animal es igual a: {animal}")

for numero in numeros:
    resultado = numero * 10
    print(resultado)

for numero,animal in zip(animales,numeros):
    print(f"recorriendo a lista 1: {animal}")
    print(f"recorreindo la lista 2: {numero}")

for num in range(5,10):
    print(num)

#forma no óptima de recorrer una lista
for num in range(len(numeros)):
    print(numeros[num])

#forma correcta de rreccorrer una lista con su índice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el valor es: {valor}") """

#usando el for/else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print(f"el bucle termino")