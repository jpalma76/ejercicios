let arreglo3 = []
    function juntarArreglos(arr1, arr2) {
        arr1.shift()
        arr2.shift()
        arreglo3 = arr1.concat(arr2)
        console.log(arreglo3); 
}

juntarArreglos([1, 2, 3], [4, 5, 6]) // [2, 3, 5, 6]
juntarArreglos(["hola", "mundo"], ["desde", "javascript"]) // ["mundo", "javascript"]