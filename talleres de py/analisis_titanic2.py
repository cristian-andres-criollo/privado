# ------------------------------------------------------
# ANÁLISIS DE DATOS EN UNA SOLA VENTANA CON SUBPLOTS
# ------------------------------------------------------
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv("titanic.csv")

# Limpiar eliminando filas con datos nulos
df_clean = df.dropna()

# Crear una figura con 3 subgráficos (1 fila, 3 columnas)
fig, axs = plt.subplots(1, 3, figsize=(18, 5))  # 1 fila, 3 columnas

# 📊 Gráfico 1: Supervivencia por género
sns.countplot(x="Sex", hue="Survived", data=df_clean, ax=axs[0])
axs[0].set_title("Supervivencia por género")
axs[0].set_xlabel("Género")
axs[0].set_ylabel("Cantidad")
axs[0].legend(title="¿Sobrevivió?", labels=["No", "Sí"])

# 📊 Gráfico 2: Histograma de edades
axs[1].hist(df_clean["Age"], bins=20, color='skyblue', edgecolor='black')
axs[1].set_title("Distribución de edades")
axs[1].set_xlabel("Edad")
axs[1].set_ylabel("Cantidad")

# 📊 Gráfico 3: Boxplot de edad por clase
sns.boxplot(x="Pclass", y="Age", data=df_clean, ax=axs[2])
axs[2].set_title("Boxplot de edad por clase")
axs[2].set_xlabel("Clase")
axs[2].set_ylabel("Edad")

# Ajustar los espacios entre gráficos
plt.tight_layout()

# Mostrar todo en una sola ventana
plt.show()
