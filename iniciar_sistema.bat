@echo off
REM Script para iniciar el Sistema de Gestión de Recursos Humanos
title Sistema de Gestion de RRHH

echo ================================================
echo    Sistema de Gestion de Recursos Humanos
echo ================================================
echo.
echo Iniciando aplicacion...
echo.

REM Buscar el ejecutable de Python
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo ERROR: Python no esta instalado o no esta en el PATH
    echo Por favor instala Python 3.8 o superior
    pause
    exit /b 1
)

REM Verificar si existen las dependencias
python -c "import mysql.connector" 2>nul
if %errorlevel% neq 0 (
    echo.
    echo Instalando dependencias necesarias...
    pip install mysql-connector-python bcrypt
    echo.
)

REM Ejecutar la aplicacion
python main_gui.py

REM Si hay error, mostrar mensaje
if %errorlevel% neq 0 (
    echo.
    echo ERROR: La aplicacion se cerro inesperadamente
    echo.
    pause
)
