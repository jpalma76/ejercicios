frutas = ["banana", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]

cadena = "Hola Dalto"
numeros = [2,5,8,10]

for fruta in frutas:
    print(f"me voy a comer una {fruta}")

print("")

#evitando que se coma una fruta con continue
for fruta in frutas:
    if fruta == "granada":
        continue
    print(f"me voy a comer una {fruta}")

print("")

#evitar que e bucle no siga ejecutandose (el else no se ejecuta)
for fruta in frutas:
    print(f"me voy a comer una {fruta}")
    if fruta == "pera":
        break
    else:
        print("bucle terminado")

#recorrer una cadena de texto
for letra in cadena:
    print(letra)

#for en una sola misma linea de codigo
"""numeros_duplicados = list()
for numero in numeros:
    numeros_duplicados.append(numero * 2) """
numeros_duplicados = [x*2 for x in numeros]

print(numeros_duplicados)