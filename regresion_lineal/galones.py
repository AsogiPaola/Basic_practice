import pandas as pd
import matplotlib.pyplot as plt


ruta_csv = "data/galones_libra.csv"
data = pd.read_csv(ruta_csv)
#print(data.head())

x = data["Libras en miles (función)"]
y = data["Millas por galón (etiqueta)"]

plt.scatter(x,  y, color = "blue", alpha = 0.7, edgecolors='black')

plt.title("Grafica de relacion entre galone y libras")
plt.xlabel(" Libras en miles")
plt.ylabel(" Millas por galon")

plt.grid(True)
plt.show()
