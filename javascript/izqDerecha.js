function izqDerecha(arr, num) {
    if(num<100) {
        arr.push(num)
    } else {
        arr.unshift(num)
    }
    console.log(arr);
}

izqDerecha([1,2,3,4], 5) // [1,2,3,4,5]
izqDerecha([1,2,3,4], 100) // [100,1,2,3,4]
izqDerecha([1,2,3,4], 101) // [101,1,2,3,4]