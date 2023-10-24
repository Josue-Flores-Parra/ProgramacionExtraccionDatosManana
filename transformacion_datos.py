
import pandas as pd

alumnos = {
    "nombre": ["Juan", "Maria", "Pedro", "Miguel", "Test"],
    "edad": [20, 19, 22, 18, 100],
    "carrera": ["IN", "C", "NI", "IN", ""],
    "promedio": [90, 85, 70, 100, 100]
}

df_alumnos = pd.DataFrame(alumnos)

carrera = {
    "nombre": ["IN", "C", "NI", "A", "I"],
    "alumnos": [190, 1000, 300, 2000, 60],
    "creditos":[352, 350, 360, 326, 340]
}

df_carrera = pd.DataFrame(carrera)

# MERGE INNER, LEFT, RIGHT, OUTER
data = pd.merge(df_alumnos, df_carrera, how="outer",
         left_on="carrera", right_on="nombre",
                suffixes=("_alumnos","_carrera"))
#print(data)

# CONCATENATION

alumnos2 = {
    "nombre": ["Juan", "Maria", "Pedro", "Miguel", "Test"],
    "edad": [20, 19, 22, 18, 100],
    "carrera": ["IN", "C", "NI", "IN", ""],
    "promedio": [90, 85, 70, 100, 100]
}

df_alumnos2 = pd.DataFrame(alumnos2)
concatenar= pd.concat([df_alumnos, df_alumnos2],
                      axis="index", ignore_index=True)
#print(concatenar)


concatenar2= pd.concat([df_alumnos, df_alumnos2],
                      axis="columns")
#print(concatenar2)

