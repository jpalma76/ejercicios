def divisores_comunes(num1, num2):
    contador = 1
    while contador <= num1:
        if num1 % contador == 0 and num2 % contador == 0:
            print(contador)
        contador = contador + 1

divisores_comunes(10, 20)
divisores_comunes(15, 30)


  # 1, 2, 5, 10
  # 1, 3, 5, 15