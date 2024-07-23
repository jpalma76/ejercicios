def sumarDeDosEnDos(num1,num2):
    suma = 0
    incremento = num1
    while(incremento <= num2):
        suma += incremento
        incremento += 2
    return suma

print(sumarDeDosEnDos(5, 10))
print(sumarDeDosEnDos(10, 20))
print(sumarDeDosEnDos(3, 7))
 # 5 + 7 + 9 = 21
 # 10 + 12 + 14 + 16 + 18 + 20 = 90
 # 3 + 5 + 7 = 15