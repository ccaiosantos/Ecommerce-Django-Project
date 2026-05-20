from django import template

register = template.Library()


@register.filter(name='formata_preco')
def formata_preco(val):
    return f'R$ {val:.2f}'.replace('.', ',')


@register.filter(name='cart_totals')
def cart_totals(carrinho):
    total = 0

    for key, item in carrinho.items():

        preco_promocional = item.get(
            'preco_quantitativo_promocional'
        )

        preco_normal = item.get(
            'preco_quantitativo'
        )

        if preco_promocional:
            total += preco_promocional
        else:
            total += preco_normal

    return total
