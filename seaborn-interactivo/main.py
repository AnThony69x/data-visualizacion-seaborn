"""
🎵 SISTEMA DE VISUALIZACIÓN DE DATOS DE SPOTIFY
===============================================
Programa principal con menú interactivo mejorado

Autores: Anthony Mejia & Emilio Cardenas
Fecha: Diciembre 2025
Universidad: ULEAM - Visualización de Datos
"""

import sys
import os
import webbrowser
from pathlib import Path
from colorama import Fore, Back, Style, init

# Inicializar colorama para colores en consola
init(autoreset=True)


class SpotifyVisualizerApp:
    """Aplicación principal de visualización de datos"""
    
    def __init__(self):
        self.running = True
        self.data_loaded = False
    
    def clear_screen(self):
        """Limpia la pantalla de la consola"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self):
        """Imprime el encabezado principal con diseño mejorado"""
        self.clear_screen()
        
        # Banner ASCII
        print(f"{Fore.GREEN}")
        print("""
    ███████╗██████╗  ██████╗ ████████╗██╗███████╗██╗   ██╗
    ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝██║██╔════╝╚██╗ ██╔╝
    ███████╗██████╔╝██║   ██║   ██║   ██║█████╗   ╚████╔╝ 
    ╚════██║██╔═══╝ ██║   ██║   ██║   ██║██╔══╝    ╚██╔╝  
    ███████║██║     ╚██████╔╝   ██║   ██║██║        ██║   
    ╚══════╝╚═╝      ╚═════╝    ╚═╝   ╚═╝╚═╝        ╚═╝   
    """)
        print(f"{Style.RESET_ALL}")
        print(f"{Back.GREEN}{Fore.BLACK}{'═'*70}{Style.RESET_ALL}")
        print(f"{Back.GREEN}{Fore.BLACK}{'  📊 SEABORN + PLOTLY VISUALIZER  ':^70}{Style.RESET_ALL}")
        print(f"{Back.GREEN}{Fore.BLACK}{'═'*70}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'  Universidad ULEAM - 2025  ':^70}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{'  Anthony Mejia & Emilio Cardenas  ':^70}{Style.RESET_ALL}")
        print(f"{Back.GREEN}{Fore.BLACK}{'═'*70}{Style.RESET_ALL}\n")
    
    def initialize(self):
        """Inicializa la aplicación y verifica archivos"""
        self.print_header()
        
        try:
            # Verificar que existe el dataset
            if not os.path.exists('data/spotify_data_limpio.csv'):
                print(f"{Fore.RED}❌ ERROR: No se encontró 'data/spotify_data_limpio.csv'{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}   Coloca tu dataset en la carpeta 'data/'{Style.RESET_ALL}")
                input(f"\n{Fore.CYAN}📌 Presiona Enter para salir...{Style.RESET_ALL}")
                sys.exit(1)
            
            # Crear carpetas de output si no existen
            os.makedirs('output/images', exist_ok=True)
            os.makedirs('output/interactive', exist_ok=True)
            
            print(f"{Fore.GREEN}✅ Sistema inicializado correctamente{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{'─'*70}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}  📁 Dataset encontrado: {Fore.WHITE}data/spotify_data_limpio.csv{Style.RESET_ALL}")
            print(f"{Fore.CYAN}  📊 Carpetas de salida: {Fore.WHITE}output/images/ y output/interactive/{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{'─'*70}{Style.RESET_ALL}")
            
            self.data_loaded = True
            input(f"\n{Fore.CYAN}📌 Presiona Enter para continuar al menú principal...{Style.RESET_ALL}")
            
        except Exception as e:
            print(f"{Fore.RED}❌ Error al inicializar: {e}{Style.RESET_ALL}")
            sys.exit(1)
    
    def show_menu(self):
        """Muestra el menú principal con diseño mejorado"""
        self.print_header()
        
        print(f"{Back.CYAN}{Fore.BLACK}{'  🎨 MENÚ DE VISUALIZACIONES  ':^70}{Style.RESET_ALL}\n")
        
        # OPCIONES PRINCIPALES
        print(f"{Back.BLUE}{Fore.WHITE}  📊 OPCIONES PRINCIPALES  {Style.RESET_ALL}")
        print(f"{Fore.CYAN}  1️⃣  {Fore.WHITE}Abrir Index HTML {Fore.YELLOW}(Ver todos los gráficos interactivos){Style.RESET_ALL}")
        print(f"{Fore.CYAN}  2️⃣  {Fore.WHITE}Generar y visualizar gráficos uno por uno{Style.RESET_ALL}")
        print(f"{Fore.CYAN}  3️⃣  {Fore.WHITE}Ver gráficos existentes uno por uno {Fore.YELLOW}(sin regenerar){Style.RESET_ALL}")
        print(f"{Fore.CYAN}  4️⃣  {Fore.WHITE}Ver un gráfico específico {Fore.YELLOW}(selección individual){Style.RESET_ALL}")
        
        # INFORMACIÓN
        print(f"\n{Back.MAGENTA}{Fore.WHITE}  📈 GRÁFICOS DISPONIBLES  {Style.RESET_ALL}")
        print(f"{Fore.GREEN}  1. 📊 Gráfico de Barras {Fore.YELLOW}(Top artistas por popularidad){Style.RESET_ALL}")
        print(f"{Fore.GREEN}  2. 🔥 Mapa de Calor {Fore.YELLOW}(Correlaciones entre variables){Style.RESET_ALL}")
        print(f"{Fore.GREEN}  3. 📈 Histogramas con KDE {Fore.YELLOW}(Distribuciones){Style.RESET_ALL}")
        print(f"{Fore.GREEN}  4. 📦 Boxplots {Fore.YELLOW}(Caja y bigotes){Style.RESET_ALL}")
        print(f"{Fore.GREEN}  5. 🐝 Gráfico de Enjambre {Fore.YELLOW}(Swarmplot){Style.RESET_ALL}")
        print(f"{Fore.GREEN}  6. 📉 Gráficos de Densidad KDE{Style.RESET_ALL}")
        print(f"{Fore.GREEN}  7. 📊 Gráfico de Pareto {Fore.YELLOW}(Principio 80/20){Style.RESET_ALL}")
        
        # SALIDA
        print(f"\n{Back.RED}{Fore.WHITE}  ❌ SALIR  {Style.RESET_ALL}")
        print(f"{Fore.RED}  0️⃣  {Fore.WHITE}Salir del sistema{Style.RESET_ALL}")
        
        print(f"\n{Fore.YELLOW}{'═'*70}{Style.RESET_ALL}")
    
    def abrir_index(self):
        """Abre el archivo index.html en el navegador"""
        self.print_header()
        
        index_path = Path(__file__).parent / "index.html"
        
        if not index_path.exists():
            print(f"{Fore.RED}❌ ERROR: No se encontró el archivo index.html{Style.RESET_ALL}")
            input(f"\n{Fore.CYAN}📌 Presiona Enter para continuar...{Style.RESET_ALL}")
            return
        
        print(f"{Back.BLUE}{Fore.WHITE}{'  🌐 ABRIENDO INDEX HTML  ':^70}{Style.RESET_ALL}\n")
        print(f"{Fore.CYAN}[>>] Abriendo index.html en el navegador...{Style.RESET_ALL}")
        
        try:
            webbrowser.open(f"file:///{index_path.absolute()}")
            print(f"{Fore.GREEN}[✓] Index abierto correctamente{Style.RESET_ALL}")
            print(f"\n{Fore.YELLOW}💡 Verás todos los 7 gráficos interactivos en tu navegador{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[ERROR] No se pudo abrir el navegador: {e}{Style.RESET_ALL}")
        
        input(f"\n{Fore.CYAN}📌 Presiona Enter para continuar...{Style.RESET_ALL}")
    
    def generar_graficos_individuales(self):
        """Genera y visualiza gráficos uno por uno, mostrándolos secuencialmente"""
        import tkinter as tk
        from tkinter import messagebox
        from PIL import Image, ImageTk
        from graficos.grafico_01_barras import crear_grafico_barras
        from graficos.grafico_02_mapa_calor import crear_mapa_calor
        from graficos.grafico_03_histogramas import crear_histogramas
        from graficos.grafico_04_boxplots import crear_boxplots
        from graficos.grafico_05_enjambre import crear_enjambre
        from graficos.grafico_06_kde import crear_kde
        from graficos.grafico_07_pareto import crear_pareto
        
        graficos = [
            {"num": 1, "nombre": "Gráfico de Barras", "funcion": crear_grafico_barras, "archivo": "01_barras.png"},
            {"num": 2, "nombre": "Mapa de Calor", "funcion": crear_mapa_calor, "archivo": "02_mapa_calor.png"},
            {"num": 3, "nombre": "Histogramas con KDE", "funcion": crear_histogramas, "archivo": "03_histogramas.png"},
            {"num": 4, "nombre": "Boxplots", "funcion": crear_boxplots, "archivo": "04_boxplots.png"},
            {"num": 5, "nombre": "Gráfico de Enjambre", "funcion": crear_enjambre, "archivo": "05_enjambre.png"},
            {"num": 6, "nombre": "Gráficos de Densidad (KDE)", "funcion": crear_kde, "archivo": "06_kde.png"},
            {"num": 7, "nombre": "Gráfico de Pareto", "funcion": crear_pareto, "archivo": "07_pareto.png"}
        ]
        
        self.print_header()
        print(f"{Back.MAGENTA}{Fore.WHITE}{'  📊 VISUALIZACIÓN SECUENCIAL DE GRÁFICOS  ':^70}{Style.RESET_ALL}\n")
        print(f"{Fore.YELLOW}Cada gráfico se generará y mostrará en una ventana.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Al cerrar la ventana, aparecerá automáticamente el siguiente.{Style.RESET_ALL}\n")
        print(f"{Fore.CYAN}Se generarán {len(graficos)} gráficos en total.{Style.RESET_ALL}\n")
        print(f"{Fore.YELLOW}{'─'*70}{Style.RESET_ALL}")
        input(f"\n{Fore.GREEN}👉 Presiona Enter para comenzar...{Style.RESET_ALL}")
        
        for grafico in graficos:
            print(f"\n{Fore.CYAN}[{grafico['num']}/7] Generando {grafico['nombre']}...{Style.RESET_ALL}")
            
            try:
                # Generar el gráfico
                grafico['funcion']()
                print(f"{Fore.GREEN}[✓] Gráfico generado correctamente{Style.RESET_ALL}")
                
                # Crear ventana para mostrar el gráfico
                ventana = tk.Tk()
                ventana.title(f"[{grafico['num']}/7] {grafico['nombre']}")
                ventana.geometry("1200x800")
                ventana.configure(bg='#1a1a1a')
                
                # Frame superior con título
                frame_titulo = tk.Frame(ventana, bg='#1DB954', height=80)
                frame_titulo.pack(fill='x', pady=(0, 10))
                
                titulo = tk.Label(frame_titulo, text=f"[{grafico['num']}/7] {grafico['nombre']}", 
                                 font=('Arial', 18, 'bold'), bg='#1DB954', fg='white')
                titulo.pack(pady=25)
                
                # Frame central para la imagen
                frame_imagen = tk.Frame(ventana, bg='#2a2a2a', relief='solid', borderwidth=2)
                frame_imagen.pack(fill='both', expand=True, padx=20, pady=10)
                
                # Cargar y mostrar la imagen
                try:
                    ruta_imagen = f"output/images/{grafico['archivo']}"
                    imagen = Image.open(ruta_imagen)
                    imagen.thumbnail((1100, 650), Image.Resampling.LANCZOS)
                    photo = ImageTk.PhotoImage(imagen)
                    
                    imagen_label = tk.Label(frame_imagen, image=photo, bg='#2a2a2a')
                    imagen_label.image = photo  # Mantener referencia
                    imagen_label.pack(expand=True)
                    
                except Exception as e:
                    error_label = tk.Label(frame_imagen, text=f"Error al cargar imagen:\n{e}",
                                          font=('Arial', 12), bg='#2a2a2a', fg='#ff5555')
                    error_label.pack(expand=True)
                
                # Frame inferior con información
                frame_info = tk.Frame(ventana, bg='#1a1a1a')
                frame_info.pack(fill='x', padx=20, pady=15)
                
                info_text = f"Gráfico {grafico['num']} de 7 | Cierra esta ventana para continuar con el siguiente"
                if grafico['num'] == 7:
                    info_text = "Gráfico 7 de 7 | ÚLTIMO GRÁFICO | Cierra para finalizar"
                
                info_label = tk.Label(frame_info, text=info_text,
                                    font=('Arial', 11), bg='#1a1a1a', fg='#1DB954')
                info_label.pack()
                
                # Botón para cerrar
                btn_cerrar = tk.Button(frame_info, text="Cerrar y Continuar ►" if grafico['num'] < 7 else "✓ Finalizar",
                                      font=('Arial', 12, 'bold'), bg='#1DB954', fg='white',
                                      activebackground='#1ed760', width=20, height=2,
                                      command=ventana.destroy)
                btn_cerrar.pack(pady=10)
                
                # Centrar ventana
                ventana.update_idletasks()
                x = (ventana.winfo_screenwidth() // 2) - (ventana.winfo_width() // 2)
                y = (ventana.winfo_screenheight() // 2) - (ventana.winfo_height() // 2)
                ventana.geometry(f"+{x}+{y}")
                
                # Mostrar ventana (bloquea hasta que se cierre)
                print(f"{Fore.YELLOW}[>>] Mostrando ventana... (ciérrala para continuar){Style.RESET_ALL}")
                ventana.mainloop()
                print(f"{Fore.GREEN}[✓] Ventana cerrada{Style.RESET_ALL}")
                
            except Exception as e:
                print(f"{Fore.RED}[ERROR] Error al procesar el gráfico: {e}{Style.RESET_ALL}")
                import traceback
                traceback.print_exc()
        
        print(f"\n{Fore.YELLOW}{'═'*70}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}✅ Todos los gráficos han sido visualizados{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{'═'*70}{Style.RESET_ALL}")
        input(f"\n{Fore.CYAN}📌 Presiona Enter para volver al menú...{Style.RESET_ALL}")
    
    def generar_todos_graficos(self):
        """Genera todos los gráficos sin visualizar"""
        import generar_graficos
        
        self.print_header()
        
        print(f"{Back.GREEN}{Fore.BLACK}{'  🎨 GENERANDO TODAS LAS VISUALIZACIONES  ':^70}{Style.RESET_ALL}\n")
        print(f"{Fore.YELLOW}Se generarán los 7 gráficos completos (PNG + HTML interactivo){Style.RESET_ALL}\n")
        print(f"{Fore.YELLOW}{'═'*70}{Style.RESET_ALL}")
        
        try:
            # Ejecutar el script de generación
            generar_graficos.main()
            
            print(f"\n{Fore.YELLOW}{'═'*70}{Style.RESET_ALL}")
            print(f"{Back.BLUE}{Fore.WHITE}{'  📊 GENERACIÓN COMPLETADA  ':^70}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{'═'*70}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}✅ Todos los gráficos generados correctamente{Style.RESET_ALL}")
            print(f"\n{Fore.CYAN}📁 Los archivos se guardaron en:{Style.RESET_ALL}")
            print(f"{Fore.WHITE}   • PNG estáticos:  {Fore.GREEN}output/images/ (300 DPI){Style.RESET_ALL}")
            print(f"{Fore.WHITE}   • HTML interactivos: {Fore.GREEN}output/interactive/{Style.RESET_ALL}")
            print(f"\n{Fore.YELLOW}💡 Abre index.html para ver todos los gráficos en el navegador{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{'═'*70}{Style.RESET_ALL}")
            
        except Exception as e:
            print(f"\n{Fore.RED}❌ Error durante la generación: {e}{Style.RESET_ALL}")
            import traceback
            traceback.print_exc()
        
        input(f"\n{Fore.CYAN}📌 Presiona Enter para continuar...{Style.RESET_ALL}")
    
    def ver_graficos_existentes(self):
        """Muestra los gráficos existentes uno por uno sin regenerar"""
        import tkinter as tk
        from PIL import Image, ImageTk
        
        graficos = [
            {"num": 1, "nombre": "Gráfico de Barras", "archivo": "01_barras.png"},
            {"num": 2, "nombre": "Mapa de Calor", "archivo": "02_mapa_calor.png"},
            {"num": 3, "nombre": "Histogramas con KDE", "archivo": "03_histogramas.png"},
            {"num": 4, "nombre": "Boxplots", "archivo": "04_boxplots.png"},
            {"num": 5, "nombre": "Gráfico de Enjambre", "archivo": "05_enjambre.png"},
            {"num": 6, "nombre": "Gráficos de Densidad (KDE)", "archivo": "06_kde.png"},
            {"num": 7, "nombre": "Gráfico de Pareto", "archivo": "07_pareto.png"}
        ]
        
        self.print_header()
        print(f"{Back.MAGENTA}{Fore.WHITE}{'  👁️  VISUALIZACIÓN DE GRÁFICOS EXISTENTES  ':^70}{Style.RESET_ALL}\n")
        print(f"{Fore.YELLOW}Se mostrarán los gráficos ya generados.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Si algún gráfico no existe, será omitido.{Style.RESET_ALL}\n")
        
        # Verificar cuáles gráficos existen
        graficos_existentes = []
        for grafico in graficos:
            ruta = f"output/images/{grafico['archivo']}"
            if os.path.exists(ruta):
                graficos_existentes.append(grafico)
        
        if not graficos_existentes:
            print(f"{Fore.RED}❌ No se encontraron gráficos generados{Style.RESET_ALL}")
            print(f"\n{Fore.YELLOW}💡 Usa la opción 2 o 3 para generar los gráficos primero{Style.RESET_ALL}")
            input(f"\n{Fore.CYAN}📌 Presiona Enter para continuar...{Style.RESET_ALL}")
            return
        
        print(f"{Fore.GREEN}✅ Se encontraron {len(graficos_existentes)} gráficos generados{Style.RESET_ALL}\n")
        print(f"{Fore.YELLOW}{'─'*70}{Style.RESET_ALL}")
        input(f"\n{Fore.GREEN}👉 Presiona Enter para comenzar...{Style.RESET_ALL}")
        
        for i, grafico in enumerate(graficos_existentes, 1):
            print(f"\n{Fore.CYAN}[{i}/{len(graficos_existentes)}] Mostrando {grafico['nombre']}...{Style.RESET_ALL}")
            
            try:
                # Crear ventana para mostrar el gráfico
                ventana = tk.Tk()
                ventana.title(f"[{grafico['num']}/7] {grafico['nombre']}")
                ventana.geometry("1200x800")
                ventana.configure(bg='#1a1a1a')
                
                # Frame superior con título
                frame_titulo = tk.Frame(ventana, bg='#1DB954', height=80)
                frame_titulo.pack(fill='x', pady=(0, 10))
                
                titulo = tk.Label(frame_titulo, text=f"[{grafico['num']}/7] {grafico['nombre']}", 
                                 font=('Arial', 18, 'bold'), bg='#1DB954', fg='white')
                titulo.pack(pady=25)
                
                # Frame central para la imagen
                frame_imagen = tk.Frame(ventana, bg='#2a2a2a', relief='solid', borderwidth=2)
                frame_imagen.pack(fill='both', expand=True, padx=20, pady=10)
                
                # Cargar y mostrar la imagen
                try:
                    ruta_imagen = f"output/images/{grafico['archivo']}"
                    imagen = Image.open(ruta_imagen)
                    imagen.thumbnail((1100, 650), Image.Resampling.LANCZOS)
                    photo = ImageTk.PhotoImage(imagen)
                    
                    imagen_label = tk.Label(frame_imagen, image=photo, bg='#2a2a2a')
                    imagen_label.image = photo  # Mantener referencia
                    imagen_label.pack(expand=True)
                    
                except Exception as e:
                    error_label = tk.Label(frame_imagen, text=f"Error al cargar imagen:\n{e}",
                                          font=('Arial', 12), bg='#2a2a2a', fg='#ff5555')
                    error_label.pack(expand=True)
                
                # Frame inferior con información
                frame_info = tk.Frame(ventana, bg='#1a1a1a')
                frame_info.pack(fill='x', padx=20, pady=15)
                
                info_text = f"Gráfico {i} de {len(graficos_existentes)} | Cierra esta ventana para continuar"
                if i == len(graficos_existentes):
                    info_text = f"Gráfico {i} de {len(graficos_existentes)} | ÚLTIMO | Cierra para finalizar"
                
                info_label = tk.Label(frame_info, text=info_text,
                                    font=('Arial', 11), bg='#1a1a1a', fg='#1DB954')
                info_label.pack()
                
                # Botón para cerrar
                btn_cerrar = tk.Button(frame_info, text="Cerrar y Continuar ►" if i < len(graficos_existentes) else "✓ Finalizar",
                                      font=('Arial', 12, 'bold'), bg='#1DB954', fg='white',
                                      activebackground='#1ed760', width=20, height=2,
                                      command=ventana.destroy)
                btn_cerrar.pack(pady=10)
                
                # Centrar ventana
                ventana.update_idletasks()
                x = (ventana.winfo_screenwidth() // 2) - (ventana.winfo_width() // 2)
                y = (ventana.winfo_screenheight() // 2) - (ventana.winfo_height() // 2)
                ventana.geometry(f"+{x}+{y}")
                
                # Mostrar ventana (bloquea hasta que se cierre)
                print(f"{Fore.YELLOW}[>>] Mostrando ventana... (ciérrala para continuar){Style.RESET_ALL}")
                ventana.mainloop()
                print(f"{Fore.GREEN}[✓] Ventana cerrada{Style.RESET_ALL}")
                
            except Exception as e:
                print(f"{Fore.RED}[ERROR] Error al mostrar el gráfico: {e}{Style.RESET_ALL}")
                import traceback
                traceback.print_exc()
        
        print(f"\n{Fore.YELLOW}{'═'*70}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}✅ Visualización completada{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{'═'*70}{Style.RESET_ALL}")
        print(f"\n{Fore.CYAN}📌 Presiona Enter para volver al menú...{Style.RESET_ALL}")
    
    def ver_grafico_individual(self):
        """Permite seleccionar y ver un gráfico específico"""
        import tkinter as tk
        from PIL import Image, ImageTk
        
        graficos = [
            {"num": 1, "nombre": "Gráfico de Barras", "archivo": "01_barras.png"},
            {"num": 2, "nombre": "Mapa de Calor", "archivo": "02_mapa_calor.png"},
            {"num": 3, "nombre": "Histogramas con KDE", "archivo": "03_histogramas.png"},
            {"num": 4, "nombre": "Boxplots", "archivo": "04_boxplots.png"},
            {"num": 5, "nombre": "Gráfico de Enjambre", "archivo": "05_enjambre.png"},
            {"num": 6, "nombre": "Gráficos de Densidad (KDE)", "archivo": "06_kde.png"},
            {"num": 7, "nombre": "Gráfico de Pareto", "archivo": "07_pareto.png"}
        ]
        
        self.print_header()
        print(f"{Back.MAGENTA}{Fore.WHITE}{'  🎯 SELECCIÓN DE GRÁFICO INDIVIDUAL  ':^70}{Style.RESET_ALL}\n")
        
        # Mostrar opciones de gráficos
        print(f"{Fore.YELLOW}Selecciona el gráfico que deseas visualizar:{Style.RESET_ALL}\n")
        print(f"{Fore.YELLOW}{'─'*70}{Style.RESET_ALL}")
        
        for grafico in graficos:
            ruta = f"output/images/{grafico['archivo']}"
            if os.path.exists(ruta):
                estado = f"{Fore.GREEN}✓ Disponible{Style.RESET_ALL}"
            else:
                estado = f"{Fore.RED}✗ No generado{Style.RESET_ALL}"
            
            print(f"{Fore.CYAN}  {grafico['num']}. {Fore.WHITE}{grafico['nombre']:<35} {estado}")
        
        print(f"{Fore.YELLOW}{'─'*70}{Style.RESET_ALL}")
        print(f"{Fore.RED}  0. Volver al menú principal{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{'─'*70}{Style.RESET_ALL}\n")
        
        try:
            seleccion = input(f"{Fore.GREEN}👉 Selecciona un gráfico (0-7): {Style.RESET_ALL}").strip()
            
            if seleccion == '0':
                return
            
            num_seleccion = int(seleccion)
            
            if num_seleccion < 1 or num_seleccion > 7:
                print(f"\n{Fore.RED}❌ Opción inválida. Debe ser un número entre 1 y 7{Style.RESET_ALL}")
                input(f"\n{Fore.CYAN}📌 Presiona Enter para continuar...{Style.RESET_ALL}")
                return
            
            grafico_seleccionado = graficos[num_seleccion - 1]
            ruta_imagen = f"output/images/{grafico_seleccionado['archivo']}"
            
            if not os.path.exists(ruta_imagen):
                print(f"\n{Fore.RED}❌ El gráfico '{grafico_seleccionado['nombre']}' no ha sido generado aún{Style.RESET_ALL}")
                print(f"\n{Fore.YELLOW}💡 Usa la opción 2 del menú principal para generar los gráficos{Style.RESET_ALL}")
                input(f"\n{Fore.CYAN}📌 Presiona Enter para continuar...{Style.RESET_ALL}")
                return
            
            print(f"\n{Fore.CYAN}[>>] Abriendo {grafico_seleccionado['nombre']}...{Style.RESET_ALL}")
            
            # Crear ventana para mostrar el gráfico
            ventana = tk.Tk()
            ventana.title(f"[{grafico_seleccionado['num']}/7] {grafico_seleccionado['nombre']}")
            ventana.geometry("1200x800")
            ventana.configure(bg='#1a1a1a')
            
            # Frame superior con título
            frame_titulo = tk.Frame(ventana, bg='#1DB954', height=80)
            frame_titulo.pack(fill='x', pady=(0, 10))
            
            titulo = tk.Label(frame_titulo, text=f"[{grafico_seleccionado['num']}/7] {grafico_seleccionado['nombre']}", 
                             font=('Arial', 18, 'bold'), bg='#1DB954', fg='white')
            titulo.pack(pady=25)
            
            # Frame central para la imagen
            frame_imagen = tk.Frame(ventana, bg='#2a2a2a', relief='solid', borderwidth=2)
            frame_imagen.pack(fill='both', expand=True, padx=20, pady=10)
            
            # Cargar y mostrar la imagen
            try:
                imagen = Image.open(ruta_imagen)
                imagen.thumbnail((1100, 650), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(imagen)
                
                imagen_label = tk.Label(frame_imagen, image=photo, bg='#2a2a2a')
                imagen_label.image = photo  # Mantener referencia
                imagen_label.pack(expand=True)
                
            except Exception as e:
                error_label = tk.Label(frame_imagen, text=f"Error al cargar imagen:\n{e}",
                                      font=('Arial', 12), bg='#2a2a2a', fg='#ff5555')
                error_label.pack(expand=True)
            
            # Frame inferior con información
            frame_info = tk.Frame(ventana, bg='#1a1a1a')
            frame_info.pack(fill='x', padx=20, pady=15)
            
            info_label = tk.Label(frame_info, text=f"Gráfico {grafico_seleccionado['num']} de 7 | Cierra esta ventana para volver al menú",
                                font=('Arial', 11), bg='#1a1a1a', fg='#1DB954')
            info_label.pack()
            
            # Botón para cerrar
            btn_cerrar = tk.Button(frame_info, text="✓ Cerrar",
                                  font=('Arial', 12, 'bold'), bg='#1DB954', fg='white',
                                  activebackground='#1ed760', width=20, height=2,
                                  command=ventana.destroy)
            btn_cerrar.pack(pady=10)
            
            # Centrar ventana
            ventana.update_idletasks()
            x = (ventana.winfo_screenwidth() // 2) - (ventana.winfo_width() // 2)
            y = (ventana.winfo_screenheight() // 2) - (ventana.winfo_height() // 2)
            ventana.geometry(f"+{x}+{y}")
            
            # Mostrar ventana
            print(f"{Fore.GREEN}[✓] Ventana abierta{Style.RESET_ALL}")
            ventana.mainloop()
            print(f"{Fore.GREEN}[✓] Ventana cerrada{Style.RESET_ALL}")
            
        except ValueError:
            print(f"\n{Fore.RED}❌ Entrada inválida. Debes ingresar un número{Style.RESET_ALL}")
            input(f"\n{Fore.CYAN}📌 Presiona Enter para continuar...{Style.RESET_ALL}")
        except Exception as e:
            print(f"\n{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")
            import traceback
            traceback.print_exc()
            input(f"\n{Fore.CYAN}📌 Presiona Enter para continuar...{Style.RESET_ALL}")
    
    def exit_app(self):
        """Sale de la aplicación con diseño mejorado"""
        self.print_header()
        
        print(f"{Back.RED}{Fore.WHITE}{'  👋 CERRANDO SISTEMA  ':^70}{Style.RESET_ALL}\n")
        print(f"{Fore.CYAN}Gracias por usar el Sistema de Visualización de Datos de Spotify{Style.RESET_ALL}")
        print(f"\n{Fore.YELLOW}👥 Desarrollado por:{Style.RESET_ALL}")
        print(f"{Fore.GREEN}   • Anthony Mejia{Style.RESET_ALL}")
        print(f"{Fore.GREEN}   • Emilio Cardenas{Style.RESET_ALL}")
        print(f"\n{Fore.CYAN}🎓 Universidad: ULEAM - Visualización de Datos{Style.RESET_ALL}")
        print(f"{Fore.CYAN}📅 Fecha: Diciembre 2025{Style.RESET_ALL}")
        print(f"{Fore.CYAN}📊 Librería Principal: Seaborn + Plotly{Style.RESET_ALL}\n")
        print(f"{Fore.YELLOW}{'═'*70}{Style.RESET_ALL}\n")
        
        self.running = False
    
    def handle_choice(self, choice):
        """Maneja la selección del usuario"""
        
        actions = {
            '1': self.abrir_index,
            '2': self.generar_graficos_individuales,
            '3': self.ver_graficos_existentes,
            '4': self.ver_grafico_individual,
            '0': self.exit_app
        }
        
        action = actions.get(choice)
        
        if action:
            try:
                action()
            except Exception as e:
                print(f"\n{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")
                import traceback
                print(f"\n{Fore.RED}{'='*70}")
                print(f"{'DETALLES DEL ERROR':^70}")
                print(f"{'='*70}{Style.RESET_ALL}")
                traceback.print_exc()
                print(f"{Fore.RED}{'='*70}{Style.RESET_ALL}")
                input(f"\n{Fore.CYAN}📌 Presiona Enter para continuar...{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.YELLOW}⚠️  Opción inválida. Por favor, intenta de nuevo.{Style.RESET_ALL}")
            input(f"\n{Fore.CYAN}📌 Presiona Enter para continuar...{Style.RESET_ALL}")
    
    def run(self):
        """Ejecuta el loop principal de la aplicación"""
        self.initialize()
        
        while self.running:
            self.show_menu()
            choice = input(f"\n{Fore.GREEN}👉 Selecciona una opción: {Style.RESET_ALL}").strip()
            self.handle_choice(choice)


def main():
    """Función principal"""
    try:
        app = SpotifyVisualizerApp()
        app.run()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.RED}⚠️  Programa interrumpido por el usuario{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}👋 ¡Hasta luego!{Style.RESET_ALL}\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}❌ Error fatal: {e}{Style.RESET_ALL}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
