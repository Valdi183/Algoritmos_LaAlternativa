# Se coge la clase Enum de la librería enum para poder enumerar los dias de la semana
from enum import Enum

# Se enumeran los dias de la semana en una clase (convirtiendolos en objetos) heredando la clase Enum
class Dia(Enum):
    lunes = 1
    martes = 2
    miércoles = 3
    jueves = 4
    viernes = 5
    sábado = 6
    domingo = 0

"""
Aquí se exponen dos versiones de algoritmos cuyo proposito es obtener de resultado el dia de la semana anterior al dia de la semana dado.
En esta primera versión, el algoritmo sucesor, comprueba con condicionales, si el dia de la semana dado como entrada coincide con alguno
de los dias de la semana (definidos todos en el enum), y devuelve en la salida el dia de la semana sucesor.
"""
def sucesor_v1(dia: Dia):
    if dia == Dia.lunes:
        return "martes"
    elif dia == Dia.martes:
        return "miercoles"
    elif dia == Dia.miércoles:
        return "jueves"
    elif dia == Dia.jueves:
        return "viernes"
    elif dia == Dia.viernes:
        return "sábado"
    elif dia == Dia.sábado:
        return "domingo"
    elif dia == Dia.domingo:
        return "lunes"

"""
Esta segunda versión, utiliza como entrada un numero entero, correspondiendo a cada dia de la semana (en el enum se puede comprobar que numero 
tiene asignado cada día de la semana). Después, calcula el sucesor utilizando la aritmética modular y devuelve como salida otro numero entero, 
correspondiente al dia sucesor de la entrada
"""
def sucesor_v2(dia: int):
    """
    Devuelve el sucesor de un día de la semana representado como un número entero.
    """
    return (dia + 1) % 7

# Ejemplo de uso
dia_actual = Dia.martes
print("Día actual: martes")
print("Sucesor (versión 1):", sucesor_v1(dia_actual))

dia_actual_num = 3  # (miercoles)
print("Día actual (número):", dia_actual_num)
print("Sucesor (versión 2):", sucesor_v2(dia_actual_num))