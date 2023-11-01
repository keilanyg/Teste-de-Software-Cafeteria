class Inventario:
    def __init__(self):
        self.inventario = {
            'cafe': 0,
            'leite': 0,
            'acucar': 0,
            'chocolate': 0
        }

    def adicionar_inventario(self, item, quantidade):
        if item in self.inventario:
            self.inventario[item] += quantidade
        else:
            print("Item inválido.")

    def verificar_inventario(self):
        for item, quantidade in self.inventario.items():
            print(f"{item}: {quantidade} unidades")

