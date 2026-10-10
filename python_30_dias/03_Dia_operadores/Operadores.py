# Tarea 1: Declarar la edad como variable entera
edad = 30
print("Mi edad es:", edad)
 
# Tarea 2: Declarar la altura como variable float
altura = 1.75
print("Mi altura es:", altura)
 
# Tarea 3: Declarar una variable que almacene un número complejo
numero_complejo = 2 + 3j
print("El número complejo es:", numero_complejo)
 
# Tarea 4: Pedir base y altura de un triángulo y calcular su área
base = float(input("Ingrese la base: "))
altura_triangulo = float(input("Ingrese la altura: "))
print("El área del triángulo es", 0.5 * base * altura_triangulo)
 
# Tarea 5: Pedir los lados a, b y c de un triángulo y calcular su perímetro
a = float(input("Ingrese el lado a: "))
b = float(input("Ingrese el lado b: "))
c = float(input("Ingrese el lado c: "))
print("El perímetro del triángulo es", a + b + c)
 
# Tarea 6: Pedir largo y ancho de un rectángulo; calcular área y perímetro
largo = float(input("Ingrese el largo: "))
ancho = float(input("Ingrese el ancho: "))
print("El área del rectángulo es", largo * ancho)
print("El perímetro del rectángulo es", 2 * (largo + ancho))
 
# Tarea 7: Pedir el radio de un círculo; calcular área y circunferencia (pi = 3.14)
pi = 3.14
radio = float(input("Ingrese el radio: "))
print("El área del círculo es", pi * radio * radio)
print("La circunferencia del círculo es", 2 * pi * radio)
 
# Tarea 8: Calcular pendiente, intercepto en x e intercepto en y de y = 2x - 2
m1 = 2
intercepto_y = -2
intercepto_x = -intercepto_y / m1  # y = 0 -> x = 1
print("La pendiente es:", m1)
print("El intercepto en x es:", intercepto_x)
print("El intercepto en y es:", intercepto_y)
 
# Tarea 9: Pendiente y distancia euclidiana entre (2, 2) y (6, 10)
x1, y1, x2, y2 = 2, 2, 6, 10
m2 = (y2 - y1) / (x2 - x1)
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("La pendiente es:", m2)
print("La distancia euclidiana es:", distancia)
 
# Tarea 10: Comparar las pendientes de las tareas 8 y 9
print("¿Las pendientes son iguales?", m1 == m2)  # True -> rectas paralelas
print("¿La pendiente de la tarea 8 es mayor que la de la tarea 9?", m1 > m2)
 
# Tarea 11: Calcular y = x^2 + 6x + 9 con distintos x; ¿en qué x es y = 0?
for x in range(-6, 1):
    print(f"x = {x:>2}, y = {x**2 + 6*x + 9}")
print("y vale 0 cuando x = -3")
 
# Tarea 12: Longitud de 'python' y 'dragon' y una comparación falsa
print("Longitud de 'python':", len('python'))
print("Longitud de 'dragon':", len('dragon'))
print("¿Tienen longitudes distintas?", len('python') != len('dragon'))  # False
 
# Tarea 13: Usar 'and' para comprobar si 'on' está en 'python' y en 'dragon'
print("¿'on' está en ambas palabras?", 'on' in 'python' and 'on' in 'dragon')  # True
 
# Tarea 14: Usar 'in' para comprobar si 'jargon' está en la oración
oracion = 'I hope this course is not full of jargon.'
print("¿'jargon' está en la oración?", 'jargon' in oracion)  # True
 
# Tarea 15: No hay 'on' ni en 'dragon' ni en 'python'
print("¿No hay 'on' en ninguna de las dos?", 'on' not in 'dragon' and 'on' not in 'python')  # False
 
# Tarea 16: Longitud de 'python' -> convertir a float -> convertir a str
n = len('python')
n = float(n)
n = str(n)
print("Valor convertido:", n, "| Tipo:", type(n))  # '6.0' <class 'str'>
 
# Tarea 17: Comprobar si un número es par
numero = int(input("Ingrese un número: "))
print(numero, "es par" if numero % 2 == 0 else "es impar")
 
# Tarea 18: ¿La división entera de 7 entre 3 es igual a int(2.7)?
print("¿7 // 3 es igual a int(2.7)?", 7 // 3 == int(2.7))  # True (ambos son 2)
 
# Tarea 19: ¿El tipo de '10' es igual al tipo de 10?
print("¿type('10') es igual a type(10)?", type('10') == type(10))  # False (str vs int)
 
# Tarea 20: ¿int('9.8') es igual a 10?
try:
    print("¿int('9.8') es igual a 10?", int('9.8') == 10)
except ValueError as e:
    print("Error:", e)  # int('9.8') lanza ValueError; int(float('9.8')) da 9
 
# Tarea 21: Pedir horas y tarifa por hora; calcular el pago semanal
horas = float(input("Ingrese las horas: "))
tarifa = float(input("Ingrese la tarifa por hora: "))
print("Su ganancia semanal es", horas * tarifa)
 
# Tarea 22: Pedir años vividos y calcular los segundos que ha vivido
anios = int(input("Ingrese el número de años que ha vivido: "))
segundos = anios * 365 * 24 * 60 * 60
print(f"Usted ha vivido {segundos} segundos.")
 
# Tarea 23: Mostrar la tabla (columnas: i, 1, i, i^2, i^3)
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)