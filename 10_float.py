x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
#el formato es para darle presión a los números con decimales .2g solo dos digitos
y_str = format(y, ".2g")
print('str-> ', y_str)
print(str(x) == y_str)

print('*' * 10)
#para poder hacer la comparacion de los numeros con mas de 2 decimales, se debe tener en cuenta un minimo de toleracia, eje:
tolerance = 0.00001
#se debe tener en cuenta que los valores negativos no se tienen en cuenta se saca en valor absoluto(abs, numeros positivos) matematicamente para comparar estos valores es:
print(abs(x - y) < tolerance)
