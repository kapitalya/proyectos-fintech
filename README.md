# 📈 Análisis de Portafolio de Activos — Mercado LATAM

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=flat&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat&logo=jupyter&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-2.1-150458?style=flat&logo=pandas&logoColor=white)
![scipy](https://img.shields.io/badge/scipy-1.11-8CAAE6?style=flat)
![Status](https://img.shields.io/badge/Estado-Activo-brightgreen)

Análisis cuantitativo de riesgo/retorno sobre activos financieros representativos del mercado latinoamericano. Aplica teoría de portafolio de Markowitz y simulación Monte Carlo para identificar la asignación óptima de activos.

---

## 🎯 Problema

Un inversor boliviano con acceso a ETFs internacionales necesita responder:
- ¿Qué activos ofrecen mejor retorno ajustado al riesgo?
- ¿Cómo diversificar para reducir volatilidad sin sacrificar retorno?
- ¿Cuánto puedo perder en un día malo (VaR)?

---

## 📐 Metodología

| Técnica | Descripción | Por qué |
|---|---|---|
| **Retornos logarítmicos** | `ln(P_t / P_{t-1})` | Aditivos en el tiempo, mejor comportamiento estadístico |
| **Sharpe Ratio** | `(R - Rf) / σ` | Mide retorno por unidad de riesgo asumido |
| **VaR paramétrico 95%** | Pérdida máxima diaria esperada | Cuantifica riesgo de cola |
| **Monte Carlo (20k portafolios)** | Pesos aleatorios normalizados | Mapea espacio completo riesgo/retorno |
| **Frontera eficiente** | Portafolios óptimos de Markowitz | Identifica la mejor combinación posible |

---

## 📊 Activos Analizados

| Ticker | Instrumento | Exposición |
|---|---|---|
| `ILF` | iShares Latin America 40 ETF | Acciones LATAM top 40 |
| `EEM` | iShares MSCI Emerging Markets | Mercados emergentes globales |
| `GLD` | SPDR Gold ETF | Oro — activo refugio |
| `SLV` | iShares Silver ETF | Plata — commodity industrial |
| `IEF` | iShares 7-10 Year Treasury | Renta fija USA |

> Estos activos son accesibles desde Bolivia vía brokers internacionales y sirven como referencia para análisis de diversificación regional.

---

## 📁 Estructura

```
portafolio-acciones-bolivia/
├── analisis_portafolio.ipynb   # Notebook principal — análisis completo
├── requirements.txt
├── .gitignore
├── img/                        # Gráficas exportadas (generadas al correr)
│   ├── 01_precios_y_distribuciones.png
│   ├── 02_correlaciones.png
│   └── 03_frontera_eficiente.png
└── README.md
```

---

## ⚙️ Instalación

```bash
git clone https://github.com/Serius69/portafolio-acciones-bolivia
cd portafolio-acciones-bolivia

python -m venv venv
source venv/bin/activate      # Linux/Mac
# venv\Scripts\activate       # Windows

pip install -r requirements.txt
mkdir img

jupyter lab analisis_portafolio.ipynb
```

Ejecutar todas las celdas en orden. Los datos se descargan automáticamente desde Yahoo Finance.

---

## 📈 Resultados Esperados

El notebook genera tres visualizaciones:

**1. Evolución de precios normalizados + distribución de retornos**
Muestra el comportamiento histórico de cada activo y si sus retornos siguen una distribución normal (test Jarque-Bera).

**2. Matriz de correlaciones**
Identifica qué activos se mueven juntos y dónde hay oportunidad real de diversificación.

**3. Frontera eficiente (Monte Carlo)**
20,000 portafolios simulados coloreados por Sharpe Ratio. Marca el portafolio de máximo Sharpe (⭐) y mínima volatilidad (◆).

---

## 🔗 Contexto Bolivia

Bolivia no tiene mercado de valores desarrollado (la BBV tiene liquidez muy baja). Este análisis usa ETFs internacionales como proxy para estudiar diversificación desde el contexto boliviano, donde el dólar paralelo y la inflación hacen especialmente relevante el análisis de activos refugio como GLD.

Ver también: [💱 Dólar Paralelo Bolivia — ARIMA](https://github.com/Serius69/dolar-paralelo-bolivia-arima)

---

## 👤 Autor

**Sergio** — Data Scientist en Finanzas | [github.com/Serius69](https://github.com/Serius69)
