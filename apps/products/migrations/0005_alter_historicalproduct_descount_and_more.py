# Generated by Django 4.0.4 on 2022-04-15 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_historicalproductimage_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproduct',
            name='descount',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Discount Rate'),
        ),
        migrations.AlterField(
            model_name='product',
            name='descount',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Discount Rate'),
        ),
    ]
