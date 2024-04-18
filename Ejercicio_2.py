"""
Este algoritmo, clasifica 4 numeros que toma como entrada(dos numeros aleatorios dados, y los otros dos correponden a su suma  y a su producto)
y los ordena en orden crciente. El algortimo devuelve los numeros clasificados.
"""

#La flecha que aparece tras definir la función, indica lo que devuelve la función (la salida del algoritmo)
def clasificar4(a: int, b: int, c: int, d: int) -> list[int, int, int, int]:
     # Clasifica a, b y c en orden creciente
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    
    # Situa d
    if d < a:
        a, d = d, a
    
    # Clasifica b, c y d en orden creciente
    if b > c:
        b, c = c, b
    if c > d:
        c, d = d, c
    if b > c:
        b, c = c, b
    
    return a, b, c, d

# Ejemplo de uso
a = int(input("Introduzca el valor de a: "))
b = int(input("Introduzca el valor de b: "))
suma = a + b
producto = a * b

# Clasifica los numeros definidos previamente
clasificación_1 = clasificar4(a, b, suma, producto)

# Mostrar los números clasificados
print("Los números clasificados en orden creciente son:",clasificación_1)