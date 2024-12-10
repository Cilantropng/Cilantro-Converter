Versi�n: 1.1.1
Descripci�n: Esta es una actualizaci�n que soluciona los problemas de descarga y agrega la barra de progreso durante la conversi�n.


# Descargador de YouTube con FFmpeg y Tkinter

Este proyecto es una herramienta para descargar videos de YouTube en diferentes calidades (MP4, MP3, 360p) y convertirlos utilizando FFmpeg. La aplicaci�n cuenta con una interfaz gr�fica de usuario (GUI) creada con la biblioteca `Tkinter`.

## Caracter�sticas

- **Interfaz gr�fica** sencilla y f�cil de usar.
- **Descarga de videos** en varias calidades:
  - Mejor calidad disponible (MP4)
  - 360p (MP4)
  - Solo audio (MP3)
- **Conversi�n autom�tica** a MP3 o MP4 utilizando FFmpeg.
- **Requiere tener FFmpeg instalado** y especificar la ruta de la carpeta `bin` donde se encuentra FFmpeg.

## Requisitos

Antes de ejecutar la aplicaci�n, aseg�rate de tener los siguientes requisitos:

1. **Python 3.x** instalado en tu sistema.
2. **FFmpeg**: Aseg�rate de tener FFmpeg instalado. Si no lo tienes, puedes descargarlo desde [aqu�](https://ffmpeg.org/download.html).
3. **Dependencias de Python**:
   - `yt-dlp`: Para descargar videos de YouTube.
   - `tkinter`: Para la interfaz gr�fica (generalmente ya est� incluido en las distribuciones de Python).
   - `Pillow` y `requests`: Para manejar y mostrar im�genes en la GUI.

### Instalaci�n de dependencias:

Para instalar las dependencias necesarias, ejecuta el siguiente comando en tu terminal:

```bash
pip install yt-dlp pillow requests
