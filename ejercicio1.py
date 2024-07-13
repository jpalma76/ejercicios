'''
edad = 18
print("Eres mayor de edad") if edad >= 18 else print("Eres menor de edad")

codigo = "1234"
# Escribe tu código aquí 
print("Código correcto") if codigo == "1234" else ("Código incorrecto")
# Fin 

def a_mayusculas(texto1,texto2):
    nueva_palabra= texto1+texto2
    return nueva_palabra.upper()

# Fin
print(a_mayusculas("hola", "mundo"))
print(a_mayusculas("cat", "Dog"))
print(a_mayusculas("King", "kong"))


def limpiar_y_mayusculas(texto1,texto2):
    nuevo_texto=texto1.strip()+texto2.strip()
    return nuevo_texto.upper()

# Fin
print(limpiar_y_mayusculas("  hola","mundo"))
print(limpiar_y_mayusculas("vaso ","  agua"))
print(limpiar_y_mayusculas("sal  ","    pimienta"))

def eliminar_especial(lista):
    if len(lista) > 5:
        lista_modificada = lista.pop()
        return lista_modificada
    elif len(lista) == 5:
        lista_modificada = lista.pop(1)
        return lista_modificada
    else:
        return lista

print(eliminar_especial([10, 20, 30, 40, 50, 60]))
print(eliminar_especial(["manzana", "pera", "uva", "naranja", "kiwi"]))
print(eliminar_especial([1, "dos", 3.0, "cuatro"]))
'''

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1.extend(lista2) #Esto está mal
#al utilizar el método extend se están agregando 
# los elementos a la lista 1,
print(lista1)