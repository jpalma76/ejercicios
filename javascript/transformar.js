const precios = [1000, 750, 950, 1100, 1300]

function transformar(precios) {
    let nuevoValor = 0
    for (let i = 0; i < precios.length; i++) {
        nuevoValor = precios[i] * 1.2
        
        if (nuevoValor > 1000) {
            console.log(nuevoValor);
        }
        
    }
}

transformar(precios);



