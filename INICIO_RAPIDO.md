# 🚀 GUÍA DE INICIO RÁPIDO

Comienza a usar el sistema en menos de 5 minutos.

## ⚡ Inicio Ultra-Rápido

### Opción 1: Doble clic (RECOMENDADO - Windows)
1. Doble clic en `iniciar_sistema.pyw` (sin consola)
2. O en `iniciar_sistema.bat` (con consola visible)

### Opción 2: Terminal
```bash
python main_gui.py
```

---

## 📋 CONFIGURACIÓN INICIAL (Primera vez)

### 1️⃣ Instalar Python (si no lo tienes)
- Descargar: https://www.python.org/downloads/
- Versión mínima: **Python 3.8**
- ✅ **IMPORTANTE:** Marcar "Add Python to PATH" durante instalación

### 2️⃣ Instalar MySQL (si no lo tienes)
- Descargar: https://dev.mysql.com/downloads/mysql/
- Recordar usuario (por defecto: `root`) y contraseña

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```
O manualmente:
```bash
pip install mysql-connector-python bcrypt
```

### 4️⃣ Crear base de datos
```bash
mysql -u root -p < dbEmpresa.sql
```

### 5️⃣ Configurar credenciales
Editar `config.py`:
```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',              # Tu usuario MySQL
    'password': '',              # Tu contraseña MySQL
    'database': 'dbEmpresa'
}
```

### 6️⃣ ¡Listo! Ejecuta
```bash
python main_gui.py
```

---

## 👤 PRIMER USO

### Registrar usuario inicial
1. En la pantalla de login → **"Registrarse"**
2. Completar formulario:
   - Nombre, Apellido, Edad, Dirección, Teléfono
   - Correo: ejemplo@email.com (usado para login)
   - **Rol: Admin RH (100)** para acceso completo
   - Contraseña: mínimo 8 caracteres
3. Clic en **"Registrarse"**
4. **Iniciar sesión** con las credenciales creadas

---

## 🎯 USOS COMUNES POR ROL

### Como Administrador (Rol 100)

**Crear un Empleado:**
- Tab "Gestionar Empleados" → "Nuevo"
- Llenar datos y guardar

**Crear y Asignar Proyecto:**
- Tab "Gestionar Proyectos" → "Nuevo Proyecto"
- Tab "Asignaciones" → Ingresar ID Empleado e ID Proyecto

**Generar Informe:**
- Tab "Informes" → Seleccionar tipo
- Archivo .txt se genera en carpeta `informes/`

**Control de Registro Público:**
- Botón en header: **"Registro Público: [Estado]"**
- Clic para habilitar/deshabilitar

### Como Gerente (Rol 101)

**Crear Departamento:**
- Tab "Gestionar Departamentos" → "Nuevo"
- Ingresar nombre y guardar

**Asignar Empleados:**
- Tab "Asignar Empleados" → Seleccionar empleado
- Ingresar ID del departamento y confirmar

### Como Empleado (Rol 102)

**Registrar Tiempo Trabajado:**
- Tab "Registrar Tiempo"
- Seleccionar fecha, ingresar horas (máx. 12)
- Seleccionar proyecto y escribir descripción
- Guardar

**Ver Histórico:**
- Tab "Mis Registros" → Ver todos los registros
- Tab "Mis Proyectos" → Ver proyectos asignados

---

## 🔍 ENCONTRAR IDs

**ID de Empleados:**
- Admin: Tab "Gestionar Empleados" → Columna ID

**ID de Proyectos:**
- Admin: Tab "Gestionar Proyectos" → Columna ID

**ID de Departamentos:**
- Gerente: Tab "Gestionar Departamentos" → Columna ID

---

## 🐛 SOLUCIÓN DE PROBLEMAS

### ❌ "Python no está instalado"
→ Instalar Python 3.8+ desde python.org

### ❌ "ModuleNotFoundError: mysql.connector"
```bash
pip install mysql-connector-python bcrypt
```

### ❌ "Can't connect to MySQL server"
- Verificar que MySQL esté ejecutándose
- Verificar usuario/contraseña en `config.py`
- Verificar que existe la BD `dbEmpresa`

### ❌ "Access denied for user"
- Cambiar contraseña en `config.py`
- Verificar permisos del usuario MySQL

### ❌ SQL error al crear base de datos
- Eliminar base de datos antigua:
```sql
DROP DATABASE IF EXISTS dbEmpresa;
```
- Ejecutar de nuevo `dbEmpresa.sql`

### ❌ "El correo ya está registrado"
- Cada correo se usa una sola vez
- Usar otro correo o editar el existente

### ❌ "No aparece el botón Registrarse"
- El admin lo deshabilitó
- Contactar al admin para que habilite o cree usuario

---

## 📁 ESTRUCTURA DE ARCHIVOS

```
📁 Proyecto/
├── 🚀 iniciar_sistema.bat    ← AQUÍ para con consola
├── 🚀 iniciar_sistema.pyw    ← AQUÍ para sin consola
├── 📄 main_gui.py
├── ⚙️ config.py              ← Editar credenciales
├── 🗄️ dbEmpresa.sql
├── 📋 requirements.txt
├── 📁 models/
├── 📁 views/
├── 📁 controllers/
├── 📁 utils/
└── 📖 README.md              ← Documentación completa
```

---

## 📚 MÁS INFORMACIÓN

- **README.md** - Documentación completa
- **RESUMEN_PROYECTO.md** - Resumen ejecutivo
- **dbEmpresa.sql** - Estructura de base de datos

---

**🎉 ¡Listo! Ahora haz doble clic en `iniciar_sistema.pyw`**
