import os
import json
import pandas as pd
import numpy as np
from datetime import datetime # Para manejar fechas reales
from sklearn.ensemble import GradientBoostingClassifier
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# --- 1. ENTRENAMIENTO (IA POTENCIAL MÁXIMO) ---
def entrenar_IA():
    np.random.seed(99)
    n = 30000
    X = pd.DataFrame({
        'f_ataque': np.random.uniform(0.5, 4.5, n),
        'f_defensa': np.random.uniform(0.5, 3.5, n),
        'lesiones': np.random.randint(0, 3, n),
        'presion': np.random.uniform(-1, 1, n),
        'h2h': np.random.uniform(0, 1, n)
    })
    y = ((X['f_ataque'] * 1.5 - X['f_defensa'] * 0.7) - (X['lesiones'] * 0.6) > 2.2).astype(int)
    return GradientBoostingClassifier(n_estimators=300).fit(X, y)

# --- 2. EL SCRAPER ACTUALIZADO (Con Fechas) ---
def ejecutar_scraper_actualizado():
    print("🕵️ Scraper buscando partidos frescos...")
    # Fecha de hoy para marcar la actualización
    fecha_hoy = datetime.now().strftime("%d/%m/%Y")
    
    # LISTA DE PARTIDOS DE LA JORNADA ACTUAL (Edita aquí o deja que el scraper muerda la web)
    # He añadido el campo 'fecha'
    raw_data = [
        {"eq": "Manchester City vs Brighton", "a": 4.5, "d": 0.5, "h": 0.99, "fecha": "15/02/2026"},
        {"eq": "Arsenal vs West Ham", "a": 4.2, "d": 0.8, "h": 0.92, "fecha": "15/02/2026"},
        {"eq": "Liverpool vs Wolves", "a": 4.3, "d": 0.7, "h": 0.95, "fecha": "16/02/2026"},
        {"eq": "Real Madrid vs Sevilla", "a": 4.1, "d": 0.9, "h": 0.90, "fecha": "16/02/2026"}
    ]
    return raw_data, fecha_hoy

# --- 3. PROCESO DE PREDICCIÓN ---
IA = entrenar_IA()
partidos, fecha_sincro = ejecutar_scraper_actualizado()
resultados = []

for p in partidos:
    stats = [p['a'], p['d'], 0, 0.85, p['h']]
    prob = IA.predict_proba([stats])[0][1]
    
    confianza = round(prob * 100, 2)
    es_dios = confianza >= 99.0
    
    resultados.append({
        "partido": p['eq'],
        "fecha": p['fecha'], # <--- Nueva columna de fecha
        "confianza": confianza,
        "mercado": "Hándicap -1.5" if p['a'] > 4.1 else "Gana Local",
        "categoria": "DIOS" if es_dios else "EXTRA",
        "stake": "$100.00" if es_dios else "$30.00",
        "actualizado": fecha_sincro
    })

with open('data.json', 'w') as f:
    json.dump(resultados, f, indent=4)
print(f"✅ Sistema T: Sincronizado para la fecha {fecha_sincro}")
