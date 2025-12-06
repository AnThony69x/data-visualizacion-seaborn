"""
Gráfico de Pareto INTERACTIVO
Principio 80/20 con Plotly
"""

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib. pyplot as plt
import numpy as np
import os

def crear_pareto(data_path='data/spotify_data_limpio.csv'):
    """
    Crea gráfico de Pareto interactivo
    """
    os.makedirs('output/images', exist_ok=True)
    os.makedirs('output/interactive', exist_ok=True)
    
    print("📂 Cargando datos...")
    data = pd.read_csv(data_path)
    
    # Preparar datos
    artist_counts = data['artist_name'].value_counts().head(20)
    cumulative = artist_counts.cumsum()
    cumulative_pct = (cumulative / artist_counts.sum()) * 100
    
    # ==========================================
    # PNG ESTÁTICO (Seaborn/Matplotlib)
    # ==========================================
    
    print("🎨 Generando PNG estático...")
    sns.set_theme(style="whitegrid", context="talk")
    fig_static, ax1 = plt.subplots(figsize=(16, 9))
    
    color1 = 'steelblue'
    bars = ax1.bar(range(len(artist_counts)), artist_counts.values,
                   color=color1, alpha=0.75, edgecolor='black', linewidth=1.8)
    ax1.set_xlabel('Artistas', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Cantidad de Canciones', color=color1, fontsize=14, fontweight='bold')
    ax1.tick_params(axis='y', labelcolor=color1, labelsize=11)
    ax1.set_xticks(range(len(artist_counts)))
    ax1.set_xticklabels(artist_counts.index, rotation=45, ha='right', fontsize=11)
    ax1.grid(axis='y', alpha=0.3, linestyle='--')
    
    ax2 = ax1.twinx()
    color2 = '#DC143C'
    ax2.plot(range(len(cumulative_pct)), cumulative_pct.values,
             color=color2, marker='o', markersize=9, linewidth=3.5, 
             markeredgecolor='white', markeredgewidth=1.5)
    ax2.set_ylabel('Porcentaje Acumulado (%)', color=color2, fontsize=14, fontweight='bold')
    ax2.tick_params(axis='y', labelcolor=color2, labelsize=11)
    ax2.set_ylim([0, 105])
    ax2.axhline(y=80, color='gray', linestyle='--', linewidth=2.5, alpha=0.7, label='Línea 80%')
    ax2.legend(loc='lower right', fontsize=11)
    
    plt.title('📊 Gráfico de Pareto: Distribución de Canciones por Artista\n(Principio 80/20 - Ley de Pareto)',
              fontsize=20, fontweight='bold', pad=20, color='#1DB954')
    
    plt.tight_layout()
    fig_static.savefig('output/images/07_pareto.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig_static)
    
    # ==========================================
    # HTML INTERACTIVO (Plotly)
    # ==========================================
    
    print("✨ Generando gráfico interactivo...")
    
    # Crear figura con eje Y secundario
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Barras
    fig.add_trace(
        go.Bar(
            x=list(artist_counts.index),
            y=artist_counts.values,
            name='Cantidad de Canciones',
            marker_color='steelblue',
            opacity=0.7,
            text=artist_counts.values,
            textposition='outside',
            hovertemplate='<b>%{x}</b><br>Canciones: %{y}<extra></extra>'
        ),
        secondary_y=False
    )
    
    # Línea acumulativa
    fig.add_trace(
        go.Scatter(
            x=list(cumulative_pct.index),
            y=cumulative_pct.values,
            name='% Acumulado',
            mode='lines+markers',
            line=dict(color='darkred', width=3),
            marker=dict(size=10, symbol='circle'),
            hovertemplate='<b>%{x}</b><br>% Acumulado: %{y:. 1f}%<extra></extra>'
        ),
        secondary_y=True
    )
    
    # Línea de referencia 80%
    fig.add_hline(
        y=80,
        line_dash="dash",
        line_color="gray",
        line_width=2,
        opacity=0.7,
        annotation_text="80% (Pareto)",
        annotation_position="right",
        secondary_y=True
    )
    
    # Encontrar punto donde cruza 80%
    cross_80 = np.where(cumulative_pct.values >= 80)[0]
    if len(cross_80) > 0:
        idx_80 = cross_80[0]
        artist_80 = cumulative_pct.index[idx_80]
        
        fig.add_annotation(
            x=artist_80,
            y=80,
            text=f"<b>{idx_80 + 1} artistas<br>= 80% canciones</b>",
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor="red",
            ax=-80,
            ay=-50,
            bgcolor="yellow",
            opacity=0.8,
            font=dict(size=12, color="black"),
            xref="x",
            yref="y2"
        )
    
    # Configurar ejes
    fig.update_xaxes(
        title_text="<b>Artistas</b>",
        tickangle=-45,
        tickfont=dict(size=10)
    )
    
    fig.update_yaxes(
        title_text="<b>Cantidad de Canciones</b>",
        title_font=dict(color="steelblue"),
        tickfont=dict(color="steelblue"),
        secondary_y=False
    )
    
    fig.update_yaxes(
        title_text="<b>Porcentaje Acumulado (%)</b>",
        title_font=dict(color="darkred"),
        tickfont=dict(color="darkred"),
        range=[0, 105],
        secondary_y=True
    )
    
    # Layout
    fig.update_layout(
        title={
            'text': '<b>Gráfico de Pareto: Principio 80/20</b><br><sub>Ley de Pareto: Pocos artistas producen la mayor cantidad de canciones</sub>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#1DB954'}
        },
        template='plotly_white',
        height=700,
        hovermode='x unified',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    fig.write_html(
        'output/interactive/07_pareto.html',
        config={'displayModeBar': True, 'displaylogo': False},
        include_plotlyjs='cdn'
    )
    
    print("✅ Gráfico 7 completado!")
    print(f"   📄 PNG: output/images/07_pareto.png")
    print(f"   🌐 HTML: output/interactive/07_pareto.html")

if __name__ == "__main__":
    crear_pareto()