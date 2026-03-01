from lib.aplicar_mascara import aplicar_mascara


def suavizado_3x3(event, editor):
    mask = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    aplicar_mascara(mask, editor)
