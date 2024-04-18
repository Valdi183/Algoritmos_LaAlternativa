"""
Este algoritmo, calcula el importe del descuento en función del numero de niños de la familia
por entrar al Parque Warner de Madrid. El algoritmo toma como entrada el precio total que ha
pagado la familia, y devuelve el dinero que se le descuenta a la familia, según los criterios
establecidos para aplicar un descuento u otro       
"""

def calcular_descuento(precio_total, cantidad_niños):
    if cantidad_niños == 2:
        return precio_total * 0.10  # 10 % de descuento para 2 niños
    elif cantidad_niños == 3:
        return precio_total * 0.15  # 15 % de descuento para 3 niños
    elif cantidad_niños == 4:
        return precio_total * 0.18  # 18 % de descuento para 4 niños
    elif cantidad_niños >= 5:
        # 18 % de descuento + 1 % adicional por cada niño por encima de 4
        return precio_total * (0.18 + (cantidad_niños - 4) * 0.01)
    else:
        return 0.0  # No hay descuento para menos de 2 niños
    
# Ejemplo de uso
precio_total = float(input("Ingrese el precio total pagado por la familia: "))
cantidad_niños = int(input("Ingrese el numero de niños que hay en la familia: "))

importe_descuento = calcular_descuento(precio_total, cantidad_niños)
print("El importe del descuento es de: ", importe_descuento)