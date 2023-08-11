name = 'Diana'
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))

full_name = 'Diana' + ' Marin'
age = 10 + 19
print(full_name)
print(age)
age = 12
print('Mi edad es: ' + str(age))
print(f'Mi edad es: {age}')

age = input('Escribe tu edad:')
print(type(age))
age = int(age)
age += 10
print(f'Tu edad en 10 años es : {age}')