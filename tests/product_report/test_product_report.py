from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "queijo",
        "Queijaria",
        "2023-01-01",
        "2023-02-01",
        "1000",
        "em local resfriado",
    )
    assert product.__repr__() == (
        "O produto queijo fabricado em 2023-01-01 por "
        "Queijaria com validade até 2023-02-01 precisa "
        "ser armazenado em local resfriado."
    )
