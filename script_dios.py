import os
import json
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# --- 1. ENTRENAMIENTO (Cerebro IA Inalterado) ---
def entrenar_cerebro():
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

# --- 2. EL SCRAPER NIVEL DIOS ---
def ejecutar_scraper_maestro():
    print("🕵️ Iniciando Scraper en modo sigilo...")
    chrome_options = Options()
    chrome_options.add_argument("--headless") # Invisible
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Aquí es donde el bot "navega". Usaremos una URL de ejemplo de estadísticas
    # En una implementación real, aquí pondrías la URL de la liga que quieres atacar
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    lista_partidos = []
    try:
        # Simulamos la entrada a una web de estadísticas deportivas
        # El bot extrae los nombres de los equipos y sus métricas recientes
        driver.get("https://www.google.com") # Punto de entrada neutro
        
        # DATOS EXTRAÍDOS POR EL SCRAPER (Simulado para que veas el flujo final)
        raw_data = [
            {"eq": "Man. City vs Everton", "a": 4.5, "d": 0.5, "h": 0.99},
            {"eq": "Real Madrid vs Valencia", "a": 4.1, "d": 0.9, "h": 0.92},
            {"eq": "Bayern vs Bochum", "a": 4.3, "d": 0.7, "h": 0.95},
            {"eq": "Inter vs Lecce", "a": 3.8, "d": 1.1, "h": 0.88}
        ]
        
        for p in raw_data:
            lista_partidos.append(p)
            
    finally:
        driver.quit()
    return lista_partidos

# --- 3. PROCESO FINAL ---
IA = entrenar_cerebro()
partidos_vivos = ejecutar_scraper_maestro()
resultados = []

for p in partidos_vivos:
    # Pasamos los datos del scraper por el filtro del Dios
    input_ia = [p['a'], p['d'], 0, 0.85, p['h']]
    prob = IA.predict_proba([input_ia])[0][1]
    
    es_dios = prob >= 0.98
    resultados.append({
        "partido": p['eq'],
        "confianza": round(prob * 100, 2),
        "mercado": "Hándicap -1.5" if p['a'] > 4.2 else "Gana Local",
        "categoria": "DIOS" if es_dios else "EXTRA",
        "stake": "10%" if es_dios else "3%"
    })

with open('data.json', 'w') as f:
    json.dump(resultados, f, indent=4)
print("✅ Extracción y Análisis completados.")
