#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Launcher para el Sistema de Gestión de Recursos Humanos
Este archivo inicia la aplicación sin mostrar ventana de consola
"""

import sys
import os
import subprocess

# Agregar el directorio actual al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    # Importar y ejecutar la aplicación principal
    from main_gui import main
    main()
except ImportError as e:
    import tkinter as tk
    from tkinter import messagebox
    
    root = tk.Tk()
    root.withdraw()
    
    error_msg = f"""Error al iniciar la aplicación:

{str(e)}

Por favor instale las dependencias:
pip install mysql-connector-python bcrypt

O ejecute: iniciar_sistema.bat"""
    
    messagebox.showerror("Error de Dependencias", error_msg)
    sys.exit(1)
except Exception as e:
    import tkinter as tk
    from tkinter import messagebox
    
    root = tk.Tk()
    root.withdraw()
    
    error_msg = f"""Error inesperado al iniciar:

{str(e)}

Por favor verifique:
1. Python 3.8+ instalado
2. Base de datos MySQL configurada
3. Archivo config.py con credenciales correctas"""
    
    messagebox.showerror("Error", error_msg)
    sys.exit(1)
