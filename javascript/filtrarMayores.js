
function filtrarMayoresA(arreglo, numero) {
    let nuevoArreglo=[]
    for (let i = 0; i < arreglo.length; i++) {
        if(arreglo[i] > numero) {
            nuevoArreglo.push(arreglo[i])
        }   
    }
    return nuevoArreglo
}

console.log(filtrarMayoresA([2,4,3,6],4));
console.log(filtrarMayoresA([-1,-8,0,3],5));