#loop :FOR , se itera pero se establece el tamaño de los elementos
'''
for element in range(1, 21):
  print(element)
'''
#listas
my_list = [23, 45, 67, 89, 43]
for element in my_list:
  print(element)
#tuplas
my_tuple = ('nico', 'diana', 'luis')
for element in my_tuple:
  print(element)

  #diccionarios, se le especifica que debe imprimir todo KEY:VALUE
  print('--------------')
product = {'name': 'camisa', 'price': 100, 'stock': 89}

for key in product:
  print(key, '=>', product[key])
  print('--------------')
#genera el mismo resultado anterior
for key, value in product.items():
  print(key, '=>', value)

#es una lista que tiene 3 diccionarios dentro y debemos recorrerlo
people = [{
  'name': 'nico',
  'age': 34
}, {
  'name': 'zule',
  'age': 45
}, {
  'name': 'santi',
  'age': 4
}]
#se retorna solo las keys llamadas 'name' de los 3 diccionarios
for person in people:
  print('name => ', person['name'])
