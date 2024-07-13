def rotar_a_la_izquierda(lista):
    valor=lista[0]
    print(lista)
    lista.pop(0)
    print(lista)
    

rotar_a_la_izquierda([1, 2, 3, 4])  # [2, 3, 4, 1]

#print(rotar_a_la_izquierda(["Juan", "Pedro", "Ana", "Luis"]))  # ["Pedro", "Ana", "Luis", "Juan"]