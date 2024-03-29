# Generated by Django 4.0.4 on 2022-04-18 02:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0007_remove_historicalproductimage_image_upload_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(choices=[(True, 'Active'), (False, 'Inactive')], default=True, verbose_name='State')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Created Date')),
                ('inactivation_date', models.DateField(auto_now=True, verbose_name='Created Date')),
                ('quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('subtotal', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.product')),
            ],
            options={
                'verbose_name': 'OrderDetail',
                'verbose_name_plural': 'OrderDetails',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(choices=[(True, 'Active'), (False, 'Inactive')], default=True, verbose_name='State')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Created Date')),
                ('inactivation_date', models.DateField(auto_now=True, verbose_name='Created Date')),
                ('order_status', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='orders.orderdetail')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
