from django.contrib import admin
from . import models


class ItemPedidoInline(admin.TabularInline):
    model = models.ItemPedido
    extra = 0
    readonly_fields = ('produto', 'produto_id', 'variacao', 'variacao_id',
                       'preco', 'preco_promocional', 'quantidade', 'imagem')


class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'total', 'qtd_total', 'status', 'data')
    list_filter = ('status',)
    search_fields = ('usuario__username', 'usuario__email')
    list_per_page = 20
    inlines = [ItemPedidoInline]
    readonly_fields = ('data',)


admin.site.register(models.Pedido, PedidoAdmin)
admin.site.register(models.ItemPedido)
