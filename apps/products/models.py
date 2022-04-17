from email.mime import image
from django.db import models
from apps.core.models import BaseModel
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError

# Create your models here.

class Category(BaseModel):
    """Model definition for Category."""

    # TODO: Define fields here
    description = models.CharField(_('Description'), max_length=100, unique=True, blank=False, null=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Category."""
        return self.description

    # TODO: Define custom methods here



class Product(BaseModel):
    """Model definition for Product."""

    # TODO: Define fields here
    name = models.CharField(_('Name'), max_length=255, unique=True, blank=False, null=False)
    description = models.TextField(_('description'), blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', blank=True, null=True)
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2, blank=False, null=False)
    stock = models.IntegerField(_('Stock'), default=1, blank=False, null=False)
    descount = models.PositiveSmallIntegerField(_('Discount Rate'), default=0)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name

    # TODO: Define custom methods here

    def get_images(self):
        images = []
        for image in ProductImage.objects.filter(product=self):
            if image.image_upload:
                images.append(image.image_upload.url)
            images.append(image.image_url)
        return images
    
    def is_off(self):
        return self.descount > 0
    
    def total_descount(self):
        descount = (self.price * self.descount) / 100
        return descount

class ProductImage(BaseModel):
    """Model definition for Product Image."""

    # TODO: Define fields here
    image_upload = models.ImageField(_('Product Image Upload'), upload_to='products/images/', blank=True, null=True)
    image_url = models.URLField(_('Product Image URL'), blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image_product', blank=True, null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        """Meta definition for Product Image."""

        verbose_name = 'ProductImage'
        verbose_name_plural = 'Product Images'

        
    def __str__(self):
        """Unicode representation of Product Image."""
        return self.product.name

    # TODO: Define custom methods here

    def clean(self) -> None:
        images = ProductImage.objects.filter(product=self.product)
        if images.count() > 4:
            raise ValidationError(_('You can only upload 5 images'))
        return super().clean()
    
