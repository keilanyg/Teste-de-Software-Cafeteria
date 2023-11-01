from src.cafeteria.maquina import Maquina
from src.cafeteria.inventario import Inventario
from src.cafeteria.receita import Receita

cafe = Maquina()
inventario = Inventario()

while True:
        print("\n----- Menu -----")
        print("1. Adicionar Receita")
        print("2. Editar Receita")
        print("3. Excluir Receita")
        print("4. Verificar Receitas")
        print("5. Adicionar Inventário")
        print("6. Verificar Inventário")
        print("7. Sair")

        opc = input("Opção: ")

        if opc == '1':
            nome = input("Nome da receita: ")
            preco = int(input("Preço: "))
            cafe = int(input("Café (unidade): "))
            leite = int(input("Leite (unidade): "))
            acucar = int(input("Açúcar (unidade): "))
            chocolate = int(input("Chocolate (unidade): "))
            receita = Receita(nome, preco, cafe, leite, acucar, chocolate)
            cafe.adicionar_receita(receita)
            print("Receita adicionada!")

    
        elif opc == '2':
            nome = input("Nome da receita a editar: ")
            novo_preco = float(input("Novo preço: "))
            novo_cafe = int(input("Novo café: "))
            novo_leite = int(input("Novo leite: "))
            novo_acucar = int(input("Novo açúcar: "))
            novo_chocolate = int(input("Novo chocolate: "))
            cafe.editar_receita(nome, novo_preco, novo_cafe, novo_leite, novo_acucar, novo_chocolate)
        
        elif opc == '3':
            nome = input("Nome da receita a excluir: ")
            cafe.excluir_receita(nome)
            print("Receita excluída!")
            
        elif opc == '4':
            cafe.verificar_receitas()
        
        elif opc == '5':
            print("\nQuantidades atuais:")
            inventario.verificar_inventario()
            item = input("Nome do item para adicionar no inventário: ")
            quantidade = int(input("Quantidade a adicionar: "))
            inventario.adicionar_inventario(item, quantidade)
        
        elif opc == '6':
            inventario.verificar_inventario()
        
        elif opc == '7':
            print("Saindo.")
            break
        
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
