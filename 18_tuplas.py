#tuplas: estructuras de control, cadenas de texto son untable no se puede hacer cambios sobre ellas cuando ya esta declarada, sería solo de lectura.
numbers = (1,2,3,5)
strings = ('nico','zule','santi','nico')
print(numbers)
print(type(numbers))
print(numbers[0])
print(numbers[-1])
print(strings)
print(strings.index('zule'))
print('Frecuencia de la cadena a buscar:',strings.count('nico'))
#convertirlo de tupla a una lista
my_list = list(strings)
print(type(my_list))

my_list[1] ='juli'
print(my_list)
#convertirlo de lista a una tupla
my_tuple = tuple(my_list)
print(type(my_tuple))
