# 💳 Scoring de Crédito — Clasificación de Riesgo Fintech

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=flat&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat&logo=jupyter&logoColor=white)
![Dataset](https://img.shields.io/badge/Dataset-Kaggle-20BEFF?style=flat&logo=kaggle&logoColor=white)
![Status](https://img.shields.io/badge/Estado-Activo-brightgreen)

Pipeline completo de machine learning para clasificación de riesgo crediticio. Desde EDA hasta selección de umbral óptimo basada en costos de negocio reales.

---

## 🎯 Problema de Negocio

En fintech, aprobar a un cliente moroso cuesta mucho más que rechazar a un buen cliente. Un modelo que solo optimiza *accuracy* puede tener 93% de accuracy simplemente prediciendo "nadie hará mora" — y sería inútil.

Este proyecto demuestra cómo **las métricas de negocio importan más que las métricas de accuracy** en modelos de riesgo crediticio.

---

## 📊 Dataset

**Give Me Some Credit** — Kaggle Competition  
150,000 prestatarios reales con 10 variables financieras.

| Variable | Descripción |
|---|---|
| `target` | 1 = mora ≥90 días en próximos 2 años |
| `util_credito` | % utilizado de líneas de crédito revolving |
| `edad` | Edad del prestatario |
| `mora_30_59` | Veces con 30-59 días de atraso |
| `ratio_deuda` | Deuda total / ingreso mensual |
| `ingreso_mensual` | Ingreso mensual (29% valores nulos) |
| `lineas_credito` | Número de líneas de crédito abiertas |
| `mora_90` | Veces con 90+ días de atraso |

📥 [Descargar dataset en Kaggle](https://www.kaggle.com/c/GiveMeSomeCredit/data) → guardar como `datos/cs-training.csv`

---

## 🧠 Pipeline

```
1. EDA             → Distribuciones, nulos, correlaciones
       ↓
2. Preprocessing   → Imputación por grupo de edad, tratamiento outliers
       ↓
3. Feature Eng.    → total_moras, ingreso_por_linea, carga_deuda
       ↓
4. Modelos         → Logistic Regression vs Random Forest
       ↓
5. Evaluación      → AUC-ROC, Precision-Recall (no accuracy)
       ↓
6. Umbral óptimo   → Minimizar costo total con FN=5×FP
```

---

## 📐 Decisiones Técnicas Clave

**¿Por qué AUC-ROC en vez de accuracy?**  
El dataset tiene ~6.7% de mora. Un modelo que prediga siempre "paga" tiene 93.3% de accuracy pero AUC=0.5 — completamente inútil. AUC mide la capacidad real de discriminar.

**¿Por qué el umbral no es 0.5?**  
En crédito, rechazar erroneamente a un buen cliente (FP) cuesta 1 unidad. Aprobar a un moroso (FN) cuesta 5 unidades. El umbral óptimo se calcula minimizando `costo = FN×5 + FP×1`.

**¿Por qué Random Forest con `class_weight='balanced'`?**  
Sin balanceo, el modelo ignora la clase minoritaria (mora). `class_weight='balanced'` pondera automáticamente cada clase según su frecuencia.

---

## 📁 Estructura

```
scoring-credito-fintech-latam/
├── scoring_credito.ipynb    # Notebook principal — pipeline completo
├── requirements.txt
├── .gitignore
├── datos/                   # Carpeta para el CSV de Kaggle (no incluido)
│   └── .gitkeep
├── img/                     # Gráficas exportadas
│   ├── 01_eda_variables.png
│   ├── 02_curvas_roc_pr.png
│   ├── 03_umbral_optimo.png
│   └── 04_feature_importance.png
└── README.md
```

---

## ⚙️ Instalación

```bash
git clone https://github.com/Serius69/scoring-credito-fintech-latam
cd scoring-credito-fintech-latam

python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
mkdir -p datos img

# Descargar cs-training.csv de Kaggle y colocarlo en datos/
jupyter lab scoring_credito.ipynb
```

---

## 📈 Resultados

| Modelo | AUC-ROC | Avg Precision |
|---|---|---|
| Logistic Regression | ~0.856 | ~0.298 |
| Random Forest | ~0.866 | ~0.312 |

> Los resultados exactos varían según la versión del dataset descargado.

---

## 🔗 Proyectos Relacionados

- [💱 Dólar Paralelo Bolivia — ARIMA](https://github.com/Serius69/dolar-paralelo-bolivia-arima) — Series de tiempo
- [📈 Portafolio de Activos BO](https://github.com/Serius69/portafolio-acciones-bolivia) — Riesgo/retorno

---

## 👤 Autor

**Sergio** — Data Scientist en Finanzas | [github.com/Serius69](https://github.com/Serius69)
