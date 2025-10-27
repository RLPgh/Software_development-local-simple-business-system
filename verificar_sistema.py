"""
Script de verificación del sistema
Valida que todo esté correctamente configurado antes de iniciar
"""

import sys
import os

def verificar_python():
    """Verifica la versión de Python"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} (se requiere 3.8+)")
        return False

def verificar_dependencias():
    """Verifica que las dependencias estén instaladas"""
    dependencias = {
        'mysql.connector': 'mysql-connector-python',
        'bcrypt': 'bcrypt',
        'tkinter': 'tkinter (incluido en Python)'
    }
    
    todas_ok = True
    for modulo, paquete in dependencias.items():
        try:
            if modulo == 'mysql.connector':
                __import__('mysql.connector')
            else:
                __import__(modulo)
            print(f"✅ {paquete}")
        except ImportError:
            print(f"❌ {paquete} - Ejecutar: pip install {paquete.split()[0]}")
            todas_ok = False
    
    return todas_ok

def verificar_mysql():
    """Verifica la conexión a MySQL"""
    try:
        import mysql.connector
        from config import DB_CONFIG
        
        # Intentar conectar sin especificar base de datos
        config_test = DB_CONFIG.copy()
        database = config_test.pop('database')
        
        conn = mysql.connector.connect(**config_test)
        cursor = conn.cursor()
        
        # Verificar si existe la base de datos
        cursor.execute("SHOW DATABASES LIKE %s", (database,))
        existe = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        if existe:
            print(f"✅ MySQL - Base de datos '{database}' existe")
            return True
        else:
            print(f"⚠️  MySQL conectado pero falta crear base de datos '{database}'")
            print(f"   Ejecutar: mysql -u root -p < dbEmpresa.sql")
            return False
            
    except ImportError:
        print("❌ MySQL - mysql-connector-python no instalado")
        return False
    except Exception as e:
        print(f"❌ MySQL - Error de conexión: {str(e)}")
        print("   Verificar credenciales en config.py")
        return False

def verificar_archivos():
    """Verifica que existan los archivos necesarios"""
    archivos_necesarios = [
        'main_gui.py',
        'config.py',
        'dbEmpresa.sql',
        'models/database.py',
        'views/login_view.py',
        'controllers/auth_controller.py'
    ]
    
    todas_ok = True
    for archivo in archivos_necesarios:
        if os.path.exists(archivo):
            print(f"✅ {archivo}")
        else:
            print(f"❌ {archivo} no encontrado")
            todas_ok = False
    
    return todas_ok

def main():
    """Función principal de verificación"""
    print("=" * 60)
    print("  VERIFICACIÓN DEL SISTEMA DE GESTIÓN DE RRHH")
    print("=" * 60)
    print()
    
    print("📌 Verificando Python...")
    python_ok = verificar_python()
    print()
    
    print("📌 Verificando dependencias...")
    deps_ok = verificar_dependencias()
    print()
    
    print("📌 Verificando archivos del sistema...")
    archivos_ok = verificar_archivos()
    print()
    
    print("📌 Verificando conexión a MySQL...")
    mysql_ok = verificar_mysql()
    print()
    
    print("=" * 60)
    if python_ok and deps_ok and archivos_ok and mysql_ok:
        print("✅ SISTEMA LISTO PARA USAR")
        print("   Ejecutar: python main_gui.py")
        print("   O doble clic en: iniciar_sistema.bat")
    else:
        print("❌ SISTEMA NO ESTÁ LISTO")
        print("   Revisar los errores anteriores y corregir")
    print("=" * 60)

if __name__ == "__main__":
    try:
        main()
        input("\nPresiona Enter para salir...")
    except KeyboardInterrupt:
        print("\n\nVerificación cancelada")
        sys.exit(0)
