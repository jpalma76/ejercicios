def cuadrado_relleno(n):
    columna = 0
    fila = 0
    string = ''
    while fila < n:
        while columna < n:
            string = string + "*"
            columna += 1
        print(string)
        fila += 1

cuadrado_relleno(5)