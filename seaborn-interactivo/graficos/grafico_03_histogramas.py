"""
Histogramas INTERACTIVOS
Distribuciones con Plotly
"""

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt
import os

def crear_histogramas(data_path='data/spotify_data_limpio.csv'):
    """
    Crea histogramas interactivos
    """
    os.makedirs('output/images', exist_ok=True)
    os.makedirs('output/interactive', exist_ok=True)
    
    print("📂 Cargando datos...")
    data = pd.read_csv(data_path)
    
    # ==========================================
    # PNG ESTÁTICO (Seaborn)
    # ==========================================
    
    print("🎨 Generando PNG estático...")
    sns.set_theme(style="whitegrid", context="talk")
    fig_static, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig_static.suptitle('📈 Distribución de Variables en Spotify', 
                        fontsize=22, fontweight='bold', y=0.995, color='#1DB954')
    
    sns.histplot(data=data, x='track_popularity', kde=True, bins=30, 
                 color='skyblue', edgecolor='black', linewidth=1.2, ax=axes[0,0])
    axes[0,0].set_title('Popularidad de Canciones', fontsize=14, fontweight='bold')
    axes[0,0].set_xlabel('Popularidad', fontsize=12)
    axes[0,0].set_ylabel('Frecuencia', fontsize=12)
    
    sns.histplot(data=data, x='track_duration_min', kde=True, bins=30,
                 color='lightcoral', edgecolor='black', linewidth=1.2, ax=axes[0,1])
    axes[0,1].set_title('Duración de Canciones', fontsize=14, fontweight='bold')
    axes[0,1].set_xlabel('Duración (minutos)', fontsize=12)
    axes[0,1].set_ylabel('Frecuencia', fontsize=12)
    
    if 'explicit' in data.columns:
        sns.histplot(data=data, x='track_popularity', hue='explicit', kde=True, 
                     palette=['lightgreen', 'salmon'], edgecolor='black', linewidth=1, ax=axes[1,0])
        axes[1,0].set_title('Popularidad por Contenido Explícito', fontsize=14, fontweight='bold')
        axes[1,0].set_xlabel('Popularidad', fontsize=12)
        axes[1,0].set_ylabel('Frecuencia', fontsize=12)
        axes[1,0].legend(title='Explícito', labels=['No', 'Sí'])
    
    sns.histplot(data=data, x='artist_followers', kde=True, log_scale=True, bins=30,
                 color='mediumpurple', edgecolor='black', linewidth=1.2, ax=axes[1,1])
    axes[1,1].set_title('Seguidores de Artistas (escala logarítmica)', fontsize=14, fontweight='bold')
    axes[1,1].set_xlabel('Seguidores (log)', fontsize=12)
    axes[1,1].set_ylabel('Frecuencia', fontsize=12)
    
    plt.tight_layout()
    fig_static.savefig('output/images/03_histogramas.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig_static)
    
    # ==========================================
    # HTML INTERACTIVO (Plotly)
    # ==========================================
    
    print("✨ Generando gráficos interactivos...")
    
    # Crear subplots
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Distribución de Popularidad de Canciones', 
                       'Distribución de Duración de Canciones',
                       'Popularidad según Contenido Explícito', 
                       'Distribución de Seguidores de Artistas (escala logarítmica)'),
        vertical_spacing=0.12,
        horizontal_spacing=0.1
    )
    
    # Histograma 1: Popularidad
    fig.add_trace(
        go.Histogram(
            x=data['track_popularity'],
            nbinsx=30,
            name='Popularidad',
            marker_color='skyblue',
            opacity=0.7,
            hovertemplate='Popularidad: %{x}<br>Frecuencia: %{y}<extra></extra>'
        ),
        row=1, col=1
    )
    
    # Histograma 2: Duración
    fig.add_trace(
        go.Histogram(
            x=data['track_duration_min'],
            nbinsx=30,
            name='Duración',
            marker_color='lightcoral',
            opacity=0.7,
            hovertemplate='Duración: %{x:.2f} min<br>Frecuencia: %{y}<extra></extra>'
        ),
        row=1, col=2
    )
    
    # Histograma 3: Por contenido explícito
    if 'explicit' in data.columns:
        for explicit_val, color in [(False, 'lightgreen'), (True, 'salmon')]:
            filtered = data[data['explicit'] == explicit_val]
            fig.add_trace(
                go.Histogram(
                    x=filtered['track_popularity'],
                    nbinsx=25,
                    name='Explícito' if explicit_val else 'No Explícito',
                    marker_color=color,
                    opacity=0.6,
                    hovertemplate='Popularidad: %{x}<br>Frecuencia: %{y}<extra></extra>'
                ),
                row=2, col=1
            )
    
    # Histograma 4: Seguidores (escala logarítmica)
    # Filtrar valores mayores a 0 para la escala log
    import numpy as np
    followers_clean = data[data['artist_followers'] > 0]['artist_followers']
    
    # Crear bins logarítmicos manualmente
    log_bins = np.logspace(np.log10(followers_clean.min()), 
                           np.log10(followers_clean.max()), 
                           30)
    
    # Calcular el histograma manualmente
    hist, bin_edges = np.histogram(followers_clean, bins=log_bins)
    
    # Calcular el centro de cada bin para el gráfico de barras
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    
    # Calcular el ancho de cada barra (distancia entre bins)
    widths = bin_edges[1:] - bin_edges[:-1]
    
    # Crear gráfico de barras en lugar de histograma
    fig.add_trace(
        go.Bar(
            x=bin_centers,
            y=hist,
            width=widths * 0.95,  # 95% del ancho del bin para dejar espacio
            name='Seguidores',
            marker=dict(
                color='mediumpurple',
                line=dict(color='darkviolet', width=0.5)
            ),
            opacity=0.85,
            hovertemplate='<b>Seguidores:</b> %{x:,.0f}<br><b>Frecuencia:</b> %{y}<extra></extra>',
            showlegend=True
        ),
        row=2, col=2
    )
    
    # Configurar ejes
    fig.update_xaxes(title_text="<b>Popularidad</b>", row=1, col=1)
    fig.update_xaxes(title_text="<b>Duración (min)</b>", row=1, col=2)
    fig.update_xaxes(title_text="<b>Popularidad</b>", row=2, col=1)
    fig.update_xaxes(
        title_text="<b>Seguidores</b>", 
        type="log",
        showgrid=True,
        gridcolor='lightgray',
        row=2, col=2
    )
    
    fig.update_yaxes(title_text="Frecuencia", row=1, col=1)
    fig.update_yaxes(title_text="Frecuencia", row=1, col=2)
    fig.update_yaxes(title_text="Frecuencia", row=2, col=1)
    fig.update_yaxes(title_text="Frecuencia", row=2, col=2)
    
    # Layout
    fig.update_layout(
        title={
            'text': '<b>Distribución de Variables en Spotify</b><br><sub>Análisis de frecuencias y patrones de distribución</sub>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#1DB954'}
        },
        template='plotly_white',
        height=900,
        showlegend=True,
        hovermode='closest'
    )
    
    fig.write_html(
        'output/interactive/03_histogramas.html',
        config={'displayModeBar': True, 'displaylogo': False},
        include_plotlyjs='cdn'
    )
    
    print("✅ Gráfico 3 completado!")
    print(f"   📄 PNG: output/images/03_histogramas.png")
    print(f"   🌐 HTML: output/interactive/03_histogramas.html")

if __name__ == "__main__":
    crear_histogramas()