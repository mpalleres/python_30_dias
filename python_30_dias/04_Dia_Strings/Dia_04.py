# -*- coding: utf-8 -*-
# Día 4: Strings - Ejercicios resueltos (entradas y salidas en español)

print("=" * 50)
print("DÍA 4: STRINGS - EJERCICIOS")
print("=" * 50)

# ---------------------------------------------------------
# NIVEL 1
# ---------------------------------------------------------
print("\n--- NIVEL 1 ---")

# 1. Concatenar 'Treinta', 'Días', 'De', 'Python'
a = input("1. Escribe la 1ra palabra (ej. Treinta): ")
b = input("   Escribe la 2da palabra (ej. Días): ")
c = input("   Escribe la 3ra palabra (ej. De): ")
d = input("   Escribe la 4ta palabra (ej. Python): ")
print("Resultado:", a + " " + b + " " + c + " " + d)

# 2. Concatenar 'Programando', 'Para', 'Todos'
x = input("\n2. Escribe 3 palabras separadas por coma (ej. Programando,Para,Todos): ")
print("Resultado:", " ".join(x.split(",")))

# 3 y 4. Variable empresa e imprimirla
empresa = input("\n3. Escribe el nombre de la empresa (ej. Programando Para Todos): ")
print("4. La empresa es:", empresa)

# 5. Longitud
print("5. Longitud del texto:", len(empresa))

# 6 y 7. Mayúsculas y minúsculas
print("6. En mayúsculas:", empresa.upper())
print("7. En minúsculas:", empresa.lower())

# 8. capitalize, title, swapcase
print("8. capitalize():", empresa.capitalize())
print("   title():", empresa.title())
print("   swapcase():", empresa.swapcase())

# 9. Cortar la primera palabra
partes = empresa.split(" ", 1)
print("9. Sin la primera palabra:", partes[1] if len(partes) > 1 else "")

# 10. Verificar si contiene una palabra
palabra = input("\n10. ¿Qué palabra quieres buscar en el texto? ")
if empresa.find(palabra) != -1:
    print(f"    Sí, contiene '{palabra}' en la posición {empresa.find(palabra)}")
else:
    print(f"    No contiene '{palabra}'")

# 11 y 12. Reemplazar palabras
vieja = input("\n11. ¿Qué palabra quieres reemplazar? ")
nueva = input("    ¿Por cuál palabra? ")
print("    Resultado:", empresa.replace(vieja, nueva))

frase = "Python para Cualquiera"
print("12. Original:", frase)
print("    Cambiado:", frase.replace("Cualquiera", "Todos"))

# 13. split con espacio
print("\n13. Dividir por espacios:", empresa.split())

# 14. split por coma
empresas = input("14. Escribe empresas separadas por coma (ej. Facebook, Google, Microsoft): ")
print("    Lista:", [e.strip() for e in empresas.split(",")])

# 15, 16, 17. Índices
print("\n15. Carácter en el índice 0:", empresa[0])
print("16. Último índice:", len(empresa) - 1, "->", empresa[-1])
i = int(input("17. ¿Qué índice quieres consultar? "))
if 0 <= i < len(empresa):
    print("    Carácter en el índice", i, ":", repr(empresa[i]))
else:
    print("    Ese índice no existe en el texto")

# 18 y 19. Acrónimos
nombre = input("\n18. Escribe un nombre para crear su acrónimo (ej. Python Para Todos): ")
print("    Acrónimo:", "".join(w[0] for w in nombre.split()).upper())
print("19. Acrónimo de 'Programando Para Todos':",
      "".join(w[0] for w in "Programando Para Todos".split()).upper())

# 20 y 21. index de la primera ocurrencia
letra = input("\n20. ¿Qué letra quieres buscar (primera ocurrencia)? ")
try:
    print("    Primera posición de", letra, ":", empresa.index(letra))
except ValueError:
    print("    Esa letra no está en el texto")

# 22. rfind última ocurrencia
texto22 = "Programando Para Toda la Gente"
print("22. Última 'l' en '" + texto22 + "':", texto22.rfind("l"))

# ---------------------------------------------------------
# NIVEL 2
# ---------------------------------------------------------
print("\n--- NIVEL 2 ---")

oracion = "No puedes terminar una oración con porque porque porque es una conjunción"
print("23. Primera posición de 'porque':", oracion.index("porque"))
print("24. Última posición de 'porque':", oracion.rindex("porque"))

ini = oracion.index("porque")
fin = oracion.rindex("porque") + len("porque")
print("25. Frase cortada:", oracion[ini:fin])

# 28 y 29. startswith / endswith
print("\n28. ¿Empieza con 'Programando'?", empresa.startswith("Programando"))
print("29. ¿Termina con 'programando'?", empresa.endswith("programando"))

# 30. strip
sucio = input("\n30. Escribe un texto con espacios al inicio y al final: ")
print("    Limpio: '" + sucio.strip() + "'")

# 31. isidentifier
for var in ["30DiasDePython", "treinta_dias_de_python"]:
    print("31.", var, "-> ¿es identificador válido?", var.isidentifier())

# 32. join con "# "
librerias = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print("32.", "# ".join(librerias))

# 33. Salto de línea
print("\n33.")
print("Estoy disfrutando este reto.\nMe pregunto qué sigue.")

# 34. Tabulaciones
print("\n34.")
print("Nombre\tEdad\tPaís\tCiudad")
print("Asabeneh\t250\tFinlandia\tHelsinki")

# 35. Área del círculo con formato
radio = float(input("\n35. Escribe el radio del círculo: "))
area = 3.14 * radio ** 2
print("El área de un círculo con radio {} es {:.2f} metros cuadrados.".format(radio, area))

# 36. Operaciones con formato
n1 = int(input("\n36. Escribe el primer número: "))
n2 = int(input("    Escribe el segundo número: "))
print(f"{n1} + {n2} = {n1 + n2}")
print(f"{n1} - {n2} = {n1 - n2}")
print(f"{n1} * {n2} = {n1 * n2}")
print(f"{n1} / {n2} = {n1 / n2:.2f}" if n2 != 0 else "No se puede dividir entre 0")
print(f"{n1} % {n2} = {n1 % n2}" if n2 != 0 else "No se puede calcular el módulo con 0")
print(f"{n1} // {n2} = {n1 // n2}" if n2 != 0 else "No se puede dividir entre 0")
print(f"{n1} ** {n2} = {n1 ** n2}")

print("\n¡Listo!  los ejercicios del Día 4.")