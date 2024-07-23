function revisarAntesDeSalir(llaves,celular) {
    // se verifica si la primera condicion es verdadera
    if(llaves == "Si") {
        // se verifica si la segunda condicion es verdadera
        if(celular == "Si") {
            return "Todo listo, puedes salir de casa"
        } else { //sino de la segunda condicion
            return "Te falta el celular"
        }
        // sino de la primera condición
    } else {
        return "Te falta las llaves"
    }
}

function revisarAntesDeSalir(llaves, celular) {
    if(llaves == "Si" && celular  == "Si") {
        return "Todo listo, puedes salir de casa";
    } else if(llaves) {
        return "Te falta el celular";
    } else {
        return "Te falta las llaves";
    }
}
