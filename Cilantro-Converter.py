import yt_dlp
import subprocess
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
import requests
from io import BytesIO

# ChatGPT Ayudo mucho aqui.

# Función para verificar si FFmpeg está instalado en la carpeta bin
def check_ffmpeg(ffmpeg_folder):
    ffmpeg_path = os.path.join(ffmpeg_folder, "ffmpeg.exe")
    if not os.path.isfile(ffmpeg_path):
        messagebox.showerror("Error", f"FFmpeg no se encuentra en la carpeta especificada: {ffmpeg_path}.")
        return False
    try:
        # Intentamos ejecutar ffmpeg para verificar si funciona
        subprocess.run([ffmpeg_path, '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "FFmpeg no se pudo ejecutar correctamente.")
        return False

# Función para descargar el video
def Download(link, quality, ffmpeg_folder, output_format):
    # Comprobar si FFmpeg está instalado y accesible
    if not check_ffmpeg(ffmpeg_folder):
        return

    # Obtener la ruta del directorio actual (donde está el archivo o script)
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Configuración para descargar el video con la calidad especificada
    ffmpeg_path = os.path.join(ffmpeg_folder, "ffmpeg.exe")
    ydl_opts = {
        'format': quality,  # Selector de calidad
        'outtmpl': os.path.join(current_directory, '%(title)s.%(ext)s'),  # Guardar en el mismo directorio
        'ffmpeg_location': ffmpeg_path,  # Ruta a FFmpeg
    }

    # Si es solo audio (MP3), se agrega la opción para convertir a MP3
    if output_format == 'mp3':
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Convertir a MP3
            'preferredquality': '192',  # Calidad de audio (192 kbps)
        }]
    elif output_format == 'mp4':
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Convertir a MP4
        }]
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    messagebox.showinfo("Éxito", "La descarga y conversión se completaron con éxito.")

# Función para manejar el evento de descarga
def on_download():
    ffmpeg_folder = ffmpeg_entry.get()
    link = link_entry.get()
    quality_option = quality_var.get()
    
    # Validar enlace
    if not link:
        messagebox.showerror("Error", "Por favor ingresa un enlace de YouTube.")
        return

    # Validar la ruta de FFmpeg
    if not os.path.isdir(ffmpeg_folder):
        messagebox.showerror("Error", "La ruta proporcionada no es válida.")
        return

    # Asignar calidad y formato de salida
    if quality_option == 1:
        quality = 'best'  # Mejor calidad disponible
        output_format = 'mp4'  # MP4
    elif quality_option == 2:
        quality = 'bestvideo[height<=360]+bestaudio/best[height<=360]'  # 360p
        output_format = 'mp4'  # MP4
    elif quality_option == 3:
        quality = 'bestaudio'  # Solo audio
        output_format = 'mp3'  # MP3
    else:
        messagebox.showerror("Error", "Opción de calidad inválida.")
        return

    # Llamar a la función de descarga
    Download(link, quality, ffmpeg_folder, output_format)

# Función para cargar imagen desde URL
def load_image_from_url(url):
    response = requests.get(url)
    img_data = BytesIO(response.content)
    img = Image.open(img_data)
    return ImageTk.PhotoImage(img)

# Crear la ventana principal
root = tk.Tk()
root.title("Descargador de YouTube")

# Cargar la imagen del logo desde la URL
logo_url = "https://cdn.discordapp.com/attachments/1295796184815763516/1315400900348481586/dec.jpg?ex=6757460d&is=6755f48d&hm=85f838a21ec9b0e1af4a80e0ea3218499af57dfb0b97dca61f419a62b334f1b0&"
logo_image = load_image_from_url(logo_url)

# Guardar la referencia a la imagen para evitar que se descarte
root.logo_image = logo_image  # Mantener la referencia a la imagen

# Etiquetas y campos de entrada
tk.Label(root, text="Ruta de la carpeta bin de FFmpeg :").pack(pady=5)
ffmpeg_entry = tk.Entry(root, width=50)
ffmpeg_entry.pack(pady=5)

tk.Label(root, text="Enlace de YouTube:").pack(pady=5)
link_entry = tk.Entry(root, width=50)
link_entry.pack(pady=5)

tk.Label(root, text="Selecciona la calidad:").pack(pady=5)

quality_var = tk.IntVar()

tk.Radiobutton(root, text="Mejor calidad (MP4)", variable=quality_var, value=1).pack(anchor="w", padx=20)
tk.Radiobutton(root, text="360p (MP4)", variable=quality_var, value=2).pack(anchor="w", padx=20)
tk.Radiobutton(root, text="Solo audio (MP3)", variable=quality_var, value=3).pack(anchor="w", padx=20)

# Mostrar el logo
logo_label = tk.Label(root, image=logo_image)
logo_label.pack(pady=10)

# Botón de descarga
download_button = tk.Button(root, text="Descargar", command=on_download)
download_button.pack(pady=20)

# Ejecutar la interfaz gráfica
root.mainloop()
