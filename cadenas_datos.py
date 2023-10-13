import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

alumnos = { "nombre": ["   Octavio", "   Maria   ", "Josue   ", "Selene"],
            "genero": ["IN", "F", "M", "F"],
            "escolaridad": ["Universidad", "Universidad", "Prepa", "Secundaria"]
        }

data = pd.DataFrame(alumnos)

data["nombre"] = data.nombre.str.strip().str.upper()
data["nom_min"] = data.nombre.str.lower()
data["nom_may"] = data.nombre.str.upper()
data["X"] = data.nombre.str.lower().str.replace("a", "X")

# Metodos de filtros
start_m = data.nombre.str.startswith("M")
#print(start_m)
#print(data[start_m])
end_e = data.nombre.str.endswith("E")
#print(end_e)
#print(data[end_e])
contiene_a = data.nombre.str.contains("A")
#print(data[contiene_a])

# Transformación de datos Nominales
one_hot_encoder = pd.get_dummies(data.genero)
print(one_hot_encoder)

data = data.join(one_hot_encoder)

# Transformar datos Ordinales
encoder = OrdinalEncoder(categories=[["Secundaria", "Prepa", "Universidad"]])
encoder.fit(data[["escolaridad"]])
data["educacion_encoder"] = encoder.transform(data[["escolaridad"]])

print(data)