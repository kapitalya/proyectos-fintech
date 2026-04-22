"""
descargar_datos.py
Descarga el IPC (inflación) de Bolivia desde la API del Banco Mundial.
No requiere cuenta ni API key — datos abiertos.
"""
import requests
import pandas as pd
import os

def descargar_inflacion_bolivia(inicio=2000, fin=2024):
    """
    Descarga inflación anual boliviana desde Banco Mundial (indicador FP.CPI.TOTL.ZG).
    Retorna DataFrame con columnas: año, inflacion_pct
    """
    url = (
        "https://api.worldbank.org/v2/country/BO/indicator/FP.CPI.TOTL.ZG"
        f"?date={inicio}:{fin}&format=json&per_page=100"
    )
    print(f"Descargando inflación Bolivia {inicio}-{fin} desde Banco Mundial...")
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()

    data = resp.json()[1]
    registros = [
        {"anio": int(d["date"]), "inflacion_pct": d["value"]}
        for d in data if d["value"] is not None
    ]
    df = pd.DataFrame(registros).sort_values("anio").reset_index(drop=True)
    print(f"✅ {len(df)} observaciones descargadas ({df['anio'].min()}-{df['anio'].max()})")
    return df


def descargar_ipc_mensual_bolivia():
    """
    Intenta descargar IPC mensual desde Banco Mundial.
    Indicador: FP.CPI.TOTL (base 2010=100)
    """
    url = (
        "https://api.worldbank.org/v2/country/BO/indicator/FP.CPI.TOTL"
        "?date=2000M01:2024M12&format=json&per_page=400&mrv=300"
    )
    print("Descargando IPC mensual Bolivia...")
    try:
        resp = requests.get(url, timeout=10)
        data = resp.json()[1]
        registros = []
        for d in data:
            if d["value"] is not None and "M" in str(d["date"]):
                anio, mes = d["date"].split("M")
                registros.append({
                    "fecha": pd.Timestamp(f"{anio}-{mes}-01"),
                    "ipc": float(d["value"])
                })
        df = pd.DataFrame(registros).sort_values("fecha").reset_index(drop=True)
        print(f"✅ {len(df)} observaciones mensuales descargadas")
        return df
    except Exception as e:
        print(f"⚠️  No se pudo obtener mensual: {e}")
        return None


if __name__ == "__main__":
    os.makedirs("datos", exist_ok=True)

    # Datos anuales
    df_anual = descargar_inflacion_bolivia()
    df_anual.to_csv("datos/inflacion_anual_bolivia.csv", index=False)
    print("💾 Guardado: datos/inflacion_anual_bolivia.csv")
    print(df_anual.tail())

    # Datos mensuales
    df_mensual = descargar_ipc_mensual_bolivia()
    if df_mensual is not None and len(df_mensual) > 0:
        df_mensual.to_csv("datos/ipc_mensual_bolivia.csv", index=False)
        print("💾 Guardado: datos/ipc_mensual_bolivia.csv")
