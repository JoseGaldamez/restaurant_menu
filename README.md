# Aplicación de Menú de Restaurante

Esta es una aplicación de escritorio desarrollada en **Python** utilizando el framework **Kivy**. Simula la interfaz de una aplicación móvil para visualizar el menú de un restaurante, permitiendo navegar entre categorías y ver productos con sus precios.

## 🚀 Funcionalidades

- **Navegación Fluida**: Utiliza `ScreenManager` para transiciones suaves entre la pantalla de inicio, categorías y lista de productos.
- **Carga Dinámica de Datos**: El menú se carga automáticamente desde un archivo `menu.json`, lo que facilita la actualización de precios y productos sin tocar el código.
- **Interfaz Adaptable**: Configurada con una resolución de 360x640 para simular la experiencia de uso en un smartphone.
- **Diseño Limpio**: Uso de `ScrollView` y `BoxLayout` para una presentación ordenada y desplazable.

## 📋 Requisitos Previos

Necesitas tener instalado **Python 3.7** o superior.

## ⚙️ Instalación y Ejecución

1.  **Clonar este repositorio** o descargar los archivos en tu computadora.

2.  **Crear un entorno virtual** (recomendado):

    ```bash
    python -m venv env
    ```

3.  **Activar el entorno virtual**:
    - En Windows: `.\env\Scripts\activate`
    - En macOS/Linux: `source env/bin/activate`

4.  **Instalar las dependencias**:
    La dependencia principal es Kivy.

    ```bash
    pip install kivy
    ```

    _Nota: Si estás en Windows, Kivy instalará automáticamente `kivy_deps.sdl2` y `kivy_deps.glew`._

5.  **Ejecutar la aplicación**:
    ```bash
    python main.py
    ```

## 📦 Compilación (Crear Ejecutable .exe)

Para convertir esta aplicación en un ejecutable de Windows (`.exe`), utilizamos **PyInstaller**. El proyecto ya incluye un archivo de configuración `RestauranteMenu.spec` listo para usar.

1.  **Instalar PyInstaller**:
    Asegúrate de tener el entorno virtual activado y ejecuta:

    ```bash
    pip install pyinstaller
    ```

2.  **Generar el Ejecutable**:
    Ejecuta el siguiente comando en la raíz del proyecto para iniciar la compilación usando el archivo de especificaciones incluido:

    ```bash
    pyinstaller RestauranteMenu.spec
    ```

3.  **Localizar el Archivo**:
    Una vez finalizado el proceso, encontrarás la carpeta de la aplicación en:
    `dist/RestauranteMenu/RestauranteMenu.exe`

    Puedes mover esta carpeta `RestauranteMenu` a cualquier otra computadora con Windows y la aplicación funcionará sin necesidad de instalar Python.

## 📁 Estructura del Proyecto

- `main.py`: Código fuente principal de la aplicación.
- `menu.json`: Base de datos de categorías y productos.
- `RestauranteMenu.spec`: Archivo de configuración para PyInstaller.
