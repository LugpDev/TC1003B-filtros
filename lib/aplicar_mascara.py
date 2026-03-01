def aplicar_mascara(mask, editor):
    pixeles_salida = editor.imagen_procesada.load()

    for x in range(editor.ancho):
        for y in range(editor.alto):
            n = r = g = b = 0
            radio = len(mask) // 2
            for dx in range(-radio, radio + 1):
                for dy in range(-radio, radio + 1):
                    if 0 <= x + dx < editor.ancho and 0 <= y + dy < editor.alto:
                        pixel = editor.pixeles[x + dx, y + dy]
                        peso = mask[dx + radio][dy + radio]
                        r += pixel[0] * peso
                        g += pixel[1] * peso
                        b += pixel[2] * peso
                        n += peso
            if n == 0:
                n = 1
            r, g, b = r // n, g // n, b // n
            pixeles_salida[x, y] = (r, g, b)
    editor.mostrar_imagen2(editor.imagen_procesada)
