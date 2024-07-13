function mensajeOculto(arreglo) {
    let palabra = ""
    for (let i = 0; i < arreglo.length; i=i+2) {
        palabra +=arreglo[i][0]
    }
    console.log(palabra)
}

mensajeOculto(["Tronco", "Perro", "Oso", "Gato", "Perro", "Loro", "Onda"])
mensajeOculto(["Sol", "Oso", "Elefante", "Lana", "Casa", "Perro", "Rana", "Gato", "Estrella", "Cuerda", "Tigre"])
mensajeOculto(["Luna", "Loro", "Avión", "Vaca", "Nutria", "Oso", "Arbol"])