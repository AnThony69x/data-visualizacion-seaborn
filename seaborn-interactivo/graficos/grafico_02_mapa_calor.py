"""
Mapa de Calor INTERACTIVO
Correlaciones con Plotly
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np
import os

def crear_mapa_calor(data_path='data/spotify_data_limpio.csv'):
    """
    Crea mapa de calor interactivo
    """
    os.makedirs('output/images', exist_ok=True)
    os.makedirs('output/interactive', exist_ok=True)
    
    print("📂 Cargando datos...")
    data = pd.read_csv(data_path)
    
    # Seleccionar columnas numéricas
    numeric_cols = ['track_popularity', 'artist_popularity', 
                    'artist_followers', 'track_duration_min']
    
    available_cols = [col for col in numeric_cols if col in data.columns]
    correlation_data = data[available_cols]
    
    # Renombrar columnas a español
    spanish_names = {
        'track_popularity': 'Popularidad Canción',
        'artist_popularity': 'Popularidad Artista',
        'artist_followers': 'Seguidores Artista',
        'track_duration_min': 'Duración (min)'
    }
    correlation_data = correlation_data.rename(columns=spanish_names)
    
    # Calcular correlación
    print("🔧 Calculando correlaciones...")
    corr_matrix = correlation_data.corr()
    
    # ==========================================
    # PNG ESTÁTICO (Seaborn)
    # ==========================================
    
    print("🎨 Generando PNG estático...")
    sns.set_theme(style="white", context="talk")
    fig_static, ax = plt.subplots(figsize=(14, 11))
    
    # Sin máscara - mostrar la matriz completa
    sns.heatmap(corr_matrix,
                annot=True,
                fmt='.2f',
                cmap='RdBu_r',
                center=0,
                vmin=-1, vmax=1,
                square=True,
                linewidths=3,
                linecolor='white',
                cbar_kws={
                    'label': 'Correlación', 
                    'shrink': 0.82,
                    'aspect': 30,
                    'pad': 0.02
                },
                annot_kws={'size': 14, 'weight': 'bold'},
                ax=ax)
    
    ax.set_title('Mapa de Calor: Correlaciones entre Variables', 
                 fontsize=20, fontweight='bold', pad=20, color='#1DB954')
    ax.set_xlabel('')
    ax.set_ylabel('')
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.yticks(rotation=0, fontsize=12)
    plt.tight_layout()
    fig_static.savefig('output/images/02_mapa_calor.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig_static)
    
    # ==========================================
    # HTML INTERACTIVO (Plotly)
    # ==========================================
    
    print("✨ Generando gráfico interactivo...")
    
    # Las columnas ya están en español, solo ajustar formato para HTML
    labels_html = {
        'Popularidad Canción': 'Popularidad<br>Canción',
        'Popularidad Artista': 'Popularidad<br>Artista',
        'Seguidores Artista': 'Seguidores<br>Artista',
        'Duración (min)': 'Duración<br>(min)'
    }
    
    # Renombrar columnas para display
    corr_display = corr_matrix.copy()
    corr_display.index = [labels_html.get(col, col) for col in corr_display.index]
    corr_display.columns = [labels_html.get(col, col) for col in corr_display.columns]
    
    fig = go.Figure(data=go.Heatmap(
        z=corr_display.values,
        x=corr_display.columns,
        y=corr_display.index,
        colorscale='RdBu',
        zmid=0,
        zmin=-1,
        zmax=1,
        text=np.round(corr_display.values, 2),
        texttemplate='%{text}',
        textfont={"size": 14, "color": "black"},
        hovertemplate='<b>%{y} vs %{x}</b><br>Correlación: %{z:.3f}<extra></extra>',
        colorbar=dict(
            title="Correlación",
            tickmode="linear",
            tick0=-1,
            dtick=0.5
        )
    ))
    
    fig.update_layout(
        title={
            'text': '<b>Mapa de Calor: Correlaciones entre Variables</b><br><sub>Valores entre -1 (correlación negativa) y +1 (correlación positiva)</sub>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#1DB954'}
        },
        xaxis_title='',
        yaxis_title='',
        template='plotly_white',
        height=600,
        width=700,
        font=dict(size=12)
    )
    
    # Hacer cuadrado
    fig.update_xaxes(side="bottom")
    fig.update_yaxes(autorange="reversed")
    
    fig.write_html(
        'output/interactive/02_mapa_calor.html',
        config={
            'displayModeBar': True,
            'displaylogo': False,
            'toImageButtonOptions': {
                'format': 'png',
                'filename': 'mapa_calor_spotify',
                'height': 800,
                'width': 900,
                'scale': 2
            }
        },
        include_plotlyjs='cdn'
    )
    
    print("✅ Gráfico 2 completado!")
    print(f"   📄 PNG: output/images/02_mapa_calor.png")
    print(f"   🌐 HTML: output/interactive/02_mapa_calor.html")

if __name__ == "__main__":
    crear_mapa_calor()