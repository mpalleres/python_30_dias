# Crear un diccionario vacío llamado dog
dog = {}

# 1. Añadir las claves name, color, breed, legs y age
dog['name'] = 'Rex'
dog['color'] = 'marrón'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 3
print(dog)
# {'name': 'Rex', 'color': 'marrón', 'breed': 'Labrador', 'legs': 4, 'age': 3}

# 2. Crear el diccionario student
student = {
    'first_name': 'Marco',
    'last_name': 'Pérez',
    'gender': 'masculino',
    'age': 28,
    'marital_status': 'soltero',
    'skills': ['Python', 'SQL', 'JavaScript'],
    'country': 'Chile',
    'city': 'Santiago',
    'address': 'Av. Providencia 1234'
}

# 3. Longitud del diccionario student
print(len(student))
# 9

# 4. Obtener el valor de skills y comprobar su tipo
skills = student['skills']
print(skills)         # ['Python', 'SQL', 'JavaScript']
print(type(skills))   # <class 'list'>
print(type(skills) is list)  # True

# 5. Modificar skills añadiendo una o dos habilidades
student['skills'].append('Docker')
student['skills'].extend(['Git', 'FastAPI'])
print(student['skills'])
# ['Python', 'SQL', 'JavaScript', 'Docker', 'Git', 'FastAPI']

# 6. Lista de claves del diccionario
keys = list(student.keys())
print(keys)
# ['first_name', 'last_name', 'gender', 'age', 'marital_status',
#  'skills', 'country', 'city', 'address']

# 7. Lista de valores del diccionario
values = list(student.values())
print(values)

# 8. Convertir el diccionario en una lista de tuplas con items()
items = list(student.items())
print(items)
# [('first_name', 'Marco'), ('last_name', 'Pérez'), ...]

# 9. Eliminar un elemento del diccionario
del student['address']
# También se puede usar: student.pop('address')
print(student)

# 10. Eliminar uno de los diccionarios
del dog
# print(dog)  # Daría NameError: name 'dog' is not defined