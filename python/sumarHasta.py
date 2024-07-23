def sumarHasta(numero):
    suma = 0
    contador = 0
    while (contador <= numero):
        suma += contador
        contador = contador + 1
    return suma

print(sumarHasta(4))
print(sumarHasta(11))
print(sumarHasta(2))
#12345 // 15