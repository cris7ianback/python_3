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

# al realizar una consulta en un registro hemos recibido unos alores coruptos, al parecer entra el nombre y apellido del alumno al reves. ( que puede para obtener el sigueinte mensaje por pantalla)

cadena = "azebaC ellehciM, 01"
print(cadena)


def invertir_cadena(cadena):
    return cadena[::-1]


print(invertir_cadena())
