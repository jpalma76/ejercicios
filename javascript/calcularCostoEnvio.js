function calcularCostoEnvio(arreglo) {
    let costo = 0
    for (let i = 0; i < arreglo.length; i++) {
        costo += parseFloat(arreglo[i]) * 1.00
    }
    console.log(costo)
}

calcularCostoEnvio(["0.25 kg", "0.75 kg", "1.25 kg", "1.75 kg"])
calcularCostoEnvio(["1.25 kg", "1.75 kg", "2.25 kg"])
 // 4.00
// 5.25