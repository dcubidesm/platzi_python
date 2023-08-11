#cicles: loops: While ejecuta una instruccion repetidamente
'''
while True:
  print('Se ejecuto!')
'''
counter = 0

while counter < 10:
  counter += 1
  print(counter)

'''
counter = 0
while counter < 20:
  counter += 1
  if counter == 15:
    break  #romper el ciclo cuando llegue a 15
  print(counter)


counter = 0
while counter < 20:
  counter += 1
  if counter < 15:
    continue  # salta-continua con la siguiente iteracion, si eso no se cumple omite las demás líneas de código hacia abajo
  print(counter)
'''
