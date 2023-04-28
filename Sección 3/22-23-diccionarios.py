# 3.5 Diccionarios
# son colecciones de datos semejantes a las listas.
# Los diccionarios se caracterizan por:
# *se define cada elemento dentro de un diccionario como una relación entre Clave: Valor.
# *Las claves ejercen como indice de cada elemento ( No son únicamente números).

colores = {'azul': 'blue', 'negro': 'black', 'rosado': 'pink'}
propiedades = {1: 'Nombre', 2: 'Apellido', 3: 'Profesión', 4: 'Región'}

print(propiedades)

# Podemos escoger entre sus elementos utilizando las claves
print(colores)

print(colores['azul'])
print(colores['negro'])

# También podemos modificar los valores de sus elementos y realizar operaciones con ellos

colores['negro'] = 'noir'
print(colores)

colores['anaranjado'] = 'orange'
colores['blanco'] = 'white'
print(colores)

edades = {'Albert': 24,
          'Johel': 24,
          'Roque': 26,
          'Victor': 27
          }
print(edades['Roque'])

edades['Johel'] += 1
print(edades)

print(edades['Albert'] + edades['Victor'])

edades['Giulia'] = edades['Albert'] + edades['Victor']
print(edades)

# Métodos
# A través de un bucle For podemos recorrer los elementos de un diccionario
for c in edades:
    print(c)

# El método items() nos devuelve Clave y Valor automáticamente
for c, v in edades.items():
    print('Nombre:', c, 'Edad:', v)

# el método del() nos permite eliminar los valores de un diccionario.
del (colores['azul'])
print(colores)

# Debemos combinar provechosamente las listas y los diccionarios. Por ejemplo para crear un equipo de personajes

equipo = []

personajes = {
    'Nombre': 'Raskolnikov',
              'Clase': 'Picaro',
              'Nación': 'Rusia'
}

equipo.append(personajes)
print(equipo)

personajes = {'Nombre': 'Emma',
              'Clase': 'Curandera',
              'Nación': 'Francia'
              }
equipo.append(personajes)

personajes = {'Nombre': 'Rebeca',
              'Clase': 'Banquera',
              'Nación': 'Inglaterra'
              }
equipo.append(personajes)
print(equipo)

for e in equipo:
    print(e["Nombre"],",", e["Clase"], "oriundo de ", e["Nación"])