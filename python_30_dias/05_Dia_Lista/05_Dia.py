# Day 5 - Listas
# Para los ejercicios de países, coloca countries.py en la misma carpeta:
# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py

# ================= LEVEL 1 =================
print("--- Level 1 ---")

# 1. Lista vacía
empty_list = []

# 2. Lista con más de 5 elementos
fruits = ['Platano', 'Naranja', 'Mango', 'Limon', 'Manzana', 'uva']

# 3. Longitud
print(len(fruits))  # 6

# 4. Primer, central y último elemento
first = fruits[0]
middle = fruits[len(fruits) // 2]
last = fruits[-1]
print(first, middle, last)

# 5. Tipos de datos mezclados
mixed_data_types = ['Ana', 30, 1.65, 'Soltera', 'Av. Principal 123, Santiago']

# 6. it_companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Imprimir la lista
print(it_companies)

# 8. Número de empresas
print(len(it_companies))  # 7

# 9. Primera, central y última
print(it_companies[0], it_companies[len(it_companies) // 2], it_companies[-1])

# 10. Modificar una empresa
it_companies[1] = 'Alphabet'
print(it_companies)

# 11. Agregar una empresa al final
it_companies.append('Tesla')

# 12. Insertar una empresa en el medio
it_companies.insert(len(it_companies) // 2, 'Intel')
print(it_companies)

# 13. Una empresa a mayúsculas (excepto IBM)
it_companies[0] = it_companies[0].upper()  # FACEBOOK
print(it_companies)

# 14. Unir con '#;  '
print('#;  '.join(it_companies))

# 15. Verificar si existe una empresa
company = 'Google'
print(company in it_companies)  # False (la cambiamos por 'Alphabet')
print('Alphabet' in it_companies)  # True

# 16. sort()
it_companies.sort()
print(it_companies)

# 17. reverse() (orden descendente: sort + reverse)
it_companies.reverse()
print(it_companies)

# 18. Primeras 3
print(it_companies[:3])

# 19. Últimas 3
print(it_companies[-3:])

# 20. Empresa(s) del medio
n = len(it_companies)
if n % 2 == 1:
    print(it_companies[n // 2])
else:
    print(it_companies[n // 2 - 1: n // 2 + 1])

# 21. Eliminar la primera
it_companies.pop(0)

# 22. Eliminar la(s) del medio
n = len(it_companies)
if n % 2 == 1:
    it_companies.pop(n // 2)
else:
    del it_companies[n // 2 - 1: n // 2 + 1]

# 23. Eliminar la última
it_companies.pop()
print(it_companies)

# 24. Eliminar todas
it_companies.clear()
print(it_companies)  # []

# 25. Destruir la lista
del it_companies
# print(it_companies)  # NameError: ya no existe

# 26. Unir listas
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined = front_end + back_end
print(joined)

# 27. Copiar e insertar Python y SQL después de Redux
full_stack = joined.copy()
index = full_stack.index('Redux') + 1
full_stack[index:index] = ['Python', 'SQL']
print(full_stack)
# ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Python', 'SQL', 'Node', 'Express', 'MongoDB']

# ================= LEVEL 2 =================
print("\n--- Level 2 ---")

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Ordenar, mínimo y máximo
ages.sort()
min_age = min(ages)
max_age = max(ages)
print(ages, min_age, max_age)

# Agregar min y max otra vez
ages.append(min_age)
ages.append(max_age)
ages.sort()
print(ages)

# Mediana
n = len(ages)
if n % 2 == 1:
    median = ages[n // 2]
else:
    median = (ages[n // 2 - 1] + ages[n // 2]) / 2
print('Mediana:', median)

# Promedio
average = sum(ages) / len(ages)
print('Promedio:', average)

# Rango
print('Rango:', max_age - min_age)

# Comparar abs(min - average) y abs(max - average)
print(abs(min_age - average), abs(max_age - average))

# --- Países ---
from countries import countries

# 1. País(es) del medio
n = len(countries)
if n % 2 == 1:
    print(countries[n // 2])
else:
    print(countries[n // 2 - 1: n // 2 + 1])

# 2. Dividir en dos listas (si es impar, la primera mitad lleva uno más)
half = (n + 1) // 2
first_half = countries[:half]
second_half = countries[half:]
print(len(first_half), len(second_half))

# 3. Desempaquetar
nordic = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *scandic = nordic
print(china, russia, usa)
print(scandic)  # ['Finland', 'Sweden', 'Norway', 'Denmark']