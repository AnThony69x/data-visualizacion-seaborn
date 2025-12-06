"""
Script Principal - Generar Todos los Gráficos Interactivos
Proyecto: Seaborn + Plotly Visualización Interactiva
Autores: Anthony Mejia & Emilio Cardenas
"""

import sys
import os
from datetime import datetime
import time

# Agregar carpeta graficos al path
sys.path. append(os.path.dirname(os.path.abspath(__file__)))

def main():
    """
    Genera todos los gráficos (PNG estáticos + HTML interactivos)
    """
    print("="*70)
    print("🎵 SPOTIFY DATA VISUALIZER - SEABORN + PLOTLY")
    print("="*70)
    print(f"📅 Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"👥 Autores: Anthony Mejia & Emilio Cardenas")
    print("="*70)
    print()
    
    # Verificar dataset
    if not os.path.exists('data/spotify_data_limpio.csv'):
        print("❌ ERROR: No se encontró 'data/spotify_data_limpio.csv'")
        print("   Coloca tu dataset en la carpeta 'data/'")
        return
    
    # Crear carpetas
    os.makedirs('output/images', exist_ok=True)
    os.makedirs('output/interactive', exist_ok=True)
    
    # Importar funciones
    try:
        from graficos.grafico_01_barras import crear_grafico_barras
        from graficos.grafico_02_mapa_calor import crear_mapa_calor
        from graficos.grafico_03_histogramas import crear_histogramas
        from graficos.grafico_04_boxplots import crear_boxplots
        from graficos.grafico_05_enjambre import crear_enjambre
        from graficos.grafico_06_kde import crear_kde
        from graficos.grafico_07_pareto import crear_pareto
    except ImportError as e:
        print(f"❌ Error al importar módulos: {e}")
        print("   Verifica que todos los archivos estén en la carpeta 'graficos/'")
        return
    
    # Lista de gráficos
    graficos = [
        ("1️⃣  Gráfico de Barras", crear_grafico_barras),
        ("2️⃣  Mapa de Calor", crear_mapa_calor),
        ("3️⃣  Histogramas", crear_histogramas),
        ("4️⃣  Boxplots", crear_boxplots),
        ("5️⃣  Enjambre (Swarmplot)", crear_enjambre),
        ("6️⃣  KDE (Densidad)", crear_kde),
        ("7️⃣  Pareto", crear_pareto),
    ]
    
    exitosos = 0
    fallidos = 0
    tiempo_inicio = time.time()
    
    print("🚀 Generando gráficos interactivos.. .\n")
    
    for idx, (nombre, funcion) in enumerate(graficos, 1):
        try:
            print(f"\n{'='*70}")
            print(f"⏳ [{idx}/7] Generando {nombre}...")
            print(f"{'='*70}")
            
            funcion()
            exitosos += 1
            print()
            
        except Exception as e:
            print(f"❌ Error en {nombre}: {e}\n")
            import traceback
            traceback.print_exc()
            fallidos += 1
    
    tiempo_total = time.time() - tiempo_inicio
    
    # Resumen
    print("\n" + "="*70)
    print("📊 RESUMEN FINAL")
    print("="*70)
    print(f"✅ Gráficos exitosos: {exitosos}")
    print(f"❌ Gráficos fallidos: {fallidos}")
    print(f"⏱️  Tiempo total: {tiempo_total:.2f} segundos")
    print(f"\n📁 Archivos generados:")
    print(f"   • PNG estáticos: output/images/")
    print(f"   • HTML interactivos: output/interactive/")
    print("="*70)
    print()
    print("🌐 Abre 'index.html' en tu navegador para ver todos los gráficos")
    print("="*70)

if __name__ == "__main__":
    main()