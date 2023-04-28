# 3.3 Tuplas
# Una tupla es una secuencia de valores ( muy parecida a una lista). Los valores almacenados en una tupla pueden ser de cualquier tipo, y tambien estan indexados.

# Se diferencia de las listas en que:
# *No podemos modificar sus valores luego de crearla (Es Inmutable).
# *Definimos sus valores entre parentesis, en vez de corchetes.

tupla = ('Lunes', 'Martes', 'Miércoles')
print(tupla)
tupla_multi = ([1, 2, 3], 'a', 71.4, tupla)
print(tupla_multi)

lista = list(tupla)
print(lista)

lista[0] = 'Domingo'
print(lista)

# Métodos
tupla.index('Lunes')
print(tupla_multi.count(71.4))
