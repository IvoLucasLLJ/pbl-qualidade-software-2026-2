import pytest

from src.pedido import calcular_total


def test_calcula_total_de_varios_itens():
    # Arrange
    itens = [
        {"preco": 20, "quantidade": 2},
        {"preco": 10, "quantidade": 1},
    ]

    # Act
    total = calcular_total(itens)

    # Assert
    assert total == 50


def test_retorna_zero_quando_lista_esta_vazia():
    # Arrange
    itens = []

    # Act
    total = calcular_total(itens)

    # Assert
    assert total == 0


def test_rejeita_item_com_preco_zero():
    itens = [{"preco": 0, "quantidade": 1}]

    with pytest.raises(ValueError, match="preco"):
        calcular_total(itens)


def test_rejeita_item_com_quantidade_zero():
    itens = [{"preco": 20, "quantidade": 0}]

    with pytest.raises(ValueError, match="quantidade"):
        calcular_total(itens)

def test_taxa_entrega_ate_tres_km():
    # Arrange: preparar os dados
    distancia_km = 2
    total_pedido = 50

    # Act: executar a função
    from src.pedido import calcular_taxa_entrega
    taxa = calcular_taxa_entrega(distancia_km, total_pedido)

    # Assert: verificar o resultado
    assert taxa == 5


def test_taxa_entrega_acima_de_tres_km():
    # Arrange
    distancia_km = 4
    total_pedido = 50

    # Act
    from src.pedido import calcular_taxa_entrega
    taxa = calcular_taxa_entrega(distancia_km, total_pedido)

    # Assert
    assert taxa == 7


def test_entrega_gratuita_pedido_cem_reais():
    # Arrange
    distancia_km = 5
    total_pedido = 100

    # Act
    from src.pedido import calcular_taxa_entrega
    taxa = calcular_taxa_entrega(distancia_km, total_pedido)

    # Assert
    assert taxa == 0
