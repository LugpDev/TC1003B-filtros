import matplotlib.pyplot as plt


class Editor:
    def __init__(self):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        self.fig = fig
        self.ax1 = ax1
        self.ax2 = ax2

    def mostrar_imagen1(self, imagen):
        self.ax1.imshow(imagen)
        self.ax1.set_title("Imagen Original")

    def mostrar_imagen2(self, imagen):
        self.ax2.imshow(imagen)
        self.ax2.set_title("Imagen Procesada")
