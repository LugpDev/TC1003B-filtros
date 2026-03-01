from PIL import Image


def copiar_imagen(event, editor):
    imagen = editor.imagen_procesada.copy()
    editor.imagen = imagen
    editor.pixeles = imagen.load()
    editor.imagen_procesada = Image.new(
        "RGB", (editor.ancho, editor.alto), color="white"
    )
    editor.mostrar_imagen1(editor.imagen)
    editor.mostrar_imagen2(editor.imagen_procesada)
