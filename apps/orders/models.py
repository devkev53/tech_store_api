from django.db import models
from apps.core.models import BaseModel
from apps.products.models import Product
from apps.profiles.models import User
from simple_history.models import HistoricalRecords
from django.core.exceptions import ValidationError



# Create your models here.

class Order(BaseModel):
    """Model definition for Order."""

    # TODO: Define fields here
    profile = models.ForeignKey(
            User, on_delete=models.CASCADE, related_name='user',
            blank=True, null=True
        )
    order_status = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    total = models.DecimalField(
            max_digits=10, decimal_places=2, blank=True, null=True,
            default=0.00, editable=False
        )
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        """Meta definition for Order."""

        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        """Unicode representation of Order."""
        return '%s %s' % (self.profile, self.created_date)

    def get_total(self):
        total = 0.00
        try:
            for detail in OrderDetail.objects.filter(order=self):
                total += float(detail.subtotal)
            self.total = total
        except(ValueError):
            total = 0.00
            self.total = total
        return total        
    
    def save(self, *args, **kwargs):
        self.total = self.get_total()
        super(Order, self).save(*args, **kwargs)

    # TODO: Define custom methods here

class OrderDetail(BaseModel):
    """Model definition for OrderDetail."""

    # TODO: Define fields here
    product = models.ForeignKey(
            Product, on_delete=models.CASCADE, related_name='product',
            blank=True, null=True
        )
    quantity = models.IntegerField(blank=True, null=True, default=1)
    subtotal = models.DecimalField(
            max_digits=10, decimal_places=2, blank=True, null=True,
            default=0.00, editable=False
        )
    order = models.ForeignKey(
            Order, on_delete=models.CASCADE, verbose_name='Order',
            related_name='order_detail', blank=True, null=True
        )
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        """Meta definition for OrderDetail."""

        verbose_name = 'OrderDetail'
        verbose_name_plural = 'OrderDetails'

    def __str__(self):
        """Unicode representation of OrderDetail."""
        return self.product.name
    
    def clean(self):
        print(self.validate_stock())
        return super().clean()
    
    def save(self, *args, **kwargs):
        self.subtotal = float(float(self.product.price) * self.quantity)
        super(OrderDetail, self).save(*args, **kwargs)
    
    # TODO: Define custom methods here

    def unit_price(self):
        return self.product.price
    
    def validate_stock(self):
        if self.product.stock >= self.quantity:
            print('stock es meno que cantidad - stock: ' + str(self.product.stock) + ' - cantidad: ' + str(self.quantity))
            product = Product.objects.filter(id=self.product.id).first()
            product.stock -= self.quantity
            product.save()
        else:
            raise ValidationError('Stock is not enough')

