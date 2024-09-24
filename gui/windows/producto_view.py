import tkinter as tk

class ProductsView:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)

    def display_products(self, data):
        for widget in self.frame.winfo_children():
            widget.destroy()
        for item in data:
            label = tk.Label(self.frame, text=f"ID: {item['ID']}, Nombre: {item['Nombre']}, Puesto: {item['Puesto']}")
            label.pack()

    def get_frame(self):
        return self.frame