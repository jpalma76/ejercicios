let temperaturas = [260, 280, 290, 310, 350]

function seleccionarTemperaturasExtremas(temperaturas) {
    for (let i = 0; i < temperaturas.length; i++) {
        let celcius = temperaturas[i] - 273;

        if (celcius < -10 || celcius > 40) {
            console.log(celcius)
        }            
    }
}

seleccionarTemperaturasExtremas(temperaturas)

