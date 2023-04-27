# FORMATEO
print('{} es el primer valor y {} es el segundo'.format(1, 2))
print('En este caso alteramos el orden y el {1} aparece primero, luego el {0}'.format(
    'Uno', 'Dos'))


nombre = ' la cartuja de parma'
x = .7

print(F'El valor de {nombre} es', x)

# También podemos aplicar métodos
print(f'El valor de {nombre.title()}\n es', x, 'dolares por el papel')

diccionario = {'uno': x, 'dos': x.__add__(10)}

print(diccionario)

print(f'{nombre.title()} cuesta {diccionario["uno"]} pesos \n y el otro libro {diccionario["dos"]} pesos.')
