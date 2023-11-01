class Maquina:
    def __init__(self):
        self.receitas = []

    def adicionar_receita(self, receita):
        if len(self.receitas) < 3:
            for r in self.receitas:
                if r.nome == receita.nome:
                    print(f"Já existe uma receita com o nome {receita.nome}.")
                    return
            self.receitas.append(receita)
        else:
            print("A máquina de café já atingiu o limite máximo de receitas (3).\n")

    def editar_receita(self, nome, novo_preco, novo_cafe, novo_leite, novo_acucar, novo_chocolate):
        for receita in self.receitas:
            if receita.nome == nome:
                receita.preco = novo_preco
                receita.cafe = novo_cafe
                receita.leite = novo_leite
                receita.acucar = novo_acucar
                receita.chocolate = novo_chocolate
                break
    
    def excluir_receita(self, nome):
        for receita in self.receitas:
            if receita.nome == nome:
                self.receitas.remove(receita)
                break

    def verificar_receitas(self):
        print("RECEITA")
        for receita in self.receitas:
            print(f"Nome: {receita.nome}")
            print(f"Preço: {receita.preco}")
            print(f"Café: {receita.cafe}g")
            print(f"Leite: {receita.leite}ml")
            print(f"Açúcar: {receita.acucar}g")
            print(f"Chocolate: {receita.chocolate}g")
            print()


