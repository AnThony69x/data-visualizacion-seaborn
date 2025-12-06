"""
Gráfico de Barras INTERACTIVO
Seaborn (análisis) + Plotly (interactividad)
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import os

def crear_grafico_barras(data_path='data/spotify_data_limpio.csv'):
    """
    Crea gráfico de barras interactivo con Plotly
    """
    # Crear carpetas
    os.makedirs('output/images', exist_ok=True)
    os.makedirs('output/interactive', exist_ok=True)
    
    # Cargar datos
    print("📂 Cargando datos...")
    data = pd.read_csv(data_path)
    
    # Preparar datos
    print("🔧 Procesando datos...")
    top_artists = (data.groupby('artist_name')['artist_popularity']
                   .mean()
                   .nlargest(15)
                   .sort_values(ascending=True)  # Para horizontal
                   .reset_index())
    
    # ==========================================
    # VERSIÓN 1: PNG ESTÁTICO (Seaborn)
    # ==========================================
    
    print("🎨 Generando PNG estático...")
    sns.set_theme(style="whitegrid", context="talk")
    fig_static, ax = plt.subplots(figsize=(14, 9))
    
    sns.barplot(data=top_artists, 
                y='artist_name', 
                x='artist_popularity',
                palette='viridis',
                edgecolor='black',
                linewidth=1.5,
                ax=ax)
    
    plt.title('📊 Top 15 Artistas Más Populares en Spotify', 
              fontsize=20, fontweight='bold', pad=20, color='#1DB954')
    plt.xlabel('Popularidad Promedio', fontsize=14, fontweight='bold')
    plt.ylabel('Artista', fontsize=14, fontweight='bold')
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    plt.tight_layout()
    
    fig_static.savefig('output/images/01_barras.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig_static)
    
    # ==========================================
    # VERSIÓN 2: HTML INTERACTIVO (Plotly)
    # ==========================================
    
    print("✨ Generando gráfico interactivo...")
    
    # Invertir orden para que el más popular esté arriba
    top_artists_plot = top_artists.sort_values('artist_popularity', ascending=True)
    
    fig = go.Figure()
    
    # Agregar barras horizontales
    fig.add_trace(go.Bar(
        x=top_artists_plot['artist_popularity'],
        y=top_artists_plot['artist_name'],
        orientation='h',
        marker=dict(
            color=top_artists_plot['artist_popularity'],
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title="Popularidad"),
            line=dict(color='rgba(0,0,0,0.5)', width=1.5)
        ),
        text=top_artists_plot['artist_popularity'].round(1),
        textposition='outside',
        hovertemplate='<b>%{y}</b><br>Popularidad: %{x:.2f}<extra></extra>'
    ))
    
    # Configurar layout
    fig.update_layout(
        title={
            'text': '<b>Top 15 Artistas Más Populares en Spotify</b><br><sub>Ranking basado en la popularidad promedio de sus canciones</sub>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#1DB954', 'family': 'Arial Black'}
        },
        xaxis_title='<b>Popularidad Promedio (0-100)</b>',
        yaxis_title='<b>Artista</b>',
        template='plotly_white',
        hovermode='y unified',
        height=700,
        showlegend=False,
        plot_bgcolor='rgba(240,240,240,0.5)',
        font=dict(size=12),
        margin=dict(l=150, r=50, t=100, b=80)
    )
    
    # Agregar anotación
    promedio = top_artists_plot['artist_popularity'].mean()
    fig.add_vline(
        x=promedio,
        line_dash="dash",
        line_color="red",
        line_width=2,
        annotation_text=f"Promedio: {promedio:.1f}",
        annotation_position="top"
    )
    
    # Guardar HTML
    fig.write_html(
        'output/interactive/01_barras.html',
        config={
            'displayModeBar': True,
            'displaylogo': False,
            'modeBarButtonsToAdd': ['hoverclosest', 'hovercompare'],
            'toImageButtonOptions': {
                'format': 'png',
                'filename': 'grafico_barras_spotify',
                'height': 1000,
                'width': 1400,
                'scale': 2
            }
        },
        include_plotlyjs='cdn'
    )
    
    print("✅ Gráfico 1 completado!")
    print(f"   📄 PNG: output/images/01_barras.png")
    print(f"   🌐 HTML: output/interactive/01_barras.html")

if __name__ == "__main__":
    crear_grafico_barras()