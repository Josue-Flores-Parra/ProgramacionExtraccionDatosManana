import pandas as pd

d = { "articulo": ["Coca", "Tostitos", "Chetos", "Jugo"],
      "precio": [17, 35, 20, 22], "costo": [8, 17, 10, 11],
      "categoria": ["Bebida", "Botana", "Botana", "Bebida"]}

data = pd.DataFrame(d)
#print(data)

art = [
    ["Tostitos", 35, 17, "Botana"],
    ["Chetos",20, 10,"Botana"],
    ["Coca", 17, 8, "Bebida"],
    ["Jugo", 22, 11, "Bebida"]
]
data2 = pd.DataFrame(art, columns=["articulo", "precio",
                                   "costo", "tipo"])
#print(data2)

#print(type(data.articulo))
#print(data["articulo"])
columnas = ["articulo", "precio"]
#print(data[columnas])

# Calcular las Utilidades de cada producto (precio - costo)
utilidad = data.precio - data.costo
data["utilidad"] = utilidad
#print(data)

# Calcular que articulo(s) tienen el precio mayor de la categoria Bebidas
data_filtrado = data[data.categoria == "Bebida"]
maximo = data_filtrado.precio.max()
filtro = (data.precio == maximo) & (data.categoria == "Bebida")
#print(data[filtro][columnas])

# Calcular max, min, mean de las columnas precio, costo y devolverlo en un DF
columnas = ["precio", "costo"]
maximos = data[columnas].max()
minimos = data[columnas].min()
promedios = data[columnas].mean()
res = pd.DataFrame([maximos, minimos, promedios], index=["max", "min", "prom"])
print(res)
