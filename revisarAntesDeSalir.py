def revisarAntesDeSalir(llaves, celular):
    if llaves == "Si":
        if celular == "Si":
            return "Todo listo, puedes salir de casa"
        else:
            return "Te falta el celular"
    else:
        return "Te falta las llaves"
    