"""
Swarmplot/Stripplot INTERACTIVO
Visualización de todos los puntos con Plotly
"""

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

def crear_enjambre(data_path='data/spotify_data_limpio.csv'):
    """
    Crea gráficos de enjambre interactivos
    """
    os.makedirs('output/images', exist_ok=True)
    os.makedirs('output/interactive', exist_ok=True)
    
    print("📂 Cargando datos...")
    data = pd.read_csv(data_path)
    
    # Tomar muestra
    sample_size = min(500, len(data))
    data_sample = data.sample(n=sample_size, random_state=42)
    
    # ==========================================
    # PNG ESTÁTICO (Seaborn)
    # ==========================================
    
    print("🎨 Generando PNG estático...")
    sns.set_theme(style="whitegrid", context="talk")
    fig_static, axes = plt.subplots(1, 2, figsize=(18, 8))
    fig_static.suptitle('🐝 Gráficos de Enjambre (Swarmplot)', 
                        fontsize=22, fontweight='bold', y=0.98, color='#1DB954')
    
    if 'explicit' in data_sample.columns:
        sns.swarmplot(data=data_sample, x='explicit', y='track_popularity', 
                     palette='Set2', size=6, alpha=0.7, edgecolor='black', linewidth=0.5, ax=axes[0])
        axes[0].set_title('Popularidad por Contenido Explícito', fontsize=14, fontweight='bold')
        axes[0].set_xlabel('Contenido Explícito', fontsize=12)
        axes[0].set_ylabel('Popularidad', fontsize=12)
        axes[0].set_xticklabels(['No', 'Sí'])
        axes[0].grid(axis='y', alpha=0.3)
    
    top5 = data['artist_name'].value_counts().head(5).index
    data_top5 = data[data['artist_name'].isin(top5)].sample(n=min(300, len(data)), random_state=42)
    sns.swarmplot(data=data_top5, x='artist_name', y='track_popularity', 
                 palette='husl', size=5, alpha=0.7, edgecolor='black', linewidth=0.5, ax=axes[1])
    axes[1].set_title('Top 5 Artistas Más Frecuentes', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Artista', fontsize=12)
    axes[1].set_ylabel('Popularidad', fontsize=12)
    axes[1].tick_params(axis='x', rotation=30)
    axes[1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    fig_static.savefig('output/images/05_enjambre.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig_static)
    
    # ==========================================
    # HTML INTERACTIVO (Plotly - Strip Plot)
    # ==========================================
    
    print("✨ Generando gráficos interactivos...")
    
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=('Distribución de Popularidad según Contenido Explícito', 
                       'Distribución de Popularidad - Top 5 Artistas'),
        horizontal_spacing=0.15
    )
    
    # Strip plot 1: Por contenido explícito
    if 'explicit' in data_sample.columns:
        for explicit_val, color, name in [(False, 'lightgreen', 'No Explícito'), 
                                           (True, 'salmon', 'Explícito')]:
            filtered = data_sample[data_sample['explicit'] == explicit_val]
            
            # Añadir jitter manual en X
            x_pos = 0 if explicit_val == False else 1
            jitter = np.random.normal(0, 0.04, size=len(filtered))
            
            fig.add_trace(
                go.Scatter(
                    x=[x_pos] * len(filtered) + jitter,
                    y=filtered['track_popularity'],
                    mode='markers',
                    name=name,
                    marker=dict(
                        size=8,
                        color=color,
                        opacity=0.6,
                        line=dict(width=0.5, color='black')
                    ),
                    hovertemplate=f'<b>{name}</b><br>Popularidad: %{{y}}<extra></extra>'
                ),
                row=1, col=1
            )
    
    # Strip plot 2: Top 5 artistas
    top5 = data['artist_name'].value_counts().head(5).index
    colors = ['skyblue', 'lightcoral', 'lightgreen', 'plum', 'gold']
    
    for idx, artist in enumerate(top5):
        filtered = data_sample[data_sample['artist_name'] == artist]
        if len(filtered) > 0:
            jitter = np.random.normal(0, 0.04, size=len(filtered))
            
            fig.add_trace(
                go.Scatter(
                    x=[idx] * len(filtered) + jitter,
                    y=filtered['track_popularity'],
                    mode='markers',
                    name=artist,
                    marker=dict(
                        size=7,
                        color=colors[idx],
                        opacity=0.6,
                        line=dict(width=0.5, color='black')
                    ),
                    hovertemplate=f'<b>{artist}</b><br>Popularidad: %{{y}}<extra></extra>'
                ),
                row=1, col=2
            )
    
    # Configurar ejes
    fig. update_xaxes(
        tickmode='array',
        tickvals=[0, 1],
        ticktext=['No Explícito', 'Explícito'],
        row=1, col=1
    )
    
    fig.update_xaxes(
        tickmode='array',
        tickvals=list(range(5)),
        ticktext=list(top5),
        row=1, col=2
    )
    
    fig.update_yaxes(title_text="Popularidad", row=1, col=1)
    fig.update_yaxes(title_text="Popularidad", row=1, col=2)
    
    # Layout
    fig.update_layout(
        title={
            'text': f'<b>Gráficos de Enjambre (Swarmplot)</b><br><sub>Cada punto representa una canción - Muestra de {sample_size} canciones</sub>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#1DB954'}
        },
        template='plotly_white',
        height=600,
        showlegend=True,
        hovermode='closest'
    )
    
    fig.write_html(
        'output/interactive/05_enjambre.html',
        config={'displayModeBar': True, 'displaylogo': False},
        include_plotlyjs='cdn'
    )
    
    print("✅ Gráfico 5 completado!")
    print(f"   📄 PNG: output/images/05_enjambre.png")
    print(f"   🌐 HTML: output/interactive/05_enjambre.html")

if __name__ == "__main__":
    crear_enjambre()