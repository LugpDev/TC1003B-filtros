from lib.aplicar_mascara import aplicar_mascara


def aplicar_bordes_horizontal(event, editor):
    mask = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    aplicar_mascara(mask, editor)


def aplicar_bordes_vertical(event, editor):
    mask = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    aplicar_mascara(mask, editor)
