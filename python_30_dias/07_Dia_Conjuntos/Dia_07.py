# Día 7 - Conjuntos (sets)

# Datos del enunciado original de 30 Days of Python
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# ================= NIVEL 1 =================
print("--- Nivel 1 ---")

# 1. Longitud
print(len(it_companies))  # 7

# 2. Agregar 'Twitter'
it_companies.add('Twitter')

# 3. Agregar varias empresas de una sola vez
it_companies.update(['Tesla', 'Netflix', 'Intel'])
print(it_companies)

# 4. Eliminar una empresa
it_companies.remove('Netflix')
print(it_companies)

# 5. Diferencia entre remove() y discard()
#    remove(x):  si x NO existe, lanza KeyError.
#    discard(x): si x NO existe, no hace nada (no hay error).
it_companies.discard('Netflix')  # ya no está, pero no da error
# it_companies.remove('Netflix')  # KeyError

# ================= NIVEL 2 =================
print("\n--- Nivel 2 ---")

# 1. Concatenar (unir) A y B
print(A.union(B))  # o A | B

# 2. Intersección
print(A.intersection(B))  # o A & B

# 3. ¿A es subconjunto de B?
print(A.issubset(B))  # True

# 4. ¿A y B son disjuntos?
print(A.isdisjoint(B))  # False (tienen elementos en común)

# 5. Combinar A con B y viceversa (la unión es conmutativa)
print(A.union(B))
print(B.union(A))
print(A.union(B) == B.union(A))  # True

# 6. Diferencia simétrica
print(A.symmetric_difference(B))  # o A ^ B

# 7. Eliminar un conjunto por completo
del A
del B
# print(A)  # NameError: ya no existe

# ================= NIVEL 3 =================
print("\n--- Nivel 3 ---")

# 1. Lista de edades -> conjunto, comparar longitudes
age_set = set(age)
print(len(age), len(age_set))  # 8 5 -> la lista es mayor

# 2. Diferencias entre tipos de datos
#    Cadena (str):    secuencia ordenada e INMUTABLE de caracteres.
#    Lista (list):    secuencia ordenada y MUTABLE; admite duplicados.
#    Tupla (tuple):   secuencia ordenada e INMUTABLE; admite duplicados.
#    Conjunto (set):  colección SIN orden, SIN duplicados, sin índices;
#                     es mutable (se puede agregar/quitar) pero sus
#                     elementos deben ser inmutables (hashables).

# 3. Palabras únicas de la frase
frase = "Soy profesor, me gusta motivar y enseñar a las personas."
palabras = frase.split()
unicas = set(palabras)
print(palabras)
print(len(unicas))  # 10

# Versión más precisa: quitar puntuación y pasar a minúsculas
import string
limpias = frase.translate(str.maketrans('', '', string.punctuation)).lower().split()
print(len(set(limpias)))  # 10