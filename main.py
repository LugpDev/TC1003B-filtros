import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import Tk
from lib.Editor import Editor
from PIL import Image

from filtros.grises import aplicar_escala_grises
from filtros.binario import aplicar_binario


def copiar_imagen(event, editor):
    global imagen
    global imagen_procesada
    global pixeles
    imagen = imagen_procesada.copy()
    pixeles = imagen.load()
    imagen_procesada = Image.new("RGB", (ancho, alto), color="white")
    editor.mostrar_imagen1(imagen)
    editor.mostrar_imagen2(imagen_procesada)


def aplicar_filtro3x3(event):
    mask = [[-1, 1, 1], [-1, -2, 1], [-1, 1, 1]]
    aplicar_mascara(mask)


def aplicar_mascara(mask):
    global imagen_procesada
    pixeles_salida = imagen_procesada.load()

    for x in range(ancho):
        for y in range(alto):
            n = r = g = b = 0
            radio = len(mask) // 2
            for dx in range(-radio, radio + 1):
                for dy in range(-radio, radio + 1):
                    if 0 <= x + dx < ancho and 0 <= y + dy < alto:
                        pixel = pixeles[x + dx, y + dy]
                        peso = mask[dx + radio][dy + radio]
                        r += pixel[0] * peso
                        g += pixel[1] * peso
                        b += pixel[2] * peso
                        n += peso
            if n == 0:
                n = 1
            r, g, b = r // n, g // n, b // n
            pixeles_salida[x, y] = (r, g, b)
    editor.mostrar_imagen2(imagen_procesada)


def aplicar_suavizado(event):
    global imagen_procesada
    pixeles_salida = imagen_procesada.load()

    for x in range(ancho):
        for y in range(alto):
            n = r = g = b = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if 0 <= x + dx < ancho and 0 <= y + dy < alto:
                        pixel = pixeles[x + dx, y + dy]
                        r += pixel[0]
                        g += pixel[1]
                        b += pixel[2]
                        n += 1
            r, g, b = r // n, g // n, b // n
            pixeles_salida[x, y] = (r, g, b)
    editor.mostrar_imagen2(imagen_procesada)


def guardar_imagen(event):
    Tk().withdraw()
    nombre_archivo = asksaveasfilename(
        title="Guardar imagen procesada",
        defaultextension=".png",
        filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("BMP", "*.bmp")],
    )
    if nombre_archivo:
        imagen_procesada.save(nombre_archivo)
    else:
        print("Guardado cancelado")


Tk().withdraw()
archivo = askopenfilename(filetypes=[("Imágenes", "*.jpg *.png *.avif")])
if not archivo:
    exit()


editor = Editor(archivo)
editor.mostrar_imagen1(editor.imagen)
editor.mostrar_imagen2(editor.imagen_procesada)


plt.subplots_adjust(wspace=0.2)

ax_btn_grises = plt.axes([0.0, 0.96, 0.08, 0.04])
btn_grises = Button(ax_btn_grises, "Grises", color="lightblue", hovercolor="skyblue")
btn_grises.on_clicked(lambda event: aplicar_escala_grises(event, editor))

ax_btn_binario_fijo = plt.axes([0.08, 0.96, 0.08, 0.04])
btn_binario_fijo = Button(
    ax_btn_binario_fijo, "Binario fijo", color="lightblue", hovercolor="skyblue"
)
btn_binario_fijo.on_clicked(lambda event: aplicar_binario(event, editor))

ax_btn_binario_dinamico = plt.axes([0.16, 0.96, 0.1, 0.04])
btn_binario_dinamico = Button(
    ax_btn_binario_dinamico, "Binario dinámico", color="lightblue", hovercolor="skyblue"
)
btn_binario_dinamico.on_clicked(
    lambda event: aplicar_binario(event, editor, binarizado=True)
)

ax_btn_save = plt.axes([0.92, 0.96, 0.08, 0.04])
btn_save = Button(ax_btn_save, "Guardar", color="white", hovercolor="yellow")
btn_save.on_clicked(guardar_imagen)

ax_btn_copy = plt.axes([0.48, 0.48, 0.04, 0.04])
btn_copy = Button(ax_btn_copy, "<-", color="white", hovercolor="yellow")
btn_copy.on_clicked(copiar_imagen)

plt.show()
