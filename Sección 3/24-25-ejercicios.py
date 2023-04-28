# 3.6 Ejercicios
# 1) ¿Puedes indentificar el error en el siguiente código?
# media = num_1 +num_2 + num_3/3

# Se pretende hacer una media muestral de 3 elementos pero no funciona correctamente

num1 = 4
num2 = 3
num3 = 3

media = (num1 + num2 + num3)/3
print("El promedio es: ", media)

# 2 En la siguiene matriz, el cuarto elemento siempre es la suma de los tres anteriores.Utilizando la indeación corrige las listas que no cumplan esta condición

matriz = [
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]
print(matriz)
# Modificamos la primera fila
matriz[1][-1] = sum(matriz[1][:-1])

# modificamos la última fila
matriz[-1][-1] = sum(matriz[-1][:-1])

print(matriz)

# 3) En el desarollo de un video juego se te encarga configurar y balancear cada clase de personaje. Partiendo de que la estadistica base es 2, debes cumplir las siguientes condiciones:
#   *El caballero tiene el doble de vida y defensa que un guerrero.
#   *el guerrero tiene el doble de ataque y alcance que un caballero.
#   *el arquero tiene la misma vida y ataque que un guererro, pero la mitad de su defensa y el doble de su alcance
# * muestra como quedan las propiedades de los tres personajes
#
# caballero = {'vida':2, 'ataque':2, 'defensa':2, 'alcance':2 }
# guerrero  = {'vida':2, 'ataque':2, 'defensa':2, 'alcance':2 }
# arquero   = {'vida':2, 'ataque':2, 'defensa':2, 'alcance':2 }

caballero = {'vida': 2, 'ataque': 2, 'defensa': 2, 'alcance': 2}
guerrero = {'vida': 2, 'ataque': 2, 'defensa': 2, 'alcance': 2}
arquero = {'vida': 2, 'ataque': 2, 'defensa': 2, 'alcance': 2}

# Modificar Guerrero
guerrero['ataque'] = caballero['ataque']*2
guerrero['alcance'] = caballero['alcance']*2

# Modificar Caballero
caballero['vida'] = guerrero['vida']*2
caballero['defensa'] = guerrero['defensa']*2

arquero['ataque'] = guerrero['ataque']
arquero['defensa'] = guerrero['defensa']/2
arquero['alcance'] = guerrero['alcance']*2


print(guerrero)
print(caballero)
print(guerrero)

print(caballero, guerrero, arquero)
