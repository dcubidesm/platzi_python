#indexing and slicing
#indexing: los textos tiene un indicador a nivel de posiciones
text = 'Ella sabe Python'
print(text[0])
print(text[1])
#print(text[999]) arroja un error cuando el texto no es muy largo
size = len(text)
print(size)
print(text[size - 1])
#imprime el caracter de derecha a izquierda
print(text[-1])

#slicing: basado en las poscines de mi texto de donde a donde (sbtextos)
print(text[0:5])
print(text[10:16])
print(text[0:10])
#me toma desde la 1era posición hasta la 10 , se puede quitar el 0 ya que siempre inicia desde allí.|
print(text[5:])  #desde la posicion 5 hasta el final de la cadena
print(text[:])  #desde el inicio hasta el final
print(text[10:16:1])  #10(posicion inicial):16(posicion final):1(saltos de la cadena)
print(text[10:16:2])
print(text[::2])
