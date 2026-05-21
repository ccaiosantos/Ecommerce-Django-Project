def formata_preco(val):
    return f'R$ {val:.2f}'.replace('.', ',')


def cart_total_qtd(carrinho):
    return sum([item['quantidade'] for item in carrinho.values()])


def cart_totals(carrinho):
    total = 0
    for item in carrinho.values():
        preco_promo = item.get('preco_quantitativo_promocional', 0)
        preco_normal = item.get('preco_quantitativo', 0)
        total += preco_promo if preco_promo else preco_normal
    return total
