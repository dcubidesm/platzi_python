#diccionarios: key : value
my_dict = {}
print(type(my_dict))

my_dict = {
'avion' : "bla bla bla",
'name': 'Nicolas',
'last_name':'Molina Monrroy',
'age' : 87  
}
print(my_dict)

print(len(my_dict))
print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('unvalor'))#sirve para buscar dentro del dict , si no existe ese valor me arroja un None indicando que ese valor no existe
print(my_dict.get('age'))

print('avion' in my_dict)
print('otro que no' in my_dict)