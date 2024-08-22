def descuentos(cantidad, hora):
    if hora == "Mañana":
        if cantidad < 3:
            return  "Sin descuento en la compra matutina."
        if cantidad >= 5 and cantidad < 10:
            return "Descuento del 15% en la compra matutina."
        if cantidad >= 10:
            return "Descuento del 25% en la compra matutina."
    if hora == "Noche":
        if cantidad < 3:
            return "Sin descuento en la compra nocturna."
        if cantidad >= 3 and cantidad < 5:
            return "Descuento del 3% en la compra nocturna."
        if cantidad >=5 and cantidad < 10:
            return "Descuento del 5% en la compra nocturna."
        if cantidad >= 10:
            return "Descuento del 15% en la compra nocturna."


print(descuentos(15, 'Mañana'))
print(descuentos(2, 'Mañana'))
print(descuentos(5, 'Noche'))
print(descuentos(4, 'Noche'))