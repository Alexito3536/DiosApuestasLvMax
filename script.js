function ejecutarAnalisis() {
    const eq = document.getElementById('input_eq').value;
    const ataque = parseFloat(document.getElementById('input_ataque').value);
    const defensa = parseFloat(document.getElementById('input_defensa').value);
    const presion = parseFloat(document.getElementById('input_presion').value);

    // Lógica Inversa del Modelo T (Simulando la inferencia del Gradient Boosting)
    let prob = (ataque * 1.5 - defensa * 0.7) + (presion * 0.5);
    let finalConf = Math.min(100, Math.max(0, (prob / 6) * 100));

    const resDiv = document.getElementById('resultado_dios');
    const combDiv = document.getElementById('combinada_area');

    if (finalConf >= 95) {
        resDiv.classList.remove('hidden');
        document.getElementById('txt_partido').innerText = eq;
        document.getElementById('txt_mercado').innerText = ataque > 4.0 ? "🎯 MERCADO: HÁNDICAP -1.5" : "🎯 MERCADO: GANA LOCAL DIRECTO";
        document.getElementById('txt_confianza').innerText = `CONFIANZA: ${finalConf.toFixed(2)}%`;
        document.getElementById('txt_stake').innerText = `STAKE: 10% DEL BANKROLL`;
        
        // Mostrar combinada si hay alta confianza
        combDiv.classList.remove('hidden');
        document.getElementById('txt_parlay').innerText = `[${eq} + Over 1.5 Goles] - Cuota estimada: 2.10`;
    } else {
        alert("⚠️ EL DIOS DICE: Riesgo detectado. Probabilidad de " + finalConf.toFixed(2) + "% no es suficiente.");
        resDiv.classList.add('hidden');
        combDiv.classList.add('hidden');
    }
}
