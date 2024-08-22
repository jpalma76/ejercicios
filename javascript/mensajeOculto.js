function mensajeOculto(arreglo) {
    let palabra = ""
    for (let i = 0; i < arreglo.length; i++) {
        palabra +=arreglo[i][0]
    }
    return palabra
}

mensajeOculto(["Gallina", "Abeja", "Tigre", "Oso"])
mensajeOculto(["Música", "Isla", "Sol", "Tren", "Elefante", "Ratón", "Iguana", "Oso"])
mensajeOculto(["Luna", "Loro", "Avión", "Vaca", "Elefante"])


