function transformarCostos(pesos, costoPorKg) {
    for (let i = 0; i < pesos.length; i++) {
        pesos[i] = parseFloat(pesos[i])*costoPorKg
    } 
    return pesos
}

pesos = ["0.25 kg", "0.75 kg", "1.25 kg", "1.75 kg"]
costoPorKg = 2
transformarCostos(pesos, costoPorKg)
console.log(pesos) // [0.5, 1.5, 2.5, 3.5]