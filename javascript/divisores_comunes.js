function divisores_comunes(num1, num2) {
    numero = num1
    while(numero <= num1 && numero <= num2){
        if(numero % num1 == 0){
            console.log(numero);
        }
        numero++
    }
}

divisores_comunes(10, 20)  // 1, 2, 5, 10
divisores_comunes(15, 30)  // 1, 3, 5, 15