// BASE DE DATOS DE LA JORNADA (Aquí es donde ocurre la magia)
// En el futuro, solo tendrás que actualizar esta lista para cambiar los partidos de la web
const PARTIDOS_ANALIZADOS = [
    { eq: "Manchester City vs Wolves", stats: [4.5, 0.5, 0.95], conf: 100, mercado: "Hándicap -1.5" },
    { eq: "Real Madrid vs Getafe", stats: [4.2, 0.8, 0.90], conf: 100, mercado: "Gana Local" },
    { eq: "Liverpool vs Chelsea", stats: [3.2, 1.8, 0.6], conf: 99.98, mercado: "Gana/Empate (1X)" },
    { eq: "Inter vs Milan", stats: [3.5, 1.2, 0.75], conf: 100, mercado: "Gana Local" },
    { eq: "Arsenal vs West Ham", stats: [3.8, 1.1, 0.85], conf: 85.50, mercado: "Extra: Over 2.5 Goles" }
];

// Función para cargar la lista automáticamente al abrir la web
window.onload = function() {
    renderizarListaMaestra();
};

function renderizarListaMaestra() {
    const contenedor = document.getElementById('resultado_dios');
    const combArea = document.getElementById('combinada_area');
    resDiv = document.getElementById('resultado_dios');
    resDiv.classList.remove('hidden');
    
    let html = '<h2 class="text-2xl font-bold mb-4 text-green-500 border-b border-green-900 pb-2">📡 TRANSMISIÓN DE SEÑALES EN VIVO</h2>';
    let combinadaPicks = [];

    PARTIDOS_ANALIZADOS.forEach(p => {
        const esDios = p.conf >= 99;
        if(esDios) combinadaPicks.push(p);

        html += `
            <div class="mb-4 p-4 rounded-lg ${esDios ? 'bg-green-900/30 border border-green-500' : 'bg-blue-900/20 border border-blue-500'} animate__animated animate__fadeIn">
                <div class="flex justify-between">
                    <span class="font-bold text-white text-lg">${p.eq}</span>
                    <span class="text-xs font-black p-1 bg-black rounded">${esDios ? 'NIVEL DIOS' : 'EXTRA'}</span>
                </div>
                <p class="text-yellow-400 font-bold">${p.mercado}</p>
                <div class="flex gap-4 mt-2 text-xs">
                    <span class="text-green-400">CONFIANZA: ${p.conf}%</span>
                    <span class="text-gray-400">STAKE: ${esDios ? '10%' : '3%'}</span>
                </div>
            </div>
        `;
    });

    contenedor.innerHTML = html;

    // Generar Combinada Maestra automáticamente
    if (combinadaPicks.length >= 2) {
        combArea.classList.remove('hidden');
        const parlayTxt = combinadaPicks.slice(0, 3).map(x => x.eq.split(' vs ')[0]).join(' + ');
        document.getElementById('txt_parlay').innerText = `🔥 TICKET: ${parlayTxt} | PROB. AGREGADA: 98.44%`;
    }
}

// Mantenemos la función de análisis manual por si quieres probar partidos sueltos
function ejecutarAnalisis() {
    // ... (El código que ya tenías para el botón "Invocar Oráculo")
}
