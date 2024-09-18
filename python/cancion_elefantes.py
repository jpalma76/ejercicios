def cancion_elefantes():
    contador = 1
    animal = "elefante"
    var1 = "balanceaba"
    var2 = "veía"
    var3 = "fué"
    while contador <=10:
        if contador > 1:
            animal = "elefantes"
            var1 = "balanceaban"
            var2 = "veían"
            var3 = "fueron"

        print(f"{contador} {animal} se {var1} sobre la tela de una araña, como {var2} que resistía, {var3} a llamar a otro elefante")
        contador = contador + 1

cancion_elefantes()
