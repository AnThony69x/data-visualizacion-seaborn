"""
Boxplots INTERACTIVOS
Diagramas de Caja y Bigotes con Plotly
"""

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt
import os

def crear_boxplots(data_path='data/spotify_data_limpio.csv'):
    """
    Crea boxplots interactivos
    """
    os.makedirs('output/images', exist_ok=True)
    os. makedirs('output/interactive', exist_ok=True)
    
    print("📂 Cargando datos...")
    data = pd.read_csv(data_path)
    
    # ==========================================
    # PNG ESTÁTICO (Seaborn)
    # ==========================================
    
    print("🎨 Generando PNG estático...")
    sns.set_theme(style="whitegrid", context="talk")
    fig_static, axes = plt.subplots(2, 2, figsize=(18, 13))
    fig_static.suptitle('📦 Análisis de Dispersión - Boxplots', 
                        fontsize=22, fontweight='bold', y=0.995, color='#1DB954')
    
    # Boxplot 1
    if 'explicit' in data.columns:
        sns.boxplot(data=data, x='explicit', y='track_popularity', 
                   palette='Set2', linewidth=2, ax=axes[0,0])
        axes[0,0].set_title('Popularidad por Contenido Explícito', fontsize=14, fontweight='bold')
        axes[0,0].set_xlabel('Contenido Explícito', fontsize=12)
        axes[0,0].set_ylabel('Popularidad', fontsize=12)
        axes[0,0].set_xticklabels(['No', 'Sí'])
    
    # Boxplot 2
    if 'album_type' in data.columns:
        sns.boxplot(data=data, x='album_type', y='track_duration_min', 
                   palette='pastel', linewidth=2, ax=axes[0,1])
        axes[0,1].set_title('Duración por Tipo de Álbum', fontsize=14, fontweight='bold')
        axes[0,1].set_xlabel('Tipo de Álbum', fontsize=12)
        axes[0,1].set_ylabel('Duración (min)', fontsize=12)
        axes[0,1].tick_params(axis='x', rotation=45)
    
    # Boxplot 3
    top10_artists = data['artist_name'].value_counts().head(10).index
    data_top10 = data[data['artist_name'].isin(top10_artists)]
    sns.boxplot(data=data_top10, x='artist_name', y='track_popularity', 
               palette='husl', linewidth=2, ax=axes[1,0])
    axes[1,0].set_title('Popularidad - Top 10 Artistas', fontsize=14, fontweight='bold')
    axes[1,0].set_xlabel('Artista', fontsize=12)
    axes[1,0].set_ylabel('Popularidad', fontsize=12)
    axes[1,0].tick_params(axis='x', rotation=45)
    
    # Boxplot 4
    sns.boxplot(data=data, y='track_popularity', color='lightblue', linewidth=2, ax=axes[1,1])
    axes[1,1].set_title('Distribución General de Popularidad', fontsize=14, fontweight='bold')
    axes[1,1].set_ylabel('Popularidad', fontsize=12)
    
    plt.tight_layout()
    fig_static.savefig('output/images/04_boxplots.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig_static)
    
    # ==========================================
    # HTML INTERACTIVO (Plotly)
    # ==========================================
    
    print("✨ Generando gráficos interactivos...")
    
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Popularidad según Contenido Explícito', 
                       'Duración según Tipo de Álbum',
                       'Popularidad de los Top 10 Artistas con Más Canciones', 
                       'Distribución General de Popularidad'),
        vertical_spacing=0.15,
        horizontal_spacing=0.12
    )
    
    # Boxplot 1: Por contenido explícito
    if 'explicit' in data.columns:
        for explicit_val, color in [(False, 'lightgreen'), (True, 'salmon')]:
            filtered = data[data['explicit'] == explicit_val]
            fig. add_trace(
                go. Box(
                    y=filtered['track_popularity'],
                    name='Explícito' if explicit_val else 'No Explícito',
                    marker_color=color,
                    boxmean='sd',
                    hovertemplate='<b>%{fullData.name}</b><br>Valor: %{y}<extra></extra>'
                ),
                row=1, col=1
            )
    
    # Boxplot 2: Por tipo de álbum
    if 'album_type' in data.columns:
        album_types = data['album_type'].unique()
        colors = ['skyblue', 'lightcoral', 'lightgreen', 'plum']
        for idx, album in enumerate(album_types[:4]):
            filtered = data[data['album_type'] == album]
            fig. add_trace(
                go. Box(
                    y=filtered['track_duration_min'],
                    name=album,
                    marker_color=colors[idx % len(colors)],
                    boxmean=True,
                    hovertemplate=f'<b>{album}</b><br>Duración: %{{y:. 2f}} min<extra></extra>'
                ),
                row=1, col=2
            )
    
    # Boxplot 3: Top 10 artistas
    top10 = data['artist_name'].value_counts().head(10).index
    colors_artists = ['#%06X' % (hash(artist) % 0xFFFFFF) for artist in top10]
    
    for idx, artist in enumerate(top10):
        filtered = data[data['artist_name'] == artist]
        fig.add_trace(
            go.Box(
                y=filtered['track_popularity'],
                name=artist,
                marker_color=colors_artists[idx],
                boxmean=True,
                hovertemplate=f'<b>{artist}</b><br>Popularidad: %{{y}}<extra></extra>'
            ),
            row=2, col=1
        )
    
    # Boxplot 4: General
    fig.add_trace(
        go.Box(
            y=data['track_popularity'],
            name='Todas las canciones',
            marker_color='mediumpurple',
            boxmean='sd',
            boxpoints='outliers',
            hovertemplate='Popularidad: %{y}<extra></extra>'
        ),
        row=2, col=2
    )
    
    # Configurar ejes
    fig. update_yaxes(title_text="Popularidad", row=1, col=1)
    fig.update_yaxes(title_text="Duración (min)", row=1, col=2)
    fig.update_yaxes(title_text="Popularidad", row=2, col=1)
    fig.update_yaxes(title_text="Popularidad", row=2, col=2)
    
    # Layout
    fig.update_layout(
        title={
            'text': '<b>Análisis de Dispersión - Boxplots</b><br><sub>Diagramas de caja que muestran mediana, cuartiles y valores atípicos</sub>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#1DB954'}
        },
        template='plotly_white',
        height=1000,
        showlegend=True,
        hovermode='closest'
    )
    
    fig.write_html(
        'output/interactive/04_boxplots.html',
        config={'displayModeBar': True, 'displaylogo': False},
        include_plotlyjs='cdn'
    )
    
    print("✅ Gráfico 4 completado!")
    print(f"   📄 PNG: output/images/04_boxplots.png")
    print(f"   🌐 HTML: output/interactive/04_boxplots.html")

if __name__ == "__main__":
    crear_boxplots()