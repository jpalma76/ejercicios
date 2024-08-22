function espejo(texto) {
    let arreglo = texto.split("")
    let mitad = arreglo.length/2
    let mitad1 = texto.substring(0,mitad)
    let mitad2 = texto.substring(mitad)
    if (mitad1 == mitad2) {
        return true
    }else {
        return false
    }
    return 
}

console.log(espejo("HolaHola"))