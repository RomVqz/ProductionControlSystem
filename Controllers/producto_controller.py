from models.producto_model import ProductsModel
from gui.windows.producto_view import ProductsView

class ProductoController:
    def __init__(self, root):
        self.model = ProductsModel()
        self.view = ProductsView(root)

    def show_products(self):
        data = self.model.get_products()
        self.view.display_products(data)

    def get_view(self):
        return self.view.get_frame()
