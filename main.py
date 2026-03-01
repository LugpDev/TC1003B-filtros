import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import Tk
from lib.Editor import Editor

from filtros.grises import aplicar_escala_grises
from filtros.binario import aplicar_binario
from filtros.inverso import aplicar_inverso
from filtros.suavizado import suavizado_3x3, suavizado_5x5, suavizado_7x7
from filtros.bordes import aplicar_bordes_horizontal, aplicar_bordes_vertical
from lib.copiar_imagen import copiar_imagen
from lib.guardar_imagen import guardar_imagen


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

ax_btn_inversio = plt.axes([0.26, 0.96, 0.08, 0.04])
btn_inversio = Button(
    ax_btn_inversio, "Inverso", color="lightblue", hovercolor="skyblue"
)
btn_inversio.on_clicked(lambda event: aplicar_inverso(event, editor))

btn_suavizado3x3 = plt.axes([0.34, 0.96, 0.1, 0.04])
btn_suavizado3x3 = Button(
    btn_suavizado3x3, "Suavizado 3x3", color="lightblue", hovercolor="skyblue"
)
btn_suavizado3x3.on_clicked(lambda event: suavizado_3x3(event, editor))

btn_suavizado5x5 = plt.axes([0.44, 0.96, 0.1, 0.04])
btn_suavizado5x5 = Button(
    btn_suavizado5x5, "Suavizado 5x5", color="lightblue", hovercolor="skyblue"
)
btn_suavizado5x5.on_clicked(lambda event: suavizado_5x5(event, editor))

btn_suavizado7x7 = plt.axes([0.54, 0.96, 0.1, 0.04])
btn_suavizado7x7 = Button(
    btn_suavizado7x7, "Suavizado 7x7", color="lightblue", hovercolor="skyblue"
)
btn_suavizado7x7.on_clicked(lambda event: suavizado_7x7(event, editor))

btn_bordes_horizontal = plt.axes([0.64, 0.96, 0.1, 0.04])
btn_bordes_horizontal = Button(
    btn_bordes_horizontal, "Bordes horiz.", color="lightblue", hovercolor="skyblue"
)
btn_bordes_horizontal.on_clicked(lambda event: aplicar_bordes_horizontal(event, editor))

btn_bordes_vertical = plt.axes([0.74, 0.96, 0.1, 0.04])
btn_bordes_vertical = Button(
    btn_bordes_vertical, "Bordes vert.", color="lightblue", hovercolor="skyblue"
)
btn_bordes_vertical.on_clicked(lambda event: aplicar_bordes_vertical(event, editor))

ax_btn_save = plt.axes([0.92, 0.96, 0.08, 0.04])
btn_save = Button(ax_btn_save, "Guardar", color="white", hovercolor="yellow")
btn_save.on_clicked(lambda event: guardar_imagen(event, editor))

ax_btn_copy = plt.axes([0.48, 0.48, 0.04, 0.04])
btn_copy = Button(ax_btn_copy, "<-", color="white", hovercolor="yellow")
btn_copy.on_clicked(lambda event: copiar_imagen(event, editor))

plt.show()
