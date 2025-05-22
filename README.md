
# Análisis de Ventas Reales – Dataset Comercial

Este proyecto utiliza un dataset real de ventas para realizar análisis exploratorios y generar visualizaciones útiles para la toma de decisiones empresariales. Forma parte de un portafolio personal que aplica conocimientos de análisis de datos a un contexto profesional.

## 📌 Objetivo

Analizar un histórico de órdenes de ventas para:
- Identificar los productos más vendidos
- Evaluar el desempeño por país
- Observar la evolución mensual de las ventas

## 📁 Dataset

- Fuente: Dataset público simulado (`sales_data_sample.csv`)
- Registros: 2,823 transacciones
- Campos clave: PRODUCTLINE, COUNTRY, SALES, ORDERDATE

## 🛠 Tecnologías

- **Python**: procesamiento de datos
- **pandas**: transformación y agrupamiento
- **matplotlib**: visualización
- **Excel (xlsxwriter)**: consolidación de reportes

## 📊 Resultados Generados

- `reporte_ventas_reales.xlsx`: Reporte en Excel con hojas:
  - Top Productos
  - Ventas por País
  - Ventas Mensuales
  - Datos Crudos

- `top_productos_reales.png`: Gráfico de barras de productos más vendidos
- `ventas_pais.png`: Gráfico de barras horizontales por país
- `ventas_mensuales.png`: Gráfico de línea con evolución mensual

## ▶️ Uso

1. Instalar dependencias:
```bash
pip install pandas matplotlib xlsxwriter
```

2. Colocar `sales_data_sample.csv` en el directorio raíz.

3. Ejecutar el script:
```bash
python analisis_ventas_reales.py
```

4. Revisar los archivos de salida (.xlsx y .png).

## 👤 Autor

Richard Jiménez – Especialista en TI con enfoque analítico y orientación a la automatización y visualización de datos.
