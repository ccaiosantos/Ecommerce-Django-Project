from django import template

register = template.Library()

@register.filter(name='formata_preco')
def formata_preco(val):
    return f'R$ {val:.2f}'.replace('.', ',')