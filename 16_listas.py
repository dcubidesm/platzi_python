#array
#         0, 1, 2, 3
numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))
#              0        ,        1
tasks = ['make a dishes', 'play videogames']
print(tasks)
#         0,  1,     2
types = [1, True, 'Hola']
print(types)
print(numbers[0])
print(tasks[0])

#ajustes o cambios o llamados mutaciones(inmutables, los strings no se puede modificar, solo con la funcion replace
text = 'hola'
#cambiar la posición 0 las veces necesarias
tasks[0] = 'watch platz courses'
print(tasks)
tasks[0] = 'do the dishes'
print(tasks)

print(numbers[:3])
print(True in types)
print('hola' in types)
