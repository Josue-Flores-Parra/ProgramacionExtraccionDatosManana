import pandas as pd
from sqlalchemy import create_engine
from enum import Enum

#TODO: ESTUDIEN ENUMERACIONES
class DataBD(Enum):
    USER = "root"
    PASSWORD = "12345"
    NAME_BD = "olimpiadas"
    SERVER = "localhost"


cadena_conexion = f"mysql+mysqlconnector://{DataBD.USER.value}:" \
                  f"{DataBD.PASSWORD.value}@{DataBD.SERVER.value}/" \
                  f"{DataBD.NAME_BD.value}"
print(cadena_conexion)

engine = create_engine(cadena_conexion)
conexion = engine.connect()
#print(conexion)

datos_olimpiadas = pd.read_csv("datasets/data_olimpiadas.csv", index_col=0)
#print(datos_olimpiadas.sample(5))

genders = datos_olimpiadas.gender.unique()
#print(genders)

df_genders = pd.DataFrame(genders, columns=["nombre"])
#print(df_genders)
#df_genders.to_sql("genero", conexion, if_exists="append", index=False)

query = "Select nombre from genero where nombre = %s"
parametros = ("female",)
resultados = pd.read_sql(query, conexion, params=parametros)
print(resultados)



"""
for item in DataBD:
    print(item.name, item.value)
"""