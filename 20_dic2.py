#Insertar y eliminar de un diccionario
person = {
  'name': 'Diana',
  'last_name': 'Marin',
  'langs': ['python', 'SQL'],  #array(lista)
  'age': 29
}

print(person)
#Update = nomlista['key'] = 'new value'
person['name'] = 'Paola'
print(person)
#se puede hacer modificacion con una operacion, eje: reducir la edad
person['age'] += 10
print(person)

#Insert datos append dentro de un array
person['langs'].append('Go')
print(person)

#Delete: con funcion  del ó pop
del person['last_name']
print(person)
#pop siempre se especifica que key en este caso para los diccionarios si no se coloca que llave, sale error
person.pop('age')
print(person)
## funciones
#items: devuelve en una lista, los pares de tuplas de la estructura de datos del diccionario: [(key:value),(key:value),(key:value)]
print('I T E M S')
print(person.items())
#retorna los nombres de los keys en una lista.
print('K E Y S')
print(person.keys())
#retorna los valores de los values de las keys en una lista.
print('V A L U E S')
print(person.values())
