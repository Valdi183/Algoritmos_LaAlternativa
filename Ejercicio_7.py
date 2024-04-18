"""
Este script contiene varios algoritmos sencillos para calcular el coste de ciertas actividades
y uno ultimo que suma todos estos costes en uno para mostrar el precio total.
"""
"""
Anotación: aunque el ejercicio no lo pida, como se dan en el enunciado algunos datos que también dependen
de los dias que se utilice la actividad, como el precio de la comida o el alojamiento, se implementa una
función extra a ciertos algoritmos que lo requieran para que tengan en cuenta los dias.
"""
# Toma como entrada la cantidad de alumnos, y devuelve el precio a pagar por el trayecto de cada alumno
def calcular_coste_alumno_trayecto(cantidad_alumnos):
    if cantidad_alumnos <= 25:
        return 67.30
    else:
        return 61.00

# Recoge como entrada la cantidad de dias a utilizar este servicio, y devuelve el coste de la comida por alumno
def calcular_coste_alumno_comida(dias):
    return 3.50 * dias

# Toma como entrada la cantidad de alumno y los dias de estancia, y devuelve el precio a pagar por el alojamiento de cada alumno
def calcular_coste_alumno_alojamiento(cantidad_alumnos, dias):
    if cantidad_alumnos < 30:
        return 4.75 * dias
    elif 30 <= cantidad_alumnos <= 35:
        return 4.00 * dias
    else:
        return 3.50 * dias
    
"""
Este algoritmo final, engloba todos los costes calculados en los algoritmos previos y devuelve
el precio total a pagar por alumno.

"""
def calcular_coste_global_viaje(cantidad_alumnos, dias):
    coste_trayecto = calcular_coste_alumno_trayecto(cantidad_alumnos)
    coste_comida = calcular_coste_alumno_comida(dias)
    coste_alojamiento = calcular_coste_alumno_alojamiento(cantidad_alumnos, dias)

    return coste_trayecto + coste_comida + coste_alojamiento

# Aplicando este algoritmo con unos parametros cualquiera
cantidad_alumnos = int(input("Introduzca la cantidad de alumnos asistentes al viaje: "))
dias = int(input("Introduzca la cantidad de dias de estancia durante el viaje: "))
# Calcula el coste global del viaje
coste_global = calcular_coste_global_viaje(cantidad_alumnos, dias)

# Muestra el coste global del viaje por alumno, y el total
print("El coste global del viaje por alumno es:", coste_global, "€")
print("EL coste del viaje en total es:", coste_global * cantidad_alumnos, "€")
