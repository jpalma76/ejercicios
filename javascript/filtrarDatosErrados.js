/* Por fallas en el disco duro, algunos datos del sistema se corrompieron y por algún motivo ahora pueden empezar con 2. Modifica la función anterior llamada filtrarDatosErrados para que pueda filtrar los datos que empiecen con 2 o que tengan una mayor cantidad de caracteres que 8. La función debe retornar un arreglo que contenga únicamente los datos que no estén errados. */

datos = ["20010000", "00000001", "100000000", "1100000010", "00000000", "20000001", "00000000", "100000010"]

function filtrarDatosErrados(datos) {
    let nuevoArreglo = []
    // iteracion de array
    for (let i = 0; i < datos.length; i++) {
        let largoElemento = datos[i].length
        let primerCaracter = datos[i][0]
        if(primerCaracter != 2 || largoElemento == 8) {
            nuevoArreglo.push(datos[i]);
        }
    }
    return nuevoArreglo;
}


console.log(filtrarDatosErrados(datos)) /* ["00000001", "00000000", "00000001", "00000000"] */

/* Largo de cada elemento del array
let largoElemento=datos[i].length
let primerCaracter = datos[i][0] */