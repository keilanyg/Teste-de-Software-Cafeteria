from src.cafeteria.maquina import Maquina
from src.cafeteria.inventario import Inventario
from src.cafeteria.receita import Receita

def test_cafe():
    cafe = Maquina()
    inventario = Inventario()
    
    #Receitas
    receita1 = Receita("Café", 4, 4, 3, 2, 2)
    receita2 = Receita("Café", 4, 4, 0, 6, 0)
    receita3 = Receita("Cappuccino", 12, 2, 3, 5, 0)
    receita4 = Receita("Espresso", 9, 6, 2, 5, 3)

    # Adicionar uma receita
    cafe.adicionar_receita(receita1)
    assert len(cafe.receitas) == 1

    # Adicionar uma receita com o nome igual
    cafe.adicionar_receita(receita2)
    assert len(cafe.receitas) == 1

    # Adiciona duas receitas
    cafe.adicionar_receita(receita3)
    cafe.adicionar_receita(receita4)
    assert len(cafe.receitas) == 3

    # Exclui receita
    cafe.excluir_receita("Café")
    assert len(cafe.receitas) == 2

    # Editar uma receita
    cafe.editar_receita("Cappuccino", 3, 9, 5, 6, 0)
    for receita in cafe.receitas:
        if receita.nome == "Cappuccino":
            assert receita.preco == 3
            assert receita.cafe == 9
            assert receita.leite == 5
            assert receita.acucar == 6
            assert receita.chocolate == 0

    # Editar uma receita inexistente
    cafe.editar_receita("Latte", 2, 4, 3, 9, 5)
    for receita in cafe.receitas:
        if receita.nome == "Latte":
            assert receita.preco != 2

def test_inventario():
    inventario = Inventario()

    # Adicionar itens ao inventário
    inventario.adicionar_inventario('cafe', 300)
    inventario.adicionar_inventario('leite', 400)
    inventario.adicionar_inventario('acucar', 600)

    assert inventario.inventario['cafe'] == 300
    assert inventario.inventario['leite'] == 400
    assert inventario.inventario['acucar'] == 600

    # Verificar o inventário
    inventario.verificar_inventario()

