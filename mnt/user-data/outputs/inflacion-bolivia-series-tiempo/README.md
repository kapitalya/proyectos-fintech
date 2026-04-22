# 🇧🇴 Inflación Bolivia — Modelado SARIMA y Proyecciones

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=flat&logo=python&logoColor=white)
![statsmodels](https://img.shields.io/badge/statsmodels-0.14-3498DB?style=flat)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat&logo=jupyter&logoColor=white)
![Fuente](https://img.shields.io/badge/Datos-Banco%20Mundial-009EDB?style=flat)
![Status](https://img.shields.io/badge/Estado-Activo-brightgreen)

Análisis de series de tiempo de la inflación boliviana (2000-2024). Descomposición de tendencia, selección automática de parámetros ARIMA y proyecciones con intervalos de confianza al 80% y 95%.

---

## 🎯 Objetivo

Construir un modelo ARIMA para la inflación boliviana que permita:
- Entender la tendencia histórica y eventos macroeconómicos clave
- Proyectar inflación con rangos de incertidumbre honestos
- Demostrar el pipeline completo de modelado de series de tiempo

---

## 📊 Datos

**Fuente:** Banco Mundial — Indicador `FP.CPI.TOTL.ZG` (Bolivia)  
**Período:** 2000-2024 | **Frecuencia:** Anual  
**Descarga:** Automática vía API pública (sin API key)

```bash
python descargar_datos.py   # Descarga y guarda en datos/
```

---

## 📐 Metodología

```
Serie histórica
       ↓
1. Descomposición HP   → Tendencia + Ciclo
       ↓
2. Test ADF + KPSS     → ¿Es estacionaria? ¿Cuántas diferencias?
       ↓
3. ACF / PACF          → Candidatos para p y q
       ↓
4. Grid search AIC     → Selección automática ARIMA(p,d,q)
       ↓
5. Diagnóstico         → Ljung-Box + normalidad de residuos
       ↓
6. Forecast            → Proyección con IC 80% y 95%
```

---

## 📁 Estructura

```
inflacion-bolivia-series-tiempo/
├── inflacion_bolivia_sarima.ipynb   # Notebook principal
├── descargar_datos.py               # Script de descarga automática
├── requirements.txt
├── .gitignore
├── datos/                           # Generado al correr descargar_datos.py
│   ├── inflacion_anual_bolivia.csv
│   └── ipc_mensual_bolivia.csv
├── img/                             # Gráficas exportadas
│   ├── 01_inflacion_historica.png
│   ├── 02_descomposicion.png
│   ├── 03_acf_pacf.png
│   ├── 04_diagnostico_residuos.png
│   └── 05_forecast_inflacion.png
└── README.md
```

---

## ⚙️ Instalación

```bash
git clone https://github.com/Serius69/inflacion-bolivia-series-tiempo
cd inflacion-bolivia-series-tiempo

python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
mkdir -p datos img

# Descargar datos automáticamente
python descargar_datos.py

# Abrir notebook
jupyter lab inflacion_bolivia_sarima.ipynb
```

---

## 🧠 Decisiones Técnicas

**¿Por qué ADF y KPSS juntos?**  
ADF y KPSS tienen hipótesis nulas opuestas. Usarlos juntos evita conclusiones erróneas: si ambos coinciden, la evidencia es sólida. Si contradicen, hay que diferenciar con cautela.

**¿Por qué Hodrick-Prescott para la tendencia?**  
Más robusto que una media móvil simple para series cortas con shocks. Con `λ=100` para datos anuales según la recomendación de la literatura económica (Hodrick & Prescott, 1997).

**¿Por qué los intervalos de confianza se amplían tanto?**  
Los datos anuales tienen pocas observaciones (~25). Con ARIMA, la incertidumbre crece proporcionalmente al horizonte de forecast. Esto es honesto — no falsa precisión.

---

## 🔗 Proyectos Relacionados

- [💱 Dólar Paralelo Bolivia — ARIMA](https://github.com/Serius69/dolar-paralelo-bolivia-arima) — Mismo enfoque, datos del mercado paralelo
- [📈 Portafolio de Activos BO](https://github.com/Serius69/portafolio-acciones-bolivia) — Análisis macroeconómico complementario

---

## 👤 Autor

**Sergio** — Data Scientist en Finanzas | [github.com/Serius69](https://github.com/Serius69)
