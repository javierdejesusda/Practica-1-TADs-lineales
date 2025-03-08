# Guía de Instalación y Ejecución

## Requisitos Previos

Asegúrese de tener Python 3 instalado en su sistema antes de proceder.

## Configuración del Entorno

Para configurar correctamente el entorno de ejecución, siga estos pasos secuencialmente:

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar el entorno virtual
# En Windows:
./venv/Scripts/activate
# En macOS/Linux:
# source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

## Estructura del Proyecto

El proyecto consta de dos archivos principales:

- `practica.py`: Contiene la implementación principal del trabajo
- `test.py`: Contiene las pruebas unitarias para verificar el correcto funcionamiento

## Ejecución de Pruebas

Para verificar que la implementación funciona correctamente, ejecute las pruebas con el siguiente comando:

```bash
python -m pytest test.py -v
```

La opción `-v` proporciona información detallada sobre cada prueba ejecutada.