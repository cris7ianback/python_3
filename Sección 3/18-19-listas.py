# 3.2 Listas
# Son un tipo de dato compuesto de varios elementos, estos pueden ser caracteres o numero, u otros tipos incluso. Cada Elemento de la lista eaccesible gracias a su indice.

lista_de_compras = ["Huevos", "Leche", "Queso", "Jabón"]
print(lista_de_compras)
lista_con_precios = ["Huevos", 1.5, "Leche", 2, "Queso", 3.5, "Jabón", 5]
print(lista_con_precios)
print(type(lista_de_compras))

print(f"""Los {lista_con_precios[0]} cuestan {lista_con_precios[1]}
La {lista_con_precios[2]} cuesta {lista_con_precios[3]}""")

# Mutabilidad
# Las listas tienen la caracteristica de permitirnos modificar el valor de alguno de sus elementos. Eso se llama
# mutabilidad y es importante distinguir entre objetos mutables, como la listas, y otros objetos inmutables

lista_con_precios[1] = 0.9

print(f'''{lista_con_precios}
Los {lista_con_precios[0]} cuestan {lista_con_precios[1]}''')

# Metodos de las listas
# Podemos inicializar una lista de números a través de una funcion llamada range (a,b, in):
# * a es elimite inferior de la secuencia de numeros
# * b es el limite superior ( este se excluye).
# * in es la unidad de incremento (argumento opcional)
print(range(0, 20, 2))

numeros = range(0, 20, 2)
lista_numeros = list(numeros)
print(f""" {numeros}
{lista_numeros}""")

# Para añadir elementos a la lista utilizamos el método apprend().
lista_numeros.append(4)
print(lista_numeros)

# Podemos aplicar el operador de la adición + para concatenar dos listas
print(lista_numeros + [23, 66, 12, 35, 'hola', 'overtime', 'cygne'])


nu_lista = lista_numeros[:5] + [23, 66, 12, 35, 'hola', 'overtime', 'cygne']
print(nu_lista)

# La función len() nos permite conoce el número total de elementos
print(len([1, 2, 3]))

print(len(nu_lista))


# Podemos comprobar si algún valor existe dentro de una lista a través del termino in
print(3 in [1, 2, 3])
print("hola" in nu_lista)


# Podemos actualizar varios elementos de una lista utiliando el slicing.
nu_lista[:4] = ["Platos", 14, "Libros", "Teclados"]
print(nu_lista)

# También podemos trabajar con listas anidadas, asignando listas como valores en una lista.
fila_1 = [1, 2, 3]
fila_2 = [4, 5, 6]
fila_3 = [7, 8, 9]
matriz = [fila_1, fila_2, fila_3]

print(matriz)
print(matriz[0])
print(matriz[0] == fila_1)
print(matriz[0][1])
print(matriz[1][1:])
