"""
Este algoritmo calcula el descuento (en porcentaje) a aplicar según los criterios dados en el
ejercicio. EL algoritmo recoge como datos de entrda, la cantidad de componentes, y el tipo de
cliente. El algoritmo porcesa estos datos para calcular su decuento, y devuelve ese descuento
a aplicar según el caso.
"""

def calcular_descuento(cantidad_componentes, cliente):
    porcentaje_descuento_base = 0

    # Determina el porcentaje de descuento base según la cantidad de componentes pedidos
    if 10000 <= cantidad_componentes <= 20000:
        porcentaje_descuento_base = 0.10
    elif 20001 <= cantidad_componentes <= 40000:
        porcentaje_descuento_base = 0.15
    elif cantidad_componentes > 40000:
        porcentaje_descuento_base = 0.20

    # Aplica     ajustes al porcentaje de descuento base según el cliente
    if cliente == "COMMAQ":
        porcentaje_descuento_base -= 0.02  # Reducción del 2 % para COMMAQ
    elif cliente == "BEL":
        porcentaje_descuento_base += 0.01  # Mejora del 1 % para BEL

    return porcentaje_descuento_base

# Ejemplo de uso
cantidad_componentes = 30000  
cliente = "COMMAQ"

# Para llamar a la función con los parametros dados de forma mas breve
porcentaje_descuento = calcular_descuento(cantidad_componentes, cliente)

# Mostrar el porcentaje de descuento
print("El porcentaje de descuento concedido es:", porcentaje_descuento * 100, "%")