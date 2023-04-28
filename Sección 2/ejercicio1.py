# 1
# Define una variable edad y asignale un valor entero OK
# Muestra su valor por pantalla OK
# define otra variable edad_cadena que contenga el valor de edad como una cadena de caracteres
# comprueba el tipo de la nueva variable
# Utiliza la variable edad que has definido prevviamente y  calcula que edad tendria esa persona en el año 2035


edad = 31
print(edad)

edad_cadena = str(edad)
print(edad_cadena)

print(type(edad_cadena))

edad_2035 = (2035-2023) + edad

print(edad_2035)

# 2
# Al realizar una consulta en un registro hemos recibido unos valores corruptos, al parecer entra el nombre y apellido del alumno al reves. (Que puede para obtener el sigueinte mensaje por pantalla)
cadena = "azebaC ellehciM, 01"
cadena_volteada = cadena[::-1]
print(cadena_volteada[4::], " ha sacado un ", cadena_volteada[:2])


# 3
# Utilizando operadores lógicos determina si una cadena de texto introducida por el usuario tiene una longitud mayor o ogual a 3  y menor o igual a 12 ( Basta con mostrar True o False)

texto = input('Ingrese Texto Aquí: ')
print('¿ el texto ingresado es mayor a 3?',
      len(texto) >= 3 and len(texto) <= 12)


# 4) Realiza un programa que lea 2 números por teclado y tedermine los siguientes aspectos ( es suficiente con mostrar True o False):
# * Si los dos números son iguales
# * si los dos numeros son diferentes
# * si el primero es mayor que el segundo
# * si el segundo e mayor o igual que el primero.


n1 = input('Ingrese primer Número: ')
n2 = input('Ingrese segundo Número: ')

print('Los Números son Iguales?:', n1 == n2)
print('Los Números son Diferentes?:', n1 != n2)
print('N°1 es  mayor que N°2"?:', n1 > n2)
print('N°2 es mayor o igual que el N°1:', n1 <= n2)
