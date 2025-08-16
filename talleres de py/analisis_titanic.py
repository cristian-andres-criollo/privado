# -----------------------------------------------
# ANÁLISIS DE DATOS CON PYTHON - EVIDENCIA AA3-EV02
# Dataset: Titanic
# Autor: Cristian Andrés Criollo Tovar
# -----------------------------------------------

# 1. Importar librerías
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Leer el dataset
df = pd.read_csv("titanic.csv")
print("Primeros 5 registros:")
print(df.head())

# 3. Ver estructura del dataset y datos faltantes
print("\nInformación general:")
print(df.info())

print("\nValores nulos por columna:")
print(df.isnull().sum())

# 4. Eliminar filas con datos nulos
df_cleaned = df.dropna()
print("\nCantidad de filas luego de eliminar nulos:", len(df_cleaned))

# 5. Estadísticas básicas
print("\nResumen estadístico:")
print(df_cleaned.describe())

print("\nConteo de pasajeros por clase (Pclass):")
print(df_cleaned["Pclass"].value_counts())

# 6. Agrupamiento y ordenamiento
print("\nPromedio de edad por género:")
print(df_cleaned.groupby("Sex")["Age"].mean())

print("\nPasajeros más viejos ordenados por edad:")
df_sorted = df_cleaned.sort_values(by="Age", ascending=False)
print(df_sorted[["Name", "Age"]].head())

# 7. Gráfico de barras: Supervivencia por género
sns.set(style="whitegrid")
plt.figure(figsize=(8, 5))
sns.countplot(x="Sex", hue="Survived", data=df_cleaned)
plt.title("Supervivencia por género")
plt.xlabel("Género")
plt.ylabel("Cantidad")
plt.legend(title="Supervivencia", labels=["No", "Sí"])
plt.tight_layout()
plt.show()

# 8. (Opcional) Guardar los datos limpios
df_cleaned.to_csv("titanic_limpio.csv", index=False)
