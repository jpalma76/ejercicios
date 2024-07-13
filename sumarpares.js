function sumarPares(arreglo) {
    let suma = 0        
    for (let i = 0; i < arreglo.length; i++) {
        if(arreglo[i]%2 == 0) {
            suma += arreglo[i]
        }
    }
    return suma
}

console.log(sumarPares([1, 2, 3, 4, 5]));
console.log(sumarPares([10, 20, 30, 40, 50, 60, 70]));
 // 6
 // 150