"""
Este algoritmo calcula la prima anual en función del número de accidentes,la distancia recorrida 
y la antigüedad del conductor, tomando estos parametros como entrada. Por último devuelve
la prima anual calculada
"""
def calcular_prima_anual(accidentes, distancia, antiguedad):
    # Calcula la prima de antigüedad
    if antiguedad < 4:
        prima_antiguedad = 0.00
    else:
        prima_antiguedad = 200.00 + (antiguedad - 4) * 20.00

    # Calcula la prima de distancia
    prima_distancia = min(distancia * 0.01, 400.00)

    # Calcula la prima anual
    if accidentes > 3:
        prima_anual = 0.00
    else:
        prima_anual = (prima_antiguedad + prima_distancia) / (accidentes + 1)

    return prima_anual

# Ejemplo de uso
accidentes = int(input("Introduzca el numero de accidentes que tuvo el conductor: "))
distancia = int(input("Introduzca la distancia total recorrida por el conductor en kilometros: "))
antiguedad = int(input("Introduzca los años de antigüedad: ")) 

# Calcula la prima anual
prima = calcular_prima_anual(accidentes, distancia, antiguedad)

# Muestra la prima anual
print("La prima anual del conductor es:", prima, "€")