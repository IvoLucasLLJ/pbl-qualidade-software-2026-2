# Responsável: Ivo Lucas de Lima Júnior
def pedido_atingiu_valor_minimo(valor_pedido):
    if valor_pedido < 0:
        raise ValueError("O valor do pedido não pode ser negativo.")
    return valor_pedido >= 30
