# 4.1 If / Else / elif: Sentencias condicionales
# En Python existen las sentencias condicionales if, else, elif (else if) que nos permiten dividir el flujo de un programa en diferentes caminos.

# Para hacer eso definimos un bloque de instrucciones que se ejecutarán solo si la condición previa se cumple (es verdadera).

if (True):
    print("Hey")

x = 6

if x == 6:
    print("x vale 6")

if x == 2:
    print("x vale 2")
if x == 6:
    print("x vale 6")


# Podemos escribir varios if anidados respetando la identación
a = 10
b = 5
if a == 10:
    print("A vale {}".format(a))
    if b == 5:
        print("B vale {}".format(b))


# También podemos incuir en estas sentencias operadores lógicos para aumentar su eficiencia y legibilidad.
if a == 10 and b == 5:
    print("A vale {}, y b vale {}".format(a, b))


# Else y Elif
# Else ( si no) se encadena al final del bloque para abrir una nueva lista instrucciones.
# Este comando nos permite definir el camino que se ejecuta si la condición original no se cumple.
# Elif(sino, si) establece una nueva condición que se encadena a otro if o elif cuya condición resultó False( no se cumplió).
# Esto nos permite establecer multiples condiciones para lidiar con los múltiples posibles entradas que el programa puede recibir.


z = 14
if z % 2 == 0:
    print(z, "Es número par")
else:
    print(z, "Es un número impar")


texto = input(" ¿Qué desea hacer?\n ")
if texto == 'SALUDAR':
    print('Muy buenas noches')
elif texto == 'RETIRARSE':
    print('Ok. Nos vemos luego')
else:
    print('Ingrese una entrada válida')


# Clasificador
puntaje = float(input("Introduce la calificación: \n"))
if puntaje >= 9:
    print('Excelente desempeño')
elif puntaje >= 7:
    print('Buen desempeño')
elif puntaje >= 5:
    print('Aprobado')
else:
    print('Reprobado')
