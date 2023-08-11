#condicionales IF
if True:
  print('Debería ejecutarse')

if False:
  print('Nunca se ejecutarse')

pet = input('Cúal es tu mascota favorita? ')
if pet == 'perro':
  print('Tienes un buen gusto')
elif pet == 'gato':
  print('Espero tengas suerte!!')
elif pet == 'pez':
  print('Es lo máximo')
else:
  print('No tienes ninguna mascota interesante')
'''
stock = int(input('Digita el stock: '))

if stock >= 100 and stock <= 1000:
  print('El stock es correcto')
else:
  print('El stock es incorrecto ')
'''
#saber si un número es par o impar
number = int(input('Digite un número: '))
result = number % 2
if result == 0:
  print('Es número par')
else:
  print('Es número impar')
