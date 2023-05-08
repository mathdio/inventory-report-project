from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "queijo",
        "Queijaria",
        "2023-01-01",
        "2023-02-01",
        "1000",
        "em local resfriado",
    )
    assert product.id == 1
    assert product.nome_do_produto == "queijo"
    assert product.nome_da_empresa == "Queijaria"
    assert product.data_de_fabricacao == "2023-01-01"
    assert product.data_de_validade == "2023-02-01"
    assert product.numero_de_serie == "1000"
    assert product.instrucoes_de_armazenamento == "em local resfriado"
