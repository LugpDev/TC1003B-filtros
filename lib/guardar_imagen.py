from tkinter import Tk
from tkinter.filedialog import asksaveasfilename


def guardar_imagen(event, editor):
    Tk().withdraw()
    nombre_archivo = asksaveasfilename(
        title="Guardar imagen procesada",
        defaultextension=".png",
        filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("BMP", "*.bmp")],
    )
    if nombre_archivo:
        editor.imagen_procesada.save(nombre_archivo)
    else:
        print("Guardado cancelado")
