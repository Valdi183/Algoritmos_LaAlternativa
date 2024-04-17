"""
Este algortimo calcula el importe del descuento de una compra dada, si la compra supera ciertos importes, el descuento será mayor.
El algoritmo toma como entrada el precio de la compra, que es el precio que ponga el usuario (puede ser decimal), y devuelve el
importe del descuento en función de lo pagado
"""

def calcular_descuento(precio: float) -> float:
    if precio < 100:
        # No hay descuento para precios inferiores a 100 €
        return 0.0
    elif precio < 500:
        # Descuento del 5 % para precios entre 100 € y 500 €
        return precio * 0.05
    else:
        # Descuento del 8 % para precios superiores a 500 €
        return precio * 0.08

# Ejemplo de uso
precio_compra = float(input("Ingrese el importe de la compra en euros: "))
descuento = calcular_descuento(precio_compra)
print("El importe del descuento es:", descuento, "€")