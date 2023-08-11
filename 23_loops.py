#CICLOS ANIDADOS
#MATRIZ
#es una lista que tiene 3 listas(sublistas) 3x3, se maneja por posiciones, eje lista 1 = posición 0, lista 2 = posición 1 y lista 2 = posición 2
matriz = [
  [1, 2, 3],  #0
  [4, 5, 6],  #1
  [7, 8, 9]  #2
]

print(matriz[0])
#coordenadas
print(matriz[0][1])

#iteracion dentro de otra de una lista tiene 3 listas
for row in matriz:
  print(row)
  for column in row:
    print(column)

######

my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []

for i in my_list:
  #< 0 me retorna los valores negativos
  #> 0 me retorna los valores positivos
  if i < 0:
    new_list.append(i)
print(new_list)
