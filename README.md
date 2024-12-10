Versión: 1.1.1
Descripción: Esta es una actualización que soluciona los problemas de descarga y agrega la barra de progreso durante la conversión.


# Descargador de YouTube con FFmpeg y Tkinter

Este proyecto es una herramienta para descargar videos de YouTube en diferentes calidades (MP4, MP3, 360p) y convertirlos utilizando FFmpeg. La aplicación cuenta con una interfaz gráfica de usuario (GUI) creada con la biblioteca `Tkinter`.

## Características

- **Interfaz gráfica** sencilla y fácil de usar.
- **Descarga de videos** en varias calidades:
  - Mejor calidad disponible (MP4)
  - 360p (MP4)
  - Solo audio (MP3)
- **Conversión automática** a MP3 o MP4 utilizando FFmpeg.
- **Requiere tener FFmpeg instalado** y especificar la ruta de la carpeta `bin` donde se encuentra FFmpeg.

## Requisitos

Antes de ejecutar la aplicación, asegúrate de tener los siguientes requisitos:

1. **Python 3.x** instalado en tu sistema.
2. **FFmpeg**: Asegúrate de tener FFmpeg instalado. Si no lo tienes, puedes descargarlo desde [aquí](https://ffmpeg.org/download.html).
3. **Dependencias de Python**:
   - `yt-dlp`: Para descargar videos de YouTube.
   - `tkinter`: Para la interfaz gráfica (generalmente ya está incluido en las distribuciones de Python).
   - `Pillow` y `requests`: Para manejar y mostrar imágenes en la GUI.

### Instalación de dependencias:

Para instalar las dependencias necesarias, ejecuta el siguiente comando en tu terminal:

```bash
pip install yt-dlp pillow requests
