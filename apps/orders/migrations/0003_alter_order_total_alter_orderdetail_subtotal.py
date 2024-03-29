# Generated by Django 4.0.4 on 2022-04-18 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_detail_orderdetail_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, editable=False, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='subtotal',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, editable=False, max_digits=10, null=True),
        ),
    ]
