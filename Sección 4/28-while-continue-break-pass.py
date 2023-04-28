# 4.2 Bucle While
# Un bucle es una secuencia que ejecuta reiteradas veces una acción hasta que la condición asignada al bucle deja de cumplirse. Cada nueva ejecución de la secuencia se denomina iteración.
# la sentencia While(Mientras) repite las operaciones dentro de un bloque mientras la condición lógica que evalúa es True(Verdadera).
# El pgroamador debe planificar un momento en que la condición es False y el bucle se detiene. De otra forma se vuelve un bucle infinito.


# contador = 0

# while contador <= 5:
#     contador += 1
#     print("Contador vale ", contador)

# c = 0

# while c <=5:
#     c +=1
#     print("Contador vale ", c)
# else:
#     print("Se realizaron {} iteraciones".format(c))


# BREAK
# Con este comando detenemos el bucle en cualquier momento.

contador = 0

while contador <= 5:
    contador += 1
    if contador == 4:
        print("Rompemos el bucle cuando contador vale ", contador)
        break
    print("Contador vale ", contador)
else:
    print("Se realizaron {} iteraciones".format(contador))


# Continue
# Con este comando saltamos a la siguiente iteración sin romper el bucle

c = 0

while c <= 5:
