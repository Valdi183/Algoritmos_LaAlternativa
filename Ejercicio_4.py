"""
Este script contiene un algoritmo que calcula la madeia de las 4 notas obtenidas por los  alumnos.
Para ello he creado una clase, que construye un objeto cuyo propósito es calcular la media de las
4 notas que se le den al programa. EL objeto realiza varias acciones, cada una un algoritmo. Esto 
quiere decir que hay un algoritmo que es el calculo de la media aritmetica (el metodo calcular_medias)
cuya entrada son las cuatro notas, y devuelve la media. El otro algoritmo (correspondiente con el metodo
evaluar_alumno) que toma como entrada la media calculada y devuelve la evaluación correspondiente según
los criterios especificados. Y el último algoritmo, es el que se encarga de pedir al usuario que ingrese
las notas (siendo esta su entrada) y las añade en una lista. Después llama a los tros dos metodos creados
(los algoritmos) para ejecutar ambos algoritmos y posteriormente, muestra en pantalla las salidas de ambos
algoritmos. En resumen, el último metodo, se encarga de procesar las notas como tal para que los algoritmos
simplemente hagan los calculos definidos y sea mucho mas facil trabajar con el objeto "CalcularNotas"
"""

class CalcularNotas:
    # Inicializo el constructor (no se necesita inicializar ningun parametro específico dentro de este)
    def __init__(self):
        pass

    def calcular_media(self, notas):
        return sum(notas) / len(notas) # Cálculo de la media
    
    # Metodo para evaluar al alumno según su media
    def evaluar_alumno(self, media):
        if media > 15:
            return "Alumno con talento"
        elif 12 <= media <= 15:
            return "Con capacidad"
        else:
            return "Debe reorientarse"

    # Metodo para facilitar el uso de los algoritmos
    def procesar_notas(self):
        notas_alumno = []

        # Solicita al usuario que ingrese las cuatro notas del alumno
        for i in range(4):
            nota = float(input(f"Ingrese la nota {i+1} del alumno (0-20): "))
            notas_alumno.append(nota)

        # Calcular la media de las notas del alumno
        media_alumno = self.calcular_media(notas_alumno)

        # Evalua al alumno según su media
        evaluacion = self.evaluar_alumno(media_alumno)

        # Muestra la media del alumno y su evaluación segun los criterios definidos
        print("La media del alumno es:", media_alumno)
        print("Evaluación del alumno:", evaluacion)

"""
Gracias al ultimo algoritmo, no necesitamos más que instanciar la clase, ya que el objeto 
se encarga no solo del calculo, si no tamién del proceso para introducir las notas, almacenarlas
y mostrarlas.
"""
calculadora = CalcularNotas()
calculadora.procesar_notas()
