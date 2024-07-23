let arreglo = [1,2,3,4,5,6,7,9]

function contarImpares(arreglo) {
    let contador = 0
    for(let i = 0; i < arreglo.length; i++) {
        let numero = arreglo[i]
        if(numero%2 > 0) {
            console.log(arreglo[i]);
        }
    }
}

contarImpares(arreglo)
