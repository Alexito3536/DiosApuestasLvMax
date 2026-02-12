import pandas as pd
import numpy as np
import json
import time
from sklearn.ensemble import GradientBoostingClassifier

# --- 1. EL CEREBRO IA (Entrenamiento de Élite) ---
def entrenar_IA():
    np.random.seed(99)
    n = 30000
    data = {
        'f_ataque': np.random.uniform(0.5, 4.5, n),
        'f_defensa': np.random.uniform(0.5, 3.5, n),
        'lesiones': np.random.randint(0, 3, n),
        'presion': np.random.uniform(-1, 1, n),
        'h2h': np.random.uniform(0, 1, n)
    }
    df = pd.DataFrame(data)
    df['win'] = ((df['f_ataque'] * 1.5 - df['f_defensa'] * 0.7) - (df['lesiones'] * 0.6) > 2.2).astype(int)
    return GradientBoostingClassifier(n_estimators=300).fit(df.drop('win', axis=1), df['win'])

# --- 2. EL SCRAPER NIVEL DIOS ---
def ejecutar_scraper_maestro():
    print("🕵️ Activando Scraper Silencioso...")
    # Aquí es donde el script "navega". Para GitHub Actions usamos headless mode.
    # Simulamos la captura de datos de una web de resultados (ej. Flashscore/FBRef)
    
    # DATOS CAPTURADOS (Simulando la salida del Scraper tras procesar el HTML)
    datos_sucios = [
        {"partido": "Man. City vs Everton", "ataque": 4.4, "defensa": 0.6, "h2h": 0.98},
        {"partido": "Arsenal vs Brentford", "ataque": 3.9, "defensa": 1.1, "h2h": 0.85},
        {"partido": "Liverpool vs Wolves", "ataque": 4.1, "defensa": 0.7, "h2h": 0.90},
        {"partido": "Aston Villa vs Fulham", "ataque": 3.1, "defensa": 1.5, "h2h": 0.60}
    ]
    return datos_sucios

# --- 3. PROCESAMIENTO Y GENERACIÓN ---
modelo = entrenar_IA()
partidos_crudos = ejecutar_scraper_maestro()
resultados_finales = []

for p in partidos_crudos:
    # Convertimos los datos del scraper al formato de la IA
    stats = [p['ataque'], p['defensa'], 0, 0.8, p['h2h']] # Lesiones y Presión por defecto
    prob = modelo.predict_proba([stats])[0][1]
    
    cat = "DIOS" if prob >= 0.98 else "EXTRA"
    mrc = "Hándicap -1.5" if p['ataque'] > 4.0 else "Gana Local"
    
    resultados_finales.append({
        "partido": p['partido'],
        "confianza": round(prob * 100, 2),
        "mercado": mrc,
        "categoria": cat,
        "stake": "10%" if cat == "DIOS" else "3%"
    })

with open('data.json', 'w') as f:
    json.dump(resultados_finales, f, indent=4)
print("🚀 Web actualizada con datos del Scraper.")
