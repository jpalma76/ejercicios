function juntarElementos(arr1, num, arr2) {
    return arr1.concat([num],arr2)
}

console.log(juntarElementos([10, 20, 30], 40, [50, 60, 70]));
console.log(juntarElementos(["a", "b", "c"], 100, ["d", "e", "f"]));