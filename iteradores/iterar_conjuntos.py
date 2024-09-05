animales = {"gato", "perro", "loro", "cocodrilo"}
numeros = {52,16,14,72}

for animal in animales:
    print(f"Ahora la variable animal es igual a: {animal}")

for numero in numeros:
    resultado = numero * 10
    print(resultado)

for numero,animal in zip(animales,numeros):
    print(f"recorriendo a conjunto 1: {animal}")
    print(f"recorreindo la conjunto 2: {numero}")

for num in range(5,10):
    print(num)

#forma correcta de rrecorrer una conjunto con su índice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el valor es: {valor}")

#usando el for/else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print(f"el bucle termino")

#todo los anterior funciona exactamente igual para tuplas, listas y conjuntos