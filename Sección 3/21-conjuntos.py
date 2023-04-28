# 3.4
# Los conjutos son colecciones de datos que nos facilitan ciertas operaciones ya que solo contienen valores únicos.
# Se diferencian de las tuplas y listas en que
#   *Cada elemento dentro del conjunto es único.
#   *Sus elementos no están ordenados.

conjunto_vacio = set()
conjunto = {1, 2, 3}

print(type(conjunto_vacio), conjunto)


# Métodos
# El método add()  nos permite agregar elementos al conjunto

conjunto.add(4)
conjunto.add(5)
conjunto.add("C")
conjunto.add("A")
conjunto.add("P")
print(conjunto)

# solo acepta valores únicos
conjunto.add("C")
print(conjunto)

# Podemos utilizar los conjuntos para verificar pertenencia

grupo = {"Luis", "Giulia", "Victor", "Aaron", "Johel"}
print("Victor" in grupo)

print("Johel" not in grupo)
print(4 not in grupo)
print(10 in conjunto)


# Un conjunto elimina automáticamente los elementos duplicados
grupo_carros = {"Toyota", "Toyota", "Ford"}
print(grupo_carros)


# Gracias a esta propiedad podemos convertir una lista a conjunto para eliminar duplicados fácilmente.
extra = [1, 1, 2, 2, 3, 3, 4, 5, 5, 4, 5, 6]
print(extra)

c = set(extra)
print(c)

sin_duplicados = list(c)
print(sin_duplicados)

# Podemos hacer la conversión en una sola línea
no_dupli = list(set(c))
print(no_dupli)

# Cuando aplicamos la conversión a una cadena, el conjunto resultante incluye solo las letras únicas de ésta
cadena = 'Jefe de jefe, patrón de patrón, Rocógelo, recógelo'
print(set(cadena))
