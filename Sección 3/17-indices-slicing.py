# 3.1 Índices y Slicing
# Los índices son números ordenados asociados a las variables que nos permiten identiciar los elementos por su posición.
# Por ejemplo, cada elemento de una cadena tiene su indice.

texto = 'ESTA-CADENA'
print(texto)

# El primer elemento siempre tiene el indice 0 porque con este número inicia la numeración.
print(texto[0], texto[1], texto[2], texto[3])

# también a cusa de esto, el indice del ´ltimo elemento se diferencia del número total de elementos por una unidad
print(texto[5], texto[6], texto[7], texto[8], texto[9], texto[10])

# Para cada elemento también existe un indice inverso que realiza una numeración desde el último elemento hasta el primero, empezando la cuenta con -1.
# -6 \ -5 \ -4 \ -3 \ -2 \ -1
#  C    A    D    E    N    A
#  5 /  6 /  7 /  8 /  9 / 10

print(texto[-6], texto[-5], texto[-4], texto[-3], texto[-2], texto[-1])


# Slicing
# Gracias a los  indices podemos seleccionar una secuencia de elemntos d una variable. Esto se conoce como slicing
# la secuencia de elementos la definimos con el formato[a:b]. Esto es un rango de valores, y el slicing va a devolvernos desde el
# elemento a hasta el elemento previo al b, así que vamos a decir que b está exluido del rango.
    #PROTIP: Cuando un rango de valores exclucye alguno de sus limites (Siendo a el limite inferior, y b el lmite superior), se dice que el rango es abierto:
        # --> Abierto por la derecha, si exclucye a b
        # --> Abiertpo por la Izquierda, si excluye a a

texto[0:3]
print(texto)
texto[-6:0]
print(texto)

# Podemos Omitir espspecificar alguno de los limites:
# si omitimos a[:b], empezará la secuencia desde el indice 0. (Equivale a escribir [0 : b])
# si omitimos b[a:], termina la secuencia con el último elemento. (Equivale a escribir[ a: (n-1)])


texto[-6]
print(texto)
texto[:4]
print(texto)
