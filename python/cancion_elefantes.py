def cancion_elefantes():
    animal=1
    while animal <= 10:
        if animal > 1:
            var1="balanceaban"
            var2="fueron"
            var3="veían"
        else:
            var1="balanceaba"
            var2="fue"
            var3="veía"
        ##          un     elefante   valanceaba como veía que resitía fue a buscar a otro elefante
        print(f"{animal} se {var1} sobre la tela de una araña, como {var3} que resistía {var2} a buscar a otro elefante")
        animal = animal + 1

cancion_elefantes()
