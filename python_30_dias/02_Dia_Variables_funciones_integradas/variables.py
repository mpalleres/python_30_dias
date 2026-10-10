#Día 2: 30 días de programación en Python
sfirst_name = 'Nombre de pila'
slast_name = 'Paterno Materno'
scountry = 'Chile'
scity = 'Santiago'
nage = 250
bis_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname': 'Asabeneh',
    'lastname': 'Yetayeh',
    'country': 'Finland',
    'city': 'Helsinki'
}

# Printing the values stored in the variables

print('Nombres :', sfirst_name)
print('Largo Nombres:', len(sfirst_name))
print('Apellidos : ', slast_name)
print('Largo Apellidos: ', len(slast_name))
print('Pais: ', scountry)
print('Ciudad: ', scity)
print('Edad: ', nage)
print('Casado: ', bis_married)
print('Habilidades: ', skills)
print('Información de la persona: ', person_info)

# Declarar varias variables en una sola línea

sfirst_name, slast_name, scountry, nage, bis_married = 'Jony', '100 Pesos', 'Chile', 50, False

print(sfirst_name, slast_name, scountry, nage, bis_married)
print('Nombres :', sfirst_name)
print('Apellidos :', slast_name)
print('Pais: ', scountry)
print('Edad: ', nage)
print('Casado: ', bis_married)