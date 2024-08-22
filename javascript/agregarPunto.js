original = [4, 5, 7, 2, 3]

function agregarPunto(original) {
    for (let i = 0; i < original.length; i++) {
        original[i] = original[i]+1;
    }
    return
}
agregarPunto(original)
console.log(original) // [5, 6, 8, 3, 4]