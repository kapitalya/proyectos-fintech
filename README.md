# Proyectos Fintech — análisis cuantitativo (notebooks)

> Tres notebooks de análisis financiero y crediticio con datos abiertos (portafolio, inflación de Bolivia y scoring de crédito). Para analistas y estudiantes de finanzas cuantitativas.

**Estado (2026-11-17):** PARCIAL — tres notebooks y un script de descarga presentes; sin `requirements.txt`, `.gitignore` ni licencia; los notebooks no tienen outputs guardados, así que sus resultados no son verificables en el repo; `datos/` no está incluido (lo genera `descargar_datos.py`, salvo `cs-training.csv`, que hay que colocar a mano).
**Repo:** kapitalya/proyectos-fintech · **Rama por defecto:** main · **Alias/nombres anteriores:** el README anterior citaba una carpeta `portafolio-acciones-bolivia/` que no existe en este repo.

> Aviso: análisis educativo, no es consejo financiero. Markowitz, VaR y Monte Carlo son ejercicios ilustrativos; no recomiendan ninguna inversión.

## Qué hace

- `analisis_portafolio.ipynb`: descarga precios con `yfinance` (diccionario `TICKERS`, con los ETF ILF, EEM, GLD, SLV e IEF según el README anterior; lista exacta sin verificar en el notebook). Calcula retornos logarítmicos, Sharpe, VaR, prueba Jarque-Bera, simulación Monte Carlo (`N_SIMULACIONES = 20_000`) y frontera eficiente.
- `inflacion_bolivia_sarima.ipynb`: lee `datos/inflacion_anual_bolivia.csv`, aplica pruebas ADF, KPSS y Ljung-Box, descomposición estacional, filtro HP, ACF/PACF y búsqueda por AIC de parámetros SARIMAX.
- `scoring_credito.ipynb`: lee `datos/cs-training.csv` (no incluido), entrena regresión logística, Random Forest y Gradient Boosting, calcula AUC-ROC y Average Precision, y una curva de calibración.
- `descargar_datos.py`: descarga desde la API del Banco Mundial el indicador `FP.CPI.TOTL.ZG` (inflación anual de Bolivia, 2000–2024) y guarda `datos/inflacion_anual_bolivia.csv`. Contiene además una función de IPC mensual (indicador `FP.CPI.TOTL`) que no guarda ningún archivo.

## Stack

Python. Librerías importadas por los notebooks y el script: `numpy`, `pandas`, `scipy`, `matplotlib`, `seaborn`, `yfinance` (portafolio); `statsmodels` (inflación); `scikit-learn` (scoring); `requests` (script de descarga). Jupyter Notebook.

## Estructura

```
proyectos-fintech/
├── analisis_portafolio.ipynb        # Portafolio: Markowitz, VaR, Monte Carlo
├── inflacion_bolivia_sarima.ipynb   # Inflación Bolivia (SARIMA)
├── scoring_credito.ipynb            # Scoring crediticio (requiere datos/cs-training.csv)
├── descargar_datos.py               # Descarga inflación Bolivia (Banco Mundial) a datos/
├── mnt/                             # Artefactos de sandbox con READMEs anidados (no forman parte del proyecto)
└── README.md
```

`datos/` e `img/` no existen en el repo: los crea `descargar_datos.py` (`datos/`) o el usuario. La carpeta `mnt/user-data/outputs/` contiene READMEs anidados que describen otro proyecto; se conservan sin cambios en este PR.

## Instalación y uso

```bash
git clone https://github.com/kapitalya/proyectos-fintech
cd proyectos-fintech

python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install numpy pandas scipy matplotlib seaborn yfinance statsmodels scikit-learn requests jupyter   # sin requirements.txt: versiones sin fijar

python descargar_datos.py         # crea datos/inflacion_anual_bolivia.csv
jupyter lab analisis_portafolio.ipynb
```

- `analisis_portafolio.ipynb` descarga precios de Yahoo Finance al ejecutarse; no necesita archivos locales.
- `inflacion_bolivia_sarima.ipynb` requiere antes `python descargar_datos.py`.
- `scoring_credito.ipynb` requiere colocar `datos/cs-training.csv` manualmente. El origen del archivo no está en el repo (sin verificar; el nombre corresponde al dataset Give Me Some Credit).

Ejecutar las celdas en orden. Sin verificar: que los notebooks corran sin errores con las versiones actuales de las librerías.

## Variables de entorno (solo nombres)

Ninguna. No hay `.env.example` en el repo y ningún script lee variables de entorno.

## Pruebas y CI

- Sin pruebas automatizadas ni workflows de CI en el repo.

### Resultados

- Los notebooks no tienen outputs guardados. Calculan AUC-ROC, Average Precision, Sharpe, VaR y la frontera eficiente, pero sus valores no se pueden verificar desde el repo. Las cifras del README anterior (AUC ~0.856 / ~0.866 en scoring) se retiran.
- Resultados no verificables en el repo; para reproducirlos, ejecutar los notebooks.

## Despliegue

No aplica: notebooks y scripts de ejecución local.

## Estado y relaciones

- Repositorio independiente. Agrupa tres análisis distintos (portafolio, inflación, scoring); separarlos en repos propios está pendiente de decisión del dueño.
- El README anterior enlazaba `Serius69/dolar-paralelo-bolivia-arima`, repo de una cuenta personal fuera de la organización; no auditado en este corte.

## Precios y planes

No aplica (repositorio de análisis, sin venta). Precios y planes: fuente única `Vault/EMPRESA/portafolio/PRECIOS-APROBADOS-20261108.md`.

## Seguridad, privacidad y derechos

- Sin secretos en el repo.
- Fuentes de datos: Yahoo Finance (vía `yfinance`), API del Banco Mundial y el dataset de `cs-training.csv`. Cada una sujeta a sus términos de uso; no verificados en este corte.
- Licencia: el repo no tiene archivo LICENSE; no hay derechos de reutilización declarados.

## Convenciones de trabajo

Cambios por rama `codex/*` y PR contra `main` (el repo no tiene rama `develop`). CI: no hay workflows configurados.
