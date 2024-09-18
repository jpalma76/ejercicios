def cancion_elefantes():
    numero_elefantes = 1
    
    while numero_elefantes <= 10:
        if numero_elefantes == 1:
            print(f"{numero_elefantes} elefante se balanceaba sobre la tela de una araña, como veía que resistía, fue a llamar a otro elefante.")
        else:
            print(f"{numero_elefantes} elefantes se balanceaban sobre la tela de una araña, como veían que resistía, fueron a llamar a otro elefante.")
        
        numero_elefantes += 1

# Llamamos a la función para mostrar la canción
cancion_elefantes()