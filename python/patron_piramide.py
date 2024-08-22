def patron_estrellas(n):
    fila = 1
    string = ""
    while fila <= n:
        string = string + "*"
        print(string)
        fila += 1

patron_estrellas(4)
patron_estrellas(7)
patron_estrellas(2)