nombres = ["ana", "luis", "jose", "rosa", "julio"] // ["Ana", "Luis", "Jose", "Rosa", "Julio"]
function capitalizarNombres(nombres) {
    for (let i = 0; i < nombres.length; i++) {
        const primeraLetra = nombres[i][0].toUpperCase()
        const resto = nombres[i].slice(1)
        nombres[i] = primeraLetra + resto            
    }
    return nombres
}

console.log(capitalizarNombres(nombres));

