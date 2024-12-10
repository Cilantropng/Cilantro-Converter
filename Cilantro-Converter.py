import yt_dlp
import subprocess
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import threading  # Importar threading

# Función para verificar si FFmpeg está instalado en la carpeta bin
def check_ffmpeg(ffmpeg_folder):
    ffmpeg_path = os.path.join(ffmpeg_folder, "ffmpeg.exe")
    if not os.path.isfile(ffmpeg_path):
        messagebox.showerror("Error", f"FFmpeg no se encuentra en la carpeta especificada: {ffmpeg_path}.")
        return False
    try:
        subprocess.run([ffmpeg_path, '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "FFmpeg no se pudo ejecutar correctamente.")
        return False

# Función para descargar el video y actualizar la barra de progreso
def Download(link, quality, ffmpeg_folder, output_format, progress_bar, progress_label):
    if not check_ffmpeg(ffmpeg_folder):
        return

    current_directory = os.path.dirname(os.path.abspath(__file__))
    ffmpeg_path = os.path.join(ffmpeg_folder, "ffmpeg.exe")
    ydl_opts = {
        'format': quality,
        'outtmpl': os.path.join(current_directory, '%(title)s.%(ext)s'),
        'ffmpeg_location': ffmpeg_path,
        'progress_hooks': [progress_hook(progress_bar, progress_label)]  # Para la barra de progreso
    }

    if output_format == 'mp3':
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    elif output_format == 'mp4':
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }]
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    messagebox.showinfo("Éxito", "La descarga y conversión se completaron con éxito.")

# Función para actualizar la barra de progreso
def progress_hook(progress_bar, progress_label):
    def hook(d):
        if d['status'] == 'downloading':
            percent = d['downloaded_bytes'] / d['total_bytes'] * 100
            progress_bar['value'] = percent
            progress_label.config(text=f"{int(percent)}%")
        elif d['status'] == 'finished':
            progress_bar['value'] = 100
            progress_label.config(text="Convirtiendo Archivo")
    return hook

# Función para manejar el evento de descarga en un hilo separado
def on_download():
    ffmpeg_folder = ffmpeg_entry.get()
    link = link_entry.get()
    quality_option = quality_var.get()
    
    if not link:
        messagebox.showerror("Error", "Por favor ingresa un enlace de YouTube.")
        return

    if not os.path.isdir(ffmpeg_folder):
        messagebox.showerror("Error", "La ruta proporcionada no es válida.")
        return

    if quality_option == 1:
        quality = 'best'
        output_format = 'mp4'
    elif quality_option == 2:
        quality = 'bestvideo[height<=360]+bestaudio/best[height<=360]'
        output_format = 'mp4'
    elif quality_option == 3:
        quality = 'bestaudio'
        output_format = 'mp3'
    else:
        messagebox.showerror("Error", "Opción de calidad inválida.")
        return

    # Crear un hilo para ejecutar la descarga sin bloquear la interfaz
    download_thread = threading.Thread(target=Download, args=(link, quality, ffmpeg_folder, output_format, progress_bar, progress_label))
    download_thread.start()

# Función para cargar la imagen desde un archivo local
def load_image_from_path(path):
    img = Image.open(path)
    return ImageTk.PhotoImage(img)

# Crear la ventana principal
root = tk.Tk()
root.title("Descargador de YouTube")

# Crear un Canvas para la barra de desplazamiento
canvas = tk.Canvas(root)
canvas.pack(side="left", fill="both", expand=True)

# Crear una barra de desplazamiento
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Asociar la barra de desplazamiento con el canvas
canvas.configure(yscrollcommand=scrollbar.set)

# Crear un frame dentro del canvas para contener los widgets
frame = tk.Frame(canvas)

# Crear una ventana en el canvas
canvas.create_window((0, 0), window=frame, anchor="nw")

# Cargar la imagen del logo
logo_path = r"imagen(es de kanaria la foto)\dec.jpg"  
logo_image = load_image_from_path(logo_path)

# Guardar la referencia a la imagen para evitar que se descarte
root.logo_image = logo_image

# Etiquetas y campos de entrada dentro del frame
logo_label = tk.Label(frame, image=logo_image)
logo_label.pack(pady=10)

tk.Label(frame, text="Ruta de la carpeta bin de FFmpeg :").pack(pady=5)
ffmpeg_entry = tk.Entry(frame, width=50)
ffmpeg_entry.pack(pady=5)

tk.Label(frame, text="Enlace de YouTube:").pack(pady=5)
link_entry = tk.Entry(frame, width=50)
link_entry.pack(pady=5)

tk.Label(frame, text="Selecciona la calidad:").pack(pady=5)

quality_var = tk.IntVar()

tk.Radiobutton(frame, text="Mejor calidad (MP4)", variable=quality_var, value=1).pack(anchor="w", padx=20)
tk.Radiobutton(frame, text="360p (MP4)", variable=quality_var, value=2).pack(anchor="w", padx=20)
tk.Radiobutton(frame, text="Solo audio (MP3)", variable=quality_var, value=3).pack(anchor="w", padx=20)

# Barra de progreso
progress_bar = ttk.Progressbar(frame, length=400, mode="determinate")
progress_bar.pack(pady=10)
progress_label = tk.Label(frame, text="0%")
progress_label.pack()

# Botón de descarga
download_button = tk.Button(frame, text="Descargar", command=on_download)
download_button.pack(pady=20)

# Actualizar la región visible del canvas cuando el contenido cambie
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Ejecutar la interfaz gráfica
root.mainloop()
