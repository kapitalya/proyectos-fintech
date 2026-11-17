# Proyectos Fintech — análisis cuantitativo (notebooks)

> Colección de notebooks de análisis financiero y crediticio con datos abiertos, orientada a LATAM y Bolivia. Para analistas y estudiantes de finanzas cuantitativas.

**Estado (2026-11-17):** PARCIAL — tres notebooks y un script de descarga presentes; sin `requirements.txt`, `.gitignore` ni licencia; notebooks sin outputs guardados (resultados no verificables en el repo); el README anterior describía una carpeta `portafolio-acciones-bolivia/` que no existe en el repo.
**Repo:** kapitalya/proyectos-fintech · **Rama por defecto:** main · **Alias/nombres anteriores:** `portafolio-acciones-bolivia` (solo en el README anterior, sin verificar en el historial)

> Aviso: análisis educativo, no es consejo financiero. Las técnicas (Markowitz, VaR, Monte Carlo) son ilustrativas y no recomiendan ninguna inversión.

## Qué hace

- `analisis_portafolio.ipynb`: descarga precios de cinco ETFs con `yfinance` (ILF, EEM, GLD, SLV, IEF), calcula retornos logarítmicos, Sharpe, VaR paramétrico e histórico al 95%, prueba Jarque-Bera, simulación Monte Carlo (`N_SIMULACIONES = 20_000`) y frontera eficiente de Markowitz.
- `inflacion_bolivia_sarima.ipynb`: modelado de inflación de Bolivia con SARIMA. Sin verificar en detalle: el notebook no se revisó línea por línea.
- `scoring_credito.ipynb`: scoring de riesgo crediticio (dataset Give Me Some Credit) comparando regresión logística y Random Forest con AUC y Average Precision. Requiere `datos/cs-training.csv`, que no está en el repo.
- `descargar_datos.py`: descarga la serie de inflación anual de Bolivia (indicador `FP.CPI.TOTL.ZG` del Banco Mundial) y el IPC mensual, y los guarda en `datos/`. No requiere API key.

## Stack

Python, Jupyter Notebook, `yfinance`, `pandas`, `numpy`, `scipy`, `requests`. Librerías exactas de los notebooks: sin verificar (no hay `requirements.txt`).

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

La carpeta `mnt/user-data/outputs/` contiene READMEs anidados que describen otro proyecto. Se conservan sin cambios en este PR; no son documentación de este repo.

## Instalación y uso

```bash
git clone https://github.com/kapitalya/proyectos-fintech
cd proyectos-fintech

python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install pandas numpy scipy yfinance requests jupyter   # sin requirements.txt: versiones sin fijar

python descargar_datos.py         # crea datos/ y guarda la serie de inflación
jupyter lab analisis_portafolio.ipynb
```

Los precios del portafolio se descargan desde Yahoo Finance al ejecutar el notebook. `scoring_credito.ipynb` exige colocar `datos/cs-training.csv` manualmente. Ejecutar las celdas en orden.

## Variables de entorno (solo nombres)

Ninguna. No hay `.env.example` en el repo y ningún script lee variables de entorno.

## Pruebas y CI

Sin pruebas automatizadas ni workflows de CI en el repo.

## Despliegue

No aplica: los artefactos son notebooks y scripts de ejecución local.

## Resultados

Los notebooks no tienen outputs guardados. Las cifras que el README anterior citaba (por ejemplo, AUC ~0.856 / ~0.866 en scoring) no son verificables desde el repo. Resultados no verificables en el repo; para reproducirlos, ejecutar los notebooks.

## Estado y relaciones

- Relación con otros repos de Kapitalya: el README anterior enlazaba `Serius69/dolar-paralelo-bolivia-arima`, repo de una cuenta personal fuera de la organización; no auditado en este corte.
- Este repo agrupa tres análisis distintos (portafolio, inflación, scoring). La separación en repos propios está pendiente de decisión del dueño.

## Precios y planes

No aplica (repositorio de análisis, sin venta). Precios y planes: fuente única `Vault/EMPRESA/portafolio/PRECIOS-APROBADOS-20261108.md`.

## Seguridad, privacidad y derechos

- Sin secretos en el repo.
- Datos de Yahoo Finance (vía `yfinance`), Banco Mundial y Give Me Some Credit: sujetos a los términos de sus proveedores. Sin verificar términos en este corte.
- Licencia: el repo no tiene archivo LICENSE; no hay derechos de reutilización declarados.

## Convenciones de trabajo

Cambios por rama `codex/*` y PR contra `main` (el repo no tiene rama `develop`). CI: no hay workflows configurados.
