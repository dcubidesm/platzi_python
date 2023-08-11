name = 'Diana'
print(name)
last_name = 'Marin'
print(last_name)
full_name = name + ' ' + last_name
print(full_name)
age = 29
print(age)
quote = "I'm Diana"
print(quote)
quote2 = 'She said "H e l l o "'
print(quote2)
#format
template = "Mi nombre es " + name + " y mi apellido es " + last_name
print('1er forma: ', template)
template2 = "Mi nombre es {} y mi apellido es {}".format(name, last_name)
print('2do forma: ', template2)
template3 = f"Mi nombre es {name} y mi apellido es {last_name}"
print('3ra forma: ', template3)
template4 = f"Mi nombre es {name} y mi apellido es {last_name} y mi edad es {age}"
print('3ra forma: ', template4)
