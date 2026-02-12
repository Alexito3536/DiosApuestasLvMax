import pandas as pd
import numpy as np
import json
import requests
from sklearn.ensemble import GradientBoostingClassifier

# --- 1. ENTRENAMIENTO (Cerebro IA) ---
np.random.seed(99)
n = 30000
data = {'f_ataque': np.random.uniform(0.5, 4.5, n), 'f_defensa': np.random.uniform(0.5, 3.5, n),
        'lesiones': np.random.randint(0, 3, n), 'presion': np.random.uniform(-1, 1, n), 'h2h': np.random.uniform(0, 1, n)}
df = pd.DataFrame(data)
df['win'] = ((df['f_ataque'] * 1.5 - df['f_defensa'] * 0.7) - (df['lesiones'] * 0.6) > 2.2).astype(int)
model = GradientBoostingClassifier(n_estimators=300).fit(df.drop('win', axis=1), df['win'])

# --- 2. CAZADOR AUTOMÁTICO DE PARTIDOS (Web Scraping / API) ---
def obtener_partidos_automaticos():
    print("🌐 Buscando partidos en la red...")
    # Intentamos conectar con una fuente de datos gratuita de la Premier League
    # Si la fuente falla, usamos una lista de respaldo para que la web no quede vacía
    try:
        # Aquí conectamos con un feed de datos (Ejemplo: API-Football o similar)
        # Por ahora, simulamos la respuesta del scraper para que veas la estructura
        url = "https://fixturedownload.com/feed/json/epl-2025" # Ejemplo de feed real
        # r = requests.get(url)
        # data_real = r.json()
        
        # Procesamos los datos para darles el formato que la IA entiende
        return [
            {"eq": "Manchester City vs Everton", "stats": [4.1, 0.7, 0, 0.9, 0.9]},
            {"eq": "Arsenal vs Brentford", "stats": [3.8, 1.2, 0, 0.8, 0.85]},
            {"eq": "Liverpool vs Wolves", "stats": [4.3, 0.6, 1, 0.95, 0.9]}
        ]
    except:
        return []

# --- 3. PROCESAMIENTO ---
partidos_hoy = obtener_partidos_automaticos()
resultados_finales = []

for p in partidos_hoy:
    prob = model.predict_proba([p['stats']])[0][1]
    categoria = "DIOS" if prob >= 0.95 else "EXTRA"
    mercado = "Hándicap -1.5" if p['stats'][0] > 4.0 else "Gana Local"
    
    resultados_finales.append({
        "partido": p['eq'],
        "confianza": round(prob * 100, 2),
        "mercado": mercado,
        "categoria": categoria,
        "stake": "10%" if categoria == "DIOS" else "3%"
    })

with open('data.json', 'w') as f:
    json.dump(resultados_finales, f, indent=4)
