from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import Tk

archivo = "test.avif"
Tk().withdraw()
archivo = askopenfilename(filetypes=[("Imágenes", "*.jpg *.png *.avif")])
if not archivo:
    exit()

imagen = Image.open(archivo)
ancho, alto = imagen.size
print("Imagen de ", ancho, "x", alto)
pixeles = imagen.load()

imagen_procesada = Image.new("RGB", (ancho, alto), color="white")


def actualizar_visualizacion(titulo):
    ax1.clear()
    ax1.imshow(imagen)
    ax1.set_title(f"Original: {titulo}")
    ax2.clear()
    ax2.imshow(imagen_procesada)
    ax2.set_title(f"Procesada: {titulo}")
    fig.canvas.draw_idle()


def copiar_imagen(event):
    global imagen
    global imagen_procesada
    global pixeles
    imagen = imagen_procesada.copy()
    pixeles = imagen.load()
    imagen_procesada = Image.new("RGB", (ancho, alto), color="white")
    actualizar_visualizacion("Copia realizada")


def aplicar_escala_grises(event):
    global imagen_procesada
    pixeles_salida = imagen_procesada.load()

    for x in range(ancho):
        for y in range(alto):
            pixel = pixeles[x, y]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            g = (r + g + b) // 3
            pixeles_salida[x, y] = (g, g, g)
    actualizar_visualizacion("Escala de Grises")


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
    actualizar_visualizacion("Filtro aplicado")


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
    actualizar_visualizacion("Suavizado")


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


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

ax1.imshow(imagen)
ax1.set_title("Imagen original")

ax2.imshow(imagen_procesada)
ax2.set_title("Imagen en niveles de gris")

plt.tight_layout()

plt.subplots_adjust(wspace=0.2)

ax_btn_grises = plt.axes([0.0, 0.96, 0.08, 0.04])
btn_grises = Button(ax_btn_grises, "Grises", color="lightblue", hovercolor="skyblue")
btn_grises.on_clicked(aplicar_escala_grises)

ax_btn_suavizado = plt.axes([0.08, 0.96, 0.08, 0.04])
btn_suavizado = Button(
    ax_btn_suavizado, "Suavizado", color="lightblue", hovercolor="skyblue"
)
btn_suavizado.on_clicked(aplicar_suavizado)

ax_btn_filtro = plt.axes([0.16, 0.96, 0.08, 0.04])
btn_filtro = Button(ax_btn_filtro, "Filtro3x3", color="lightblue", hovercolor="skyblue")
btn_filtro.on_clicked(aplicar_filtro3x3)

ax_btn_save = plt.axes([0.92, 0.96, 0.08, 0.04])
btn_save = Button(ax_btn_save, "Guardar", color="white", hovercolor="yellow")
btn_save.on_clicked(guardar_imagen)

ax_btn_copy = plt.axes([0.48, 0.48, 0.04, 0.04])
btn_copy = Button(ax_btn_copy, "<-", color="white", hovercolor="yellow")
btn_copy.on_clicked(copiar_imagen)

plt.show()
