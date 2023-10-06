import pandas as pd

datos = pd.read_csv("datasets/surveys.csv")
#print(datos.sample(10))
nulos = datos.isnull()
#print(nulos.any())
#print(nulos.sum())
#print(nulos.sum().sum())
#print(nulos.sum()/len(nulos))

# Eliminar columnas
datos_eliminados = datos.drop(["day", "month"], axis="columns" )
#print(datos.columns)
#print(datos_eliminados.columns)

# Eliminar columnas original
datos.drop(["day", "month"], axis="columns", inplace=True)
#print(datos.columns)

# Eliminar renglones
datos_row_eliminados= datos.drop([2,3,4], axis="index")
#print(datos_row_eliminados.head(10))

# Eliminar Nulos
datos_no_nulos= datos.dropna(axis="index", subset=["hindfoot_length", "sex"])
#print(len(datos))
#print(len(datos_no_nulos))

# LLenar valores nulos
columnas = ["hindfoot_length","weight"]
promedios = datos[columnas].mean()
#print(promedios)
datos_llenos = datos.fillna(promedios)
#print(datos_llenos)

# Llenar valores nulos usando bfill
datos_bfill = datos.bfill()
#print(datos_bfill)

# LLenar valores nulos usando ffill
datos_ffill = datos.ffill()
#print(datos_ffill)

# Llenar valores nulos MIX
datos_mix = datos.bfill().ffill()
#print(datos_mix)

# VERIFICAR DUPLICADOS
duplicados= datos.duplicated()
#print(duplicados)

eliminar_duplicados= datos.drop_duplicates()
print(len(datos))
print(len(eliminar_duplicados))