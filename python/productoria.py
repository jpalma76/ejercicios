def productoria(numero):
    factor = 1
    incremento = 1
    while incremento <= numero:
        factor = factor * incremento
        incremento = incremento + 1
    return factor

print(productoria(9))
print(productoria(12))
print(productoria(7))

#print(1*2*3*4*5*6*7*8*9)