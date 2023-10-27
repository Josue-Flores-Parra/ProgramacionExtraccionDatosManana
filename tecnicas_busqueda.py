import pandas as pd

alumnos = {
    "nombre": ["Juan", "Maria", "Pedro", "Miguel"],
    "edad": [20, 19, 22, 18],
    "carrera": ["IN", "C", "NI", "IN"],
    "promedio": [90, 85, 70, 100]
}

df_alumnos = pd.DataFrame(alumnos)

# TECNICA 1. FILTRADO DE DATOS
c1 = df_alumnos.promedio > 80
data_c1 = df_alumnos[c1]
#print(data_c1)

c2 = (df_alumnos.promedio > 80) & (df_alumnos.carrera.isin(["IN", "C"]))
columnas = ["nombre", "carrera"]
data_c2 = df_alumnos[c2][columnas]
#print(data_c2)

# TECNICA 2. BUSQUEDA POR QUERY
query1_c1= df_alumnos.query("promedio > 80")
#print(query1_c1)

condicion = "promedio > 80 and carrera.isin(['IN', 'C'])"
query2_c2 = df_alumnos.query(condicion)
print(query2_c2[columnas])
