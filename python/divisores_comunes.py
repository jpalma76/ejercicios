'''crea una funcion que recina 2 numeros y que reciba los divisores comunes de ambos numeros'''

def divisores_comunes(num1, num2):
   contador = 1
   while contador <= num2:
        if contador % num1 == 0:
            print(contador)
        num1 += 1

divisores_comunes(10, 20)  # 1, 2, 5, 10
#divisores_comunes(15, 30)  # 1, 3, 5, 15

