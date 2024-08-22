var alphabet = {
    'a': '.-',    'b': '-...',  'c': '-.-.', 'd': '-..',
    'e': '.',     'f': '..-.',  'g': '--.',  'h': '....',
    'i': '..',    'j': '.---',  'k': '-.-',  'l': '.-..',
    'm': '--',    'n': '-.',    'o': '---',  'p': '.--.',
    'q': '--.-',  'r': '.-.',   's': '...',  't': '-',
    'u': '..-',   'v': '...-',  'w': '.--',  'x': '-..-',
    'y': '-.--',  'z': '--..',  
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----', ' ': '/'
}

function changeToMorse(texto,alphabet,char) {
    let morseText = ""
    let text = texto.toLowerCase().split("")
    if (text == " ") {
        text = "/"
    }
    return text
}

//changeToMorse("Hola mundo")
console.log(changeToMorse("Hola mundo"))
/*
herramientas de ciberseguridad
chekmark
acunetix
tenable
nessus 
rapid7
vicarius
fortinet
*/