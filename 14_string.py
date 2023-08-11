text = 'Todo lo que te propongas lo puedes lograr!'

print('JavaSctipt' in text)
print('Python' in text)

if 'Python' in text:
  print('Elegiste bien!')
else:
  print('También elegiste bien!')

#tamaño de las cadenas de texto
size = len(text)
print(size)
#metodos para manejar cadenas de texto
print('Metodos para cadenas: ')
print('Texto en Mayusculas:', text.upper())
print('Texto en Minusculas:',text.lower())
print('Cuenta # de caracteres del texto:', text.count('a'))
print('Hace inversion de Mayus y Minus: ', text.swapcase())
#Si un texto inicia con algo en especifico startswith
print('Respuesta booleana: ', text.startswith('Ella'))
#Si un texto finaliza con algo en especifico startswith
print('Respuesta booleana: ', text.endswith('Rush'))
print('Reemplazar un texto :', text.replace('Python', 'Go'))

text2 = 'este es un titulo'
print(text2)
print('Poner el 1er caracter en mayus :', text2.capitalize())
print('Poner los caracteres en mayus x cada palabra :', text2.title())
print('Si es un digito :', text2.isdigit())
#Puede validar si es un potencialmente un digito
print('398'.isdigit())
