function revisarAntesDeSalir(llaves, celular) {
    if(llaves == true) {
        if (celular == true) {
            return "Todo listo, puedes salir de casa"
        } else {
            return "Te falta el celular"
        }
    } else {
        return "Te falta las llaves"
    }
}