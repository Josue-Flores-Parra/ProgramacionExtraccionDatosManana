import pandas as pd
import numpy as np
data = pd.read_csv("datasets/data_olimpiadas.csv",
                   index_col=0)
#print(data.sample(5))
datos_agrupados = data.groupby(["gender", "country"])

#print(datos_agrupados.get_group("female"))
columnas= ["gold", "silver", "bronze"]
res = datos_agrupados[columnas].sum()
#print(res)

#print(data.gender.value_counts())
#print(data.sort_values("year", ascending=False))

#print(data.mean(numeric_only=True))

#print(data.describe().transpose())
grupos = data.groupby(["gender","country"])
#print(grupos.gold.mean())
#print(grupos.gold.mean().unstack())

print(data.pivot_table("gold", index="gender",columns="year", margins=True, aggfunc=np.sum))