def aplicar_binario(event, editor, binarizado=False):
    pixeles_salida = editor.imagen_procesada.load()

    if binarizado:
        datos = editor.imagen.getdata()
        suma = sum((r + g + b) // 3 for r, g, b in datos)
        umbral = suma / (editor.ancho * editor.alto)
    else:
        umbral = 128

    for x in range(editor.ancho):
        for y in range(editor.alto):
            pixel = editor.pixeles[x, y]

            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            g = (r + g + b) // 3

            if g <= umbral:
                pixeles_salida[x, y] = (0, 0, 0)
            else:
                pixeles_salida[x, y] = (255, 255, 255)

    editor.mostrar_imagen2(editor.imagen_procesada)
