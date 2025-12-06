"""
KDE (Density) INTERACTIVO
Gráficos de Densidad con Plotly
"""

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

def crear_kde(data_path='data/spotify_data_limpio.csv'):
    """
    Crea gráficos KDE interactivos
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
    fig_static, axes = plt.subplots(2, 2, figsize=(17, 13))
    fig_static.suptitle('📉 Gráficos de Densidad (KDE)', 
                        fontsize=22, fontweight='bold', y=0.995, color='#1DB954')
    
    sns.kdeplot(data=data, x='track_popularity', fill=True, color='skyblue', 
               linewidth=2.5, ax=axes[0,0])
    axes[0,0].set_title('Densidad de Popularidad', fontsize=14, fontweight='bold')
    axes[0,0].set_xlabel('Popularidad', fontsize=12)
    axes[0,0].set_ylabel('Densidad', fontsize=12)
    
    if 'explicit' in data.columns:
        sns.kdeplot(data=data, x='track_popularity', hue='explicit', fill=True, 
                   alpha=0.6, linewidth=2, palette=['lightgreen', 'salmon'], ax=axes[0,1])
        axes[0,1].set_title('Densidad por Contenido Explícito', fontsize=14, fontweight='bold')
        axes[0,1].set_xlabel('Popularidad', fontsize=12)
        axes[0,1].set_ylabel('Densidad', fontsize=12)
        axes[0,1].legend(title='Explícito', labels=['No', 'Sí'])
    
    sns.kdeplot(data=data, x='artist_followers', y='track_popularity', 
               fill=True, cmap='viridis', levels=10, ax=axes[1,0])
    axes[1,0].set_title('Densidad 2D: Seguidores vs Popularidad', fontsize=14, fontweight='bold')
    axes[1,0].set_xlabel('Seguidores (log)', fontsize=12)
    axes[1,0].set_ylabel('Popularidad', fontsize=12)
    axes[1,0].set_xscale('log')
    
    sns.kdeplot(data=data, x='track_duration_min', fill=True, color='lightcoral', 
               linewidth=2.5, ax=axes[1,1])
    axes[1,1].set_title('Densidad de Duración', fontsize=14, fontweight='bold')
    axes[1,1].set_xlabel('Duración (min)', fontsize=12)
    axes[1,1].set_ylabel('Densidad', fontsize=12)
    
    plt.tight_layout()
    fig_static.savefig('output/images/06_kde.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig_static)
    
    # ==========================================
    # HTML INTERACTIVO (Plotly)
    # ==========================================
    
    print("✨ Generando gráficos interactivos...")
    
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Densidad de Popularidad', 
                       'Densidad por Contenido Explícito',
                       'Densidad 2D: Seguidores vs Popularidad', 
                       'Densidad de Duración'),
        vertical_spacing=0.12,
        horizontal_spacing=0.12,
        specs=[[{"type": "xy"}, {"type": "xy"}],
               [{"type": "xy"}, {"type": "xy"}]]
    )
    
    # KDE 1: Popularidad univariada
    hist_data = [data['track_popularity'].dropna().values]
    group_labels = ['Popularidad']
    
    kde_fig1 = ff.create_distplot(hist_data, group_labels, 
                                   show_hist=False, show_rug=False,
                                   colors=['skyblue'])
    
    for trace in kde_fig1.data:
        trace.fill = 'tozeroy'
        trace.hovertemplate = 'Popularidad: %{x}<br>Densidad: %{y:. 4f}<extra></extra>'
        fig.add_trace(trace, row=1, col=1)
    
    # KDE 2: Por contenido explícito
    if 'explicit' in data.columns:
        hist_explicit = [
            data[data['explicit'] == False]['track_popularity'].dropna().values,
            data[data['explicit'] == True]['track_popularity'].dropna().values
        ]
        group_labels_explicit = ['No Explícito', 'Explícito']
        
        kde_fig2 = ff. create_distplot(hist_explicit, group_labels_explicit,
                                       show_hist=False, show_rug=False,
                                       colors=['lightgreen', 'salmon'])
        
        for trace in kde_fig2.data:
            trace.fill = 'tozeroy'
            trace.opacity = 0.6
            trace.hovertemplate = trace.name + '<br>Popularidad: %{x}<br>Densidad: %{y:. 4f}<extra></extra>'
            fig.add_trace(trace, row=1, col=2)
    
    # KDE 3: Densidad 2D (Contour)
    sample_2d = data.sample(n=min(1000, len(data)), random_state=42)
    
    fig.add_trace(
        go.Histogram2dContour(
            x=np.log10(sample_2d['artist_followers'] + 1),
            y=sample_2d['track_popularity'],
            colorscale='Viridis',
            showscale=True,
            contours=dict(showlabels=True),
            hovertemplate='Log Seguidores: %{x:. 2f}<br>Popularidad: %{y}<extra></extra>'
        ),
        row=2, col=1
    )
    
    # KDE 4: Duración
    hist_duration = [data['track_duration_min'].dropna().values]
    group_labels_duration = ['Duración']
    
    kde_fig4 = ff.create_distplot(hist_duration, group_labels_duration,
                                   show_hist=False, show_rug=False,
                                   colors=['lightcoral'])
    
    for trace in kde_fig4.data:
        trace.fill = 'tozeroy'
        trace.hovertemplate = 'Duración: %{x:. 2f} min<br>Densidad: %{y:.4f}<extra></extra>'
        fig.add_trace(trace, row=2, col=2)
    
    # Configurar ejes
    fig. update_xaxes(title_text="Popularidad", row=1, col=1)
    fig.update_xaxes(title_text="Popularidad", row=1, col=2)
    fig.update_xaxes(title_text="Log(Seguidores)", row=2, col=1)
    fig.update_xaxes(title_text="Duración (min)", row=2, col=2)
    
    fig.update_yaxes(title_text="Densidad", row=1, col=1)
    fig.update_yaxes(title_text="Densidad", row=1, col=2)
    fig.update_yaxes(title_text="Popularidad", row=2, col=1)
    fig.update_yaxes(title_text="Densidad", row=2, col=2)
    
    # Layout
    fig.update_layout(
        title={
            'text': '<b>Gráficos de Densidad (KDE)</b><br><sub>Estimación de densidad de probabilidad mediante Kernel (curvas suavizadas)</sub>',
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
        'output/interactive/06_kde.html',
        config={'displayModeBar': True, 'displaylogo': False},
        include_plotlyjs='cdn'
    )
    
    print("✅ Gráfico 6 completado!")
    print(f"   📄 PNG: output/images/06_kde.png")
    print(f"   🌐 HTML: output/interactive/06_kde.html")

if __name__ == "__main__":
    crear_kde()