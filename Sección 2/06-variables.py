x = 3
print(x)

x + x.__add__(5)

x2 = x.__add__(60)

print(x2)

# FLOAT: pero números decimales
y = 4.5
print(y)
type(x)




#COMPLEX: para números complejos, o sea, de la forma (A+Bj) donde la unidad imaginaria esta repreesntada por j.
c = 1+2j;
print(c), type(c)
parte_real = c.real
parte_imaginaria = c.imag

print(parte_real, parte_imaginaria)