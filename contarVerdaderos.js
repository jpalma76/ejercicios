function contarVerdaderos(arreglo) {
    let contador = 0
    for (let i = 0; i < arreglo.length; i++) {
        let elemento = arreglo[i];
        if(elemento) {
            contador++
        }
    }
    console.log(contador)
}

contarVerdaderos([0, 1, "", "Hola", null, undefined, false, true, {}, [], "0"]) // 6
