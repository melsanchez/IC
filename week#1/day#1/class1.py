# Tipo de datos 

# Numeros 

a = 5 
# print(a, 'es del tipo', type(a))

a = 2.3 
# print(a, 'es del tipo', type(a))

a = 2 + 3j
# print(a, 'es del tipo', type(a))

# Cadenas de texto
s = 'Esta es una cadena\nmultiple'
# print(s)

s = '''Esta es 
una cadena multiple '''
# print(s)

# Listas

a = [3, 2.3, 'texto']
# print(a)

# Tuplas 
a = (3, 2.3, 'mas texto')

# Colecciones #no tienen ningun orden

c = {1, 2, 3, 4, 5}
# print(c)

c = {1, 2, 2, 3, 4, 4}
# print(c)

# Diccionario

d = {1: 'valor', 'key': 2}
# print(d)
# print(d['key'])

# Estamentos y expresiones

import platform

#Todo lo que retorne un valor es una expresion
version = format(platform.python_version())

#Los Estamentos es toda linea de codigo
# print("Mi version de python es", version); print('Hola')

# Identacion

def mensage():
    print('Linea 1')
    print('Linea 2')
    print('Linea 3')

#mensage()

# Funcion Print

nombre = "Daniel"

apellido = 'Villalba'

#print("Hola, {} {}".format(nombre, apellido))

# print(f"Hola, {nombre} {apellido}")
