'''Crea una función llamada sumarDesdeHasta que reciba dos números como parámetros y retorne la suma de los números desde el primer número hasta el segundo número.'''

def sumarDesdeHasta(num1, num2):
    contador = num1
    while num1 <= num2:
        #contador = 1 / 2 / 3
        incremento = contador + 1 # 2 / 3 / 4
        suma = contador + incremento # 3 / 7
        num1 = num1 + 1
        contador = contador + 1 # 2 / 3
    return suma



    
print(sumarDesdeHasta(1, 5)) # 15
#print(sumarDesdeHasta(10, 20)) # 165
#print(sumarDesdeHasta(100, 200)) # 15150


