
import numpy as np

l = [[1, 2, 3, 4, 5] , [6, 7, 8, 9, 10]]
n1 = np.array(l)
print(n1)
print(type(n1))

# Principales atributos
print(n1.ndim)
print(n1.shape)
print(n1.size)
print(n1.dtype)

## Acceso a los elementos
print(n1[1, 2]) # PRIMER NUMERO ES EL RENGLON, SEGUNDO NUMERO ES LA COLUMNA

print(n1.transpose())

print(n1[0, :].mean())
"""
    Ecuaciones
    x + 2y = 1
    3x + 5y = 2
"""
ecuaciones = [[1, 2], [3, 5]]

np_ecuaciones = np.array(ecuaciones)
resultados = np.array([1, 2])
print(np.linalg.solve(np_ecuaciones, resultados))

print("Fin")