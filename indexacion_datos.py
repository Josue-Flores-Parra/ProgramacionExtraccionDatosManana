import pandas as pd

alumnos = {
    "nombre": ["Juan", "Maria", "Pedro", "Miguel", "Juan"],
    "edad": [20, 19, 22, 18, 25],
    "carrera": ["IN", "C", "NI", "IN", "A"],
    "promedio": [90, 85, 70, 100, 95]
}

#df_alumnos = pd.DataFrame(alumnos, index=["A", "B", "C", "D"])
df_alumnos = pd.DataFrame(alumnos)
df_alumnos_index = df_alumnos.set_index("nombre", drop=True)
#print(df_alumnos_index)

df_reset = df_alumnos_index.reset_index()
#print(df_reset)

columnas = ["promedio", "carrera"]
#print(df_alumnos_index.loc[["Juan", "Maria"], columnas])

print(df_alumnos_index)
print(df_alumnos_index.iloc[0:4:2 , :])