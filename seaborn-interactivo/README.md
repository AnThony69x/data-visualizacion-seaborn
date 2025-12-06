# 🎵 Spotify Data Visualizer - Seaborn + Plotly

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Seaborn](https://img.shields.io/badge/Seaborn-0.13.2-green?logo=python)
![Plotly](https://img.shields.io/badge/Plotly-6.5.0-purple?logo=plotly)
![Pandas](https://img.shields.io/badge/Pandas-2.3.3-orange?logo=pandas)
![License](https://img.shields.io/badge/License-MIT-yellow)

**Proyecto de Visualización de Datos de Spotify usando Seaborn y Plotly**  
Desarrollado para la Universidad Laica Eloy Alfaro de Manabí (ULEAM)

---

## 📋 Tabla de Contenidos

- [Descripción](#-descripción)
- [Características](#-características)
- [Librerías Utilizadas](#-librerías-utilizadas)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Gráficos Generados](#-gráficos-generados)
- [Dataset](#-dataset)
- [Autores](#-autores)
- [Análisis de Resultados](#-análisis-de-resultados)

---

## 📖 Descripción

Este proyecto implementa un **sistema completo de visualización de datos** que analiza información de Spotify utilizando dos enfoques complementarios:

1. **📊 Gráficos Estáticos (PNG)** - Generados con **Seaborn** para análisis profesional
2. **🌐 Gráficos Interactivos (HTML)** - Generados con **Plotly** para exploración dinámica

El sistema procesa **8,579 registros de canciones de Spotify** y genera **7 tipos diferentes de visualizaciones** que revelan patrones sobre popularidad, correlaciones entre variables, distribuciones estadísticas y el principio de Pareto en la industria musical.

---

## ✨ Características

- ✅ **Doble Formato de Salida**: PNG (300 DPI) + HTML interactivo
- ✅ **7 Tipos de Gráficos**: Barras, Mapa de Calor, Histogramas, Boxplots, Swarmplot, KDE, Pareto
- ✅ **100% Interactivo**: Zoom, pan, hover tooltips en gráficos HTML
- ✅ **Análisis Estadístico Avanzado**: Correlaciones, densidades, outliers, distribuciones
- ✅ **Diseño Profesional**: Colores de Spotify, gradientes, sombras
- ✅ **Interfaz Web Completa**: index.html con todos los gráficos embebidos
- ✅ **Exportación Fácil**: Descarga de PNG desde la interfaz web
- ✅ **Código Modular**: Cada gráfico es un módulo independiente
- ✅ **Documentación Completa**: Análisis detallado de cada visualización

---

## 📚 Librerías Utilizadas

Este proyecto utiliza las siguientes librerías de Python, cada una con un propósito específico:

### 🌟 **Librerías Principales**

#### 1. **Seaborn (v0.13.2)** - 📊 LIBRERÍA BASE PARA GRÁFICOS ESTÁTICOS
```python
import seaborn as sns
```
**Propósito:** Crear visualizaciones estadísticas profesionales y estéticas
- ✅ Genera gráficos PNG de alta calidad (300 DPI)
- ✅ Estilos predefinidos (`whitegrid`, `white`, `talk`)
- ✅ Integración automática con Pandas DataFrames
- ✅ Gráficos especializados: `barplot`, `heatmap`, `histplot`, `boxplot`, `swarmplot`, `kdeplot`
- ✅ Paletas de colores profesionales (`viridis`, `Set2`, `pastel`, `husl`)

**Uso en el proyecto:**
- Todos los gráficos PNG se generan con Seaborn
- Base visual para la presentación del proyecto
- Análisis estadístico con curvas KDE automáticas

#### 2. **Plotly (v6.5.0)** - 🌐 LIBRERÍA PARA INTERACTIVIDAD
```python
import plotly.graph_objects as go
import plotly.express as px
```
**Propósito:** Crear visualizaciones interactivas HTML
- ✅ Zoom, pan, hover tooltips dinámicos
- ✅ Exportación a HTML standalone
- ✅ Gráficos responsivos y modernos
- ✅ Subplots con múltiples paneles
- ✅ Ejes duales (Pareto)

**Uso en el proyecto:**
- Todos los gráficos HTML interactivos
- Permite exploración dinámica de datos
- Visualizaciones embebidas en index.html

#### 3. **Pandas (v2.3.3)** - 🐼 MANIPULACIÓN DE DATOS
```python
import pandas as pd
```
**Propósito:** Cargar, filtrar y procesar datos
- ✅ Lectura de CSV: `pd.read_csv()`
- ✅ Agrupaciones: `groupby()`, `value_counts()`
- ✅ Filtrado: `nlargest()`, `isin()`
- ✅ Cálculos: `mean()`, `corr()`, `cumsum()`

**Uso en el proyecto:**
- Carga del dataset `spotify_data_limpio.csv`
- Procesamiento de top artistas, correlaciones
- Preparación de datos para visualización

#### 4. **Matplotlib (v3.10.7)** - 🎨 BACKEND DE SEABORN
```python
import matplotlib.pyplot as plt
```
**Propósito:** Motor detrás de Seaborn + personalización avanzada
- ✅ Configuración de figuras: `plt.subplots()`, `figsize`
- ✅ Títulos, etiquetas, leyendas
- ✅ Guardado de imágenes: `savefig(dpi=300)`
- ✅ Grid, rotación de ejes, colores personalizados

**Uso en el proyecto:**
- Seaborn está construido sobre Matplotlib
- Personalización de títulos, ejes, colores
- Exportación de PNG de alta resolución

### 🔧 **Librerías de Soporte**

#### 5. **NumPy (v2.3.5)** - 🔢 OPERACIONES MATEMÁTICAS
```python
import numpy as np
```
**Propósito:** Cálculos numéricos y arrays
- ✅ Logaritmos: `np.log10()`, `np.logspace()`
- ✅ Máscaras triangulares: `np.triu()`
- ✅ Histogramas manuales: `np.histogram()`

**Uso en el proyecto:**
- Bins logarítmicos para histograma de seguidores
- Máscara para mapa de calor triangular
- Cálculos estadísticos avanzados

#### 6. **SciPy (v1.16.3)** - 📐 FUNCIONES ESTADÍSTICAS
```python
from scipy import stats
```
**Propósito:** Funciones científicas y estadísticas
- ✅ Dependencia interna de Seaborn
- ✅ Cálculos de densidad (KDE)
- ✅ Pruebas estadísticas

**Uso en el proyecto:**
- Cálculos internos de Seaborn para KDE
- Estimación de densidad de probabilidad

#### 7. **Kaleido (v0.2.1)** - 📸 EXPORTACIÓN DE PLOTLY
```python
# Usado internamente por Plotly
```
**Propósito:** Convertir gráficos Plotly a imágenes estáticas
- ✅ Exportación a PNG/JPG desde HTML
- ✅ Renderizado headless

**Uso en el proyecto:**
- Opcional: permite exportar gráficos Plotly como PNG
- En este proyecto se usa Plotly principalmente para HTML

---

## 🎨 Flujo de Trabajo de las Librerías

```
┌─────────────────────────────────────────────────┐
│          DATOS DE ENTRADA                        │
│  spotify_data_limpio.csv (8,579 registros)      │
└──────────────────┬──────────────────────────────┘
                   │
                   ▼
         ┌─────────────────┐
         │  PANDAS 🐼       │ ← Carga y procesa CSV
         │  Limpia y filtra │
         └────────┬─────────┘
                  │
         ┌────────┴─────────┐
         │                  │
         ▼                  ▼
┌─────────────────┐  ┌──────────────────┐
│  SEABORN 📊     │  │  PLOTLY 🌐       │
│  + Matplotlib   │  │  Gráficos        │
│  Gráficos PNG   │  │  HTML            │
└────────┬────────┘  └────────┬─────────┘
         │                     │
         │  NumPy 🔢           │
         │  (cálculos)         │
         │                     │
         │  SciPy 📐           │
         │  (estadísticas)     │
         │                     │
         ▼                     ▼
┌─────────────────┐  ┌──────────────────┐
│  output/images/ │  │ output/          │
│  01_barras.png  │  │ interactive/     │
│  02_mapa...png  │  │ 01_barras.html   │
│  ... (7 PNGs)   │  │ ... (7 HTMLs)    │
└─────────────────┘  └──────────────────┘
         │                     │
         └──────────┬──────────┘
                    ▼
         ┌─────────────────────┐
         │   index.html        │
         │  Interfaz completa  │
         └─────────────────────┘
```

---

## 📁 Estructura del Proyecto

```
seaborn-interactivo/
│
├── 📄 generar_graficos.py          # Script principal - orquestador
├── 📄 index.html                   # Interfaz web completa
├── 📄 requirements.txt             # Dependencias del proyecto
├── 📄 README.md                    # Esta documentación
│
├── 📁 data/
│   └── spotify_data_limpio.csv     # Dataset (8,579 canciones)
│
├── 📁 graficos/                    # Módulos de visualización
│   ├── __init__.py                 # Inicializador del paquete
│   ├── grafico_01_barras.py        # Top 15 artistas
│   ├── grafico_02_mapa_calor.py    # Correlaciones
│   ├── grafico_03_histogramas.py   # Distribuciones
│   ├── grafico_04_boxplots.py      # Dispersión y outliers
│   ├── grafico_05_enjambre.py      # Swarmplot
│   ├── grafico_06_kde.py           # Densidades
│   └── grafico_07_pareto.py        # Principio 80/20
│
└── 📁 output/
    ├── 📁 images/                  # Gráficos PNG estáticos
    │   ├── 01_barras.png
    │   ├── 02_mapa_calor.png
    │   ├── 03_histogramas.png
    │   ├── 04_boxplots.png
    │   ├── 05_enjambre.png
    │   ├── 06_kde.png
    │   └── 07_pareto.png
    │
    └── 📁 interactive/             # Gráficos HTML interactivos
        ├── 01_barras.html
        ├── 02_mapa_calor.html
        ├── 03_histogramas.html
        ├── 04_boxplots.html
        ├── 05_enjambre.html
        ├── 06_kde.html
        └── 07_pareto.html
```

---

## 🚀 Instalación

### Requisitos Previos
- Python 3.13 o superior
- pip (gestor de paquetes de Python)

### Paso 1: Clonar o Descargar el Proyecto
```bash
cd "ruta/del/proyecto/seaborn-interactivo"
```

### Paso 2: Instalar Dependencias
```bash
pip install -r requirements.txt
```

Esto instalará:
- pandas>=2.0.0
- numpy>=1.24.0
- seaborn>=0.12.0
- matplotlib>=3.7.0
- plotly>=5.18.0
- scipy>=1.10.0
- kaleido>=0.2.1

---

## 💻 Uso

### Opción 1: Generar Todos los Gráficos
```bash
python generar_graficos.py
```

**Salida esperada:**
```
======================================================================
🎵 SPOTIFY DATA VISUALIZER - SEABORN + PLOTLY
======================================================================
📅 Fecha: 2025-12-06
👥 Autores: Anthony Mejia & Emilio Cardenas
======================================================================

🚀 Generando gráficos interactivos...

⏳ [1/7] Generando 1️⃣ Gráfico de Barras...
✅ Gráfico 1 completado!
   📄 PNG: output/images/01_barras.png
   🌐 HTML: output/interactive/01_barras.html

⏳ [2/7] Generando 2️⃣ Mapa de Calor...
✅ Gráfico 2 completado!
...

======================================================================
📊 RESUMEN FINAL
======================================================================
✅ Gráficos exitosos: 7
❌ Gráficos fallidos: 0
⏱️ Tiempo total: ~40 segundos
======================================================================
```

### Opción 2: Ver la Interfaz Web
1. Abre el archivo `index.html` en tu navegador
2. Navega por los 7 gráficos interactivos
3. Usa zoom, hover y descarga de PNG

### Opción 3: Generar un Solo Gráfico
```bash
python -m graficos.grafico_01_barras
python -m graficos.grafico_02_mapa_calor
# ... etc
```

---

## 📊 Gráficos Generados

### 1️⃣ **Gráfico de Barras** (`01_barras.png` / `.html`)
**Librería:** Seaborn (`sns.barplot`) + Plotly (`go.Bar`)  
**Variables:** Artista (eje Y) vs Popularidad Promedio 0-100 (eje X)  
**Descripción:** Ranking de los top 15 artistas más populares de Spotify

**Análisis:**
- Taylor Swift domina con ~100 de popularidad promedio
- Top 5 concentrados en 90-100 (superestrellas)
- Brecha entre primeros 5 y el resto

### 2️⃣ **Mapa de Calor** (`02_mapa_calor.png` / `.html`)
**Librería:** Seaborn (`sns.heatmap`) + Plotly (`go.Heatmap`)  
**Variables:** Popularidad Canción, Popularidad Artista, Seguidores Artista, Duración (min)  
**Descripción:** Matriz de correlaciones entre variables numéricas

**Análisis:**
- Correlación FUERTE (0.64): Popularidad Artista ↔ Seguidores
- Correlación MODERADA (0.47): Popularidad Canción ↔ Popularidad Artista
- Correlación DÉBIL (0.11-0.21): Duración no afecta éxito

### 3️⃣ **Histogramas** (`03_histogramas.png` / `.html`)
**Librería:** Seaborn (`sns.histplot`) + Plotly (`go.Histogram`)  
**Variables:** (1) Popularidad, (2) Duración, (3) Contenido Explícito, (4) Seguidores (log)  
**Descripción:** 4 paneles de distribución de frecuencias

**Análisis:**
- Distribución BIMODAL en popularidad (picos en 0 y 70-80)
- Duración centrada en 3-4 minutos (estándar industria)
- Contenido explícito NO afecta popularidad

### 4️⃣ **Boxplots** (`04_boxplots.png` / `.html`)
**Librería:** Seaborn (`sns.boxplot`) + Plotly (`go.Box`)  
**Variables:** 4 análisis de dispersión con outliers  
**Descripción:** Diagramas de caja y bigotes

**Análisis:**
- Medianas similares (~55-70) en artistas top
- Albums más variables que singles en duración
- The Weeknd es el más consistente

### 5️⃣ **Gráfico de Enjambre** (`05_enjambre.png` / `.html`)
**Librería:** Seaborn (`sns.swarmplot`) + Plotly (`go.Scatter`)  
**Variables:** Cada punto = 1 canción (muestra 500)  
**Descripción:** Visualización de puntos individuales sin superposición

**Análisis:**
- Taylor Swift y The Weeknd: alta densidad en 60-80
- Revela distribución completa sin ocultar datos
- Nirvana más disperso (catálogo antiguo)

### 6️⃣ **Gráficos KDE** (`06_kde.png` / `.html`)
**Librería:** Seaborn (`sns.kdeplot`) + Plotly (`ff.create_distplot`)  
**Variables:** 4 estimaciones de densidad de probabilidad  
**Descripción:** Curvas suavizadas de distribución

**Análisis:**
- Bimodalidad confirmada (0 y 70-75)
- Explícito vs No Explícito: curvas IDÉNTICAS
- Duración perfectamente normal (3.5 min)

### 7️⃣ **Gráfico de Pareto** (`07_pareto.png` / `.html`)
**Librería:** Matplotlib (dual axis) + Plotly (`make_subplots`)  
**Variables:** Cantidad de canciones + Porcentaje acumulado  
**Descripción:** Principio 80/20 - Ley de Pareto

**Análisis:**
- Principio confirmado: 10 artistas = 80% canciones
- Taylor Swift: ~330 canciones (dominio absoluto)
- Concentración típica de la industria musical

---

## 📊 Dataset

**Archivo:** `data/spotify_data_limpio.csv`  
**Registros:** 8,579 canciones  
**Variables principales:**
- `artist_name`: Nombre del artista
- `track_name`: Nombre de la canción
- `track_popularity`: Popularidad (0-100)
- `artist_popularity`: Popularidad del artista (0-100)
- `artist_followers`: Número de seguidores
- `track_duration_min`: Duración en minutos
- `explicit`: Contenido explícito (True/False)
- `album_type`: Tipo de álbum (album, single, compilation)

**Fuente:** Datos recopilados de Spotify API  
**Preprocesamiento:** Limpieza de valores nulos y duplicados

---

## 👥 Autores

**Anthony Mejia** & **Emilio Cardenas**  
Universidad Laica Eloy Alfaro de Manabí (ULEAM)  
Materia: Visualización de Datos  
Fecha: Diciembre 2025

---

## 🔍 Análisis de Resultados

### Conclusiones Generales

1. **Concentración de Poder**: Pocos artistas dominan en popularidad y producción
2. **Contenido Explícito es Neutral**: NO afecta positiva ni negativamente
3. **Duración Estándar**: La industria converge hacia 3-4 minutos
4. **Bimodalidad**: Las canciones son hits (70-80) o no son escuchadas (0)
5. **Fama del Artista Importa**: Correlación 0.64 entre popularidad y seguidores
6. **Consistencia de Top Artists**: Los grandes mantienen calidad uniforme
7. **Ley de Pareto Confirmada**: 20% de artistas generan 80% del contenido

### Insights Clave

- **Taylor Swift** es la artista más prolífica y popular del dataset
- **The Weeknd** es el artista más consistente en popularidad
- Tener muchos **seguidores** garantiza un piso de popularidad (~50) pero no garantiza hits individuales
- Las **canciones antiguas** (Nirvana) muestran patrones diferentes a las actuales
- La **duración de las canciones** no influye en el éxito (correlación 0.11)

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.

---

## 🙏 Agradecimientos

- **Seaborn** por facilitar visualizaciones estadísticas elegantes
- **Plotly** por revolucionar la interactividad en Python
- **Pandas** por hacer el análisis de datos accesible
- **Spotify** por proporcionar datos de música

---

## 📞 Contacto

Para preguntas o sugerencias sobre este proyecto, contactar a los autores a través de la universidad.

---

**Hecho con ❤️ usando Python, Seaborn y Plotly**
