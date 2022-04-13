from django.db import models
from apps.core.models import BaseModel
from simple_history.models import HistoricalRecords

# Create your models here.

class ProductImage(models.Model):
    """Model definition for ProductImage."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for ProductImage."""

        verbose_name = 'ProductImage'
        verbose_name_plural = 'ProductImages'

    def __str__(self):
        """Unicode representation of ProductImage."""
        pass

    # TODO: Define custom methods here

class Product(models.Model):
    """Model definition for Product."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Product."""
        pass

    # TODO: Define custom methods here
