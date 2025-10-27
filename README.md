# 🏢 Sistema de Gestión de Recursos Humanos

Sistema integral de gestión de RRHH con interfaz gráfica desarrollado en Python con Tkinter y arquitectura MVC.

## 📋 Tabla de Contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación Rápida](#instalación-rápida)
- [Primer Uso](#primer-uso)
- [Roles del Sistema](#roles-del-sistema)
- [Estructura](#estructura)
- [Documentación](#documentación)

## 🚀 Características

- **Interfaz Gráfica Moderna** con Tkinter
- **3 Roles** con permisos diferenciados
- **CRUD completo** de empleados, proyectos y departamentos
- **Registro de tiempos** con validación legal (máx. 12h/día)
- **Generación de informes** en TXT
- **Seguridad** con contraseñas hasheadas (bcrypt)
- **Validaciones** de datos completas en formularios
- **Control dinámico** de registro público

## 🏗️ Arquitectura MVC

```
models/          → Capa de datos (6 modelos)
views/           → Interfaces gráficas (5 vistas)
controllers/     → Lógica de negocio (6 controladores)
utils/           → Validadores y helpers
config.py        → Configuración centralizada
main_gui.py      → Punto de entrada
```

**Ventajas:** Separación de responsabilidades, mantenibilidad, testabilidad y escalabilidad.

## 📦 Requisitos

- **Python** 3.8+
- **MySQL** 5.7+
- **Dependencias:** `mysql-connector-python`, `bcrypt`

## 🔧 Instalación Rápida

### 1. Clonar o descargar proyecto

```bash
cd "ruta/del/proyecto"
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Crear base de datos

```bash
mysql -u root -p < dbEmpresa.sql
```

### 4. Configurar `config.py`

Editar las credenciales de MySQL:

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',              # Tu usuario
    'password': 'tu_contraseña', # Tu contraseña
    'database': 'dbEmpresa'
}
```

### 5. Ejecutar aplicación

```bash
python main_gui.py
```

O doble clic en: `iniciar_sistema.pyw`

## 👤 Primer Uso

1. **Registrar usuario inicial**
   - Clic en "Registrarse" en pantalla de login
   - Completar datos personales
   - Seleccionar rol: **Admin RH (100)** para acceso completo
   - Crear contraseña (mín. 8 caracteres)

2. **Iniciar sesión** con las credenciales creadas

3. **Usar el sistema** según tu rol

## 👥 Roles del Sistema

### 🔴 Administrador RH (100)
- CRUD completo de empleados
- CRUD completo de proyectos
- Asignar/desasignar proyectos
- Generar 3 tipos de informes
- Control de registro público
- Ver todas las asignaciones

### 🟠 Gerente (101)
- CRUD de departamentos
- Asignar empleados a departamentos
- Ver empleados por departamento
- Restricciones de seguridad por rol

### 🟡 Empleado (102)
- Registrar tiempo trabajado
- Asociar horas a proyectos
- Ver histórico de tiempos
- Ver proyectos asignados
- Validación: máx. 12h/día

## 🔍 Estructura del Proyecto

```
📁 Proyecto/
├── 🚀 iniciar_sistema.bat      # Iniciar con consola
├── 🚀 iniciar_sistema.pyw      # Iniciar sin consola
├── 📄 main_gui.py              # Punto de entrada
├── ⚙️ config.py                # Configuración
├── 🗄️ dbEmpresa.sql            # Base de datos
├── 📋 requirements.txt         # Dependencias
├── 📁 models/                  # Capa de datos
├── 📁 views/                   # Interfaces gráficas
├── 📁 controllers/             # Lógica de negocio
├── 📁 utils/                   # Validadores
└── 📖 README.md                # Este archivo
```

## 📚 Documentación

- **[INICIO_RAPIDO.md](./INICIO_RAPIDO.md)** - Guía de inicio rápido (primeros pasos)
- **[RESUMEN_PROYECTO.md](./RESUMEN_PROYECTO.md)** - Resumen ejecutivo del proyecto
- **[dbEmpresa.sql](./dbEmpresa.sql)** - Estructura de base de datos

## 🐛 Solución de Problemas

### Error: "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### Error: "Can't connect to MySQL"
- Verificar que MySQL esté ejecutándose
- Verificar credenciales en `config.py`
- Verificar que existe la BD `dbEmpresa`

### Error: "Access denied for user"
- Actualizar contraseña de MySQL en `config.py`
- Verificar permisos del usuario

### "Máximo 12 horas por día"
- Validación de ley laboral chilena
- Ya registraste horas en esa fecha

## 📝 Notas

- Todas las contraseñas se encriptan con bcrypt
- Las validaciones protegen contra inyección SQL
- El sistema genera timestamps en los informes
- Confirmación requerida para acciones críticas

---

**¿Listo?** Ejecuta: `python main_gui.py` o haz doble clic en `iniciar_sistema.pyw` (o `iniciar_sistema.bat`)
