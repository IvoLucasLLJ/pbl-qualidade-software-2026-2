import pytest

from src.regras_localeats import pedido_atingiu_valor_minimo


# TU01 — Responsável: Ivo Lucas de Lima Júnior
def test_tu01_pedido_no_valor_minimo():
    resultado = pedido_atingiu_valor_minimo(30)

    assert resultado is True


# TU02 — Responsável: Ivo Lucas de Lima Júnior
def test_tu02_pedido_abaixo_do_valor_minimo():
    resultado = pedido_atingiu_valor_minimo(29.99)

    assert resultado is False


# TU03 — Responsável: Ivo Lucas de Lima Júnior
def test_tu03_pedido_com_valor_negativo():
    with pytest.raises(ValueError):
        pedido_atingiu_valor_minimo(-1)
