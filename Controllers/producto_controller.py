# controllers/producto_controller.py

from models.producto_model import ProductsModel
from gui.windows.producto_view import ProductsView

class ProductoController:
    def __init__(self, root):
        """
        Inicializa el controlador de productos, con su modelo y vista correspondiente.
        """
        self.model = ProductsModel()
        self.view = ProductsView(root)

    def show_products(self):
        """
        Obtiene los productos del modelo y los muestra en la vista.
        """
        data = self.model.get_products()
        self.view.display_products(data)

    def get_view(self):
        """
        Retorna la vista del controlador.
        """
        return self.view.get_frame()
