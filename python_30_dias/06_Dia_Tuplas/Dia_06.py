# Día 6 - Tuplas

# ================= NIVEL 1 =================
print("--- Nivel 1 ---")

# 1. Tupla vacía
empty_tuple = ()

# 2. Tuplas con hermanos y hermanas (ficticios)
brothers = ('Juan', 'Pedro')
sisters = ('Ana', 'Marta', 'Lucía')

# 3. Concatenar y asignar a siblings
siblings = brothers + sisters
print(siblings)

# 4. ¿Cuántos hermanos tengo?
print(len(siblings))  # 5

# 5. Las tuplas no se pueden modificar, así que se crea una nueva
#    concatenando los padres
parents = ('Carlos', 'Rosa')
family_members = siblings + parents
print(family_members)

# ================= NIVEL 2 =================
print("\n--- Nivel 2 ---")

# 1. Extraer hermanos y padres desde family_members
n_siblings = len(siblings)
siblings_extracted = family_members[:n_siblings]
parents_extracted = family_members[n_siblings:]
print(siblings_extracted)
print(parents_extracted)

# 2. fruits, vegetables, animal_products -> food_stuff_tp
fruits = ('banana', 'orange', 'mango')
vegetables = ('tomato', 'carrot', 'onion')
animal_products = ('milk', 'meat', 'honey')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# 3. Tupla -> lista
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# 4. Elemento(s) del medio
n = len(food_stuff_tp)
if n % 2 == 1:
    middle = food_stuff_tp[n // 2]
else:
    middle = food_stuff_tp[n // 2 - 1: n // 2 + 1]
print(middle)  # 'carrot' (9 elementos -> índice 4)

# 5. Primeras tres y últimas tres entradas de la lista
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])

# 6. Eliminar completamente la tupla
del food_stuff_tp
# print(food_stuff_tp)  # NameError: la tupla ya no existe

# 7. Comprobar elementos
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)  # False
print('Iceland' in nordic_countries)  # True