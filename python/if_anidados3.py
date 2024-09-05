def revisar_antes_de_salir(llaves, celular):
# primero preguntas si ambas condiciones son True
    if llaves and celular: # Si ambas son True
        return  "Todo listo, puedes salir de casa"
    elif: #si no haz esto
        return "Te falta el celular"
    else: #si no haz esto otro
        return "Te falta las llaves"

"""
pero aquí el problema es que preguntas si ambas condiciones son True haz una cosa
y si no, es decir, "lo contrario" o sea que llaves y celular son False has esto otro
y después preguntas lo contrario de ambas condiciones, ** esto es lógicamente imposible **
porque solo existen True o False.
"""



print(revisar_antes_de_salir(True, True))
print(revisar_antes_de_salir(True, False))
print(revisar_antes_de_salir(False, True))
print(revisar_antes_de_salir(False, False))