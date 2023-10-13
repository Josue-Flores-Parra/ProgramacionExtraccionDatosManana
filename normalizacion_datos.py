import pandas as pd

personas= { "salario": [20000, 10000, 40000, 25000, 60000],
            "edad": [20, 18, 35, 40, 45]}

data = pd.DataFrame(personas)

# CALCULO Z-SCORE X= (Xi - promedio) / std
prom_salario = data.salario.mean()
std_salario = data.salario.std()
data["zscore_salario"] = (data.salario - prom_salario) / std_salario

prom_edad = data.edad.mean()
std_edad = data.edad.std()
data["zscore_edad"] = (data.edad - prom_edad) / std_edad

# CALCULO MIN-MAX X= (xi - min) /(max - min)
min_salario = data.salario.min()
max_salario = data.salario.max()
data["minmax_salario"] = (data.salario - min_salario)/(max_salario - min_salario)

min_edad = data.edad.min()
max_edad = data.edad.max()
data["minmax_edad"] = (data.edad - min_edad)/(max_edad - min_edad)

# ESCALADO SIMPLE X= (Xi) / max
data["es_salario"] = data.salario / max_salario
data["es_edad"] = data.edad / max_edad

print(data)