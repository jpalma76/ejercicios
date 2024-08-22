function rotarALaDerecha(arreglo) {
    let ultimo = [arreglo.pop()]
    console.log(ultimo.concat(arreglo))
}
/* Fin */
console.log(rotarALaDerecha([5, 6, 7, 8, 9]));
console.log(rotarALaDerecha(['a', 'b', 'c', 'd', 'e'])); 