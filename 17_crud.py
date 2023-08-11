#metodos de listas: CRUD (Create, Read, Update & Delete)
numbers = [1, 2, 3, 4, 5]
print(numbers[1])
numbers[-1] = 10
print(numbers)
#agregar un nuevo elemento appened al final de la lista
numbers.append(700)
print(numbers)
#agregar un nuevo elemento insert al inicio de la lista o la posicion que desee
numbers.insert(0, 'hola')
print(numbers)
numbers.insert(3, 'change')
print(numbers)

tasks = ['todo 1', 'todo 2', 'todo 3']
new_list = numbers + tasks
print(new_list)
#preguntar en que posicion esta un texto
print('Que posicion esta mi cadena:', new_list.index('todo 2'))
index = new_list.index('todo 2')
print(index)
new_list[index] = 'todo changed'
print(new_list)
#remove elimina elementos de la lista, se le especifica que valor es
new_list.remove('todo 1')
print(new_list)
#pop por defecto elimina el ultimo elemento de la lista se le especifica que osición
new_list.pop()
print(new_list)
new_list.pop(0)
print(new_list)
#cambiar la posición del array de cada posicion
new_list.reverse()
print(new_list)
#para ordenar, si tiene diferentes tipos de datos mezclados no se puede ordenar con esta funcion, sale un error
numbers_a = [1, 4, 6, 3]
numbers_a.sort()
print(numbers_a)

strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)
