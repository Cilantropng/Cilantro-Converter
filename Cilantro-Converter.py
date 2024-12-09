from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import os

# Función para cargar la imagen desde un archivo local
def load_image_from_file(file_path):
    try:
        img = Image.open(file_path)  # Abre la imagen desde el archivo local
        return ImageTk.PhotoImage(img)  # Convierte la imagen a un formato compatible con Tkinter
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")
        return None

# Crear la ventana principal
root = tk.Tk()
root.title("Descargador de YouTube")

# Ruta local de la imagen (ajusta según la ubicación real)
logo_path = 'imagen(es de kanaria la foto)/dec.jpg'  # Ruta relativa de la imagen

# Verificar si la imagen existe en la ruta especificada
if os.path.exists(logo_path):
    # Cargar la imagen local
    logo_image = load_image_from_file(logo_path)

    if logo_image:
        # Mostrar la imagen en la interfaz gráfica
        logo_label = tk.Label(root, image=logo_image)
        logo_label.pack(pady=10)
else:
    messagebox.showerror("Error", f"La imagen no se encuentra en la ruta: {logo_path}")

# Etiquetas y campos de entrada
tk.Label(root, text="Ruta de la carpeta bin de FFmpeg:").pack(pady=5)
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

# Botón de descarga
download_button = tk.Button(root, text="Descargar", command=lambda: print("Descargar"))
download_button.pack(pady=20)

# Ejecutar la interfaz gráfica
root.mainloop()
