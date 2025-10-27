"""
Sistema de Gestión de Recursos Humanos
Archivo principal de la aplicación

Este sistema implementa una arquitectura MVC (Model-View-Controller) con interfaz gráfica Tkinter.

ROLES:
- 100: Administrador RH (gestiona empleados, proyectos, genera informes)
- 101: Gerente (gestiona departamentos)
- 102: Empleado (registra tiempos)

ARQUITECTURA:
- models/: Modelos de datos y acceso a base de datos
- views/: Interfaces gráficas
- controllers/: Lógica de negocio
- utils/: Utilidades y validaciones
- config.py: Configuración

AUTOR: Sistema RH
VERSION: 1.0.0
"""

import tkinter as tk
from tkinter import messagebox
import sys

# Importar vistas
from views.login_view import LoginView
from views.admin_view import AdminView
from views.manager_view import ManagerView
from views.employee_view import EmployeeView


class AplicacionRH:
    """Clase principal de la aplicación"""
    
    def __init__(self):
        """Inicializa la aplicación"""
        self.root = tk.Tk()
        self.usuario_actual = None
        self.configurar_ventana()
        self.mostrar_login()
    
    def configurar_ventana(self):
        """Configura la ventana principal"""
        self.root.title("Sistema de Gestión de Recursos Humanos")
        self.root.geometry("800x600")
        
        # Configurar cierre de ventana
        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_aplicacion)
    
    def mostrar_login(self):
        """Muestra la ventana de login"""
        LoginView(self.root, self.on_login_exitoso)
    
    def on_login_exitoso(self, usuario):
        """
        Callback cuando el login es exitoso
        
        Args:
            usuario: Diccionario con datos del usuario
        """
        self.usuario_actual = usuario
        rol = usuario.get('fk_id_rol_e')
        
        # Redirigir según el rol
        if rol == 100:  # Administrador RH
            AdminView(self.root, usuario, self.cerrar_sesion)
        elif rol == 101:  # Gerente
            ManagerView(self.root, usuario, self.cerrar_sesion)
        elif rol == 102:  # Empleado
            EmployeeView(self.root, usuario, self.cerrar_sesion)
        else:
            messagebox.showerror("Error", "Rol de usuario no reconocido")
            self.mostrar_login()
    
    def cerrar_sesion(self):
        """Cierra la sesión actual y vuelve al login"""
        if messagebox.askyesno("Cerrar Sesión", "¿Está seguro que desea cerrar sesión?"):
            self.usuario_actual = None
            self.mostrar_login()
    
    def cerrar_aplicacion(self):
        """Cierra la aplicación"""
        if messagebox.askyesno("Salir", "¿Está seguro que desea salir?"):
            self.root.quit()
            self.root.destroy()
            sys.exit(0)
    
    def ejecutar(self):
        """Inicia el loop principal de la aplicación"""
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            print("\n\nAplicación interrumpida por el usuario")
            sys.exit(0)
        except Exception as e:
            messagebox.showerror("Error Fatal", f"Error inesperado: {str(e)}")
            sys.exit(1)


def main():
    """Función principal"""
    try:
        app = AplicacionRH()
        app.ejecutar()
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
