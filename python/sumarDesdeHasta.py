def sumarDesdeHasta(num1,num2):
    suma = 0
    incremento = num1
    while(incremento <= num2):
        suma += incremento
        incremento += 1
    return suma


print(sumarDesdeHasta(1, 5))
print(sumarDesdeHasta(10, 20))
print(sumarDesdeHasta(100, 200))
 # 15
 # 165
 # 15150