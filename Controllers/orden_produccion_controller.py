from gui.windows.orden_produccion_view import Production_orderView
from models.orden_produccion_model import Production_orderModel


class Production_orderController:
    def __init__(self, root):
        self.model = Production_orderModel()
        self.view = Production_orderView(root)

        # Crear barra de búsqueda y botones en la vista
        self.view.create_search_bar(root, self.search_orders)

    def show_production_order(self):
        data = self.model.get_production_orders()
        self.view.display_production_order(data)

    # Función para manejar la búsqueda
    def search_orders(self):
        query, column = self.view.get_search_query()
        if column and query:
            # Filtrar las órdenes según la columna seleccionada
            filtered_data = [order for order in self.model.get_production_orders() if query.lower() in str(order[column]).lower()]
            self.view.display_production_order(filtered_data)
        else:
            # Si no hay búsqueda o filtro, mostrar todos los datos
            self.show_production_order()

    def get_view(self):
        return self.view.get_frame()
