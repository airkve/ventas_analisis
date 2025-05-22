
import pandas as pd
import matplotlib.pyplot as plt

# Cargar dataset
df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"], errors="coerce")
df["MES"] = df["ORDERDATE"].dt.to_period("M").astype(str)

# Análisis
top_productos = df.groupby("PRODUCTLINE")["QUANTITYORDERED"].sum().sort_values(ascending=False)
ventas_pais = df.groupby("COUNTRY")["SALES"].sum().sort_values(ascending=False)
ventas_mensuales = df.groupby("MES")["SALES"].sum().sort_index()

# Gráficos
top_productos.plot(kind="bar", figsize=(10,5), title="Productos más vendidos por categoría")
plt.ylabel("Cantidad Vendida")
plt.tight_layout()
plt.savefig("top_productos_reales.png")
plt.close()

ventas_pais.plot(kind="barh", figsize=(10,6), title="Ingresos por país")
plt.xlabel("Ventas Totales (USD)")
plt.tight_layout()
plt.savefig("ventas_pais.png")
plt.close()

ventas_mensuales.plot(kind="line", marker="o", figsize=(12,5), title="Evolución mensual de las ventas")
plt.ylabel("Ventas (USD)")
plt.grid(True)
plt.tight_layout()
plt.savefig("ventas_mensuales.png")
plt.close()

# Exportar resultados
with pd.ExcelWriter("reporte_ventas_reales.xlsx", engine="xlsxwriter") as writer:
    top_productos.to_frame("Cantidad Vendida").to_excel(writer, sheet_name="Top Productos")
    ventas_pais.to_frame("Ventas Totales").to_excel(writer, sheet_name="Ventas por País")
    ventas_mensuales.to_frame("Ventas Mensuales").to_excel(writer, sheet_name="Ventas Mensuales")
    df.to_excel(writer, sheet_name="Datos Crudos", index=False)
