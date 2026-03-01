def aplicar_escala_grises(event, editor):
    pixeles_salida = editor.imagen_procesada.load()

    for x in range(editor.ancho):
        for y in range(editor.alto):
            pixel = editor.pixeles[x, y]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            g = (r + g + b) // 3
            pixeles_salida[x, y] = (g, g, g)
    editor.mostrar_imagen2(editor.imagen_procesada)
