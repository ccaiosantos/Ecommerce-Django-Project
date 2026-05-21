from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='qtd_total',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pedido',
            name='data',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterModelOptions(
            name='pedido',
            options={'ordering': ['-id'], 'verbose_name': 'Pedido', 'verbose_name_plural': 'Pedidos'},
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='pedido',
            field=models.ForeignKey(
                on_delete=models.deletion.CASCADE,
                related_name='itens',
                to='pedido.pedido'
            ),
        ),
    ]
