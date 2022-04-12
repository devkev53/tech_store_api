from xmlrpc.client import Boolean
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

STATE_CHOICES = (
    (True, 'Inactive'),
    (False, 'Active'),
)

class BaseModel(models.Model):
    """Model definition for BaseModel."""

    # TODO: Define fields here
    id = models.AutoField(primary_key=True)
    state = models.BooleanField(_('State'), default=True, choices=STATE_CHOICES)
    created_date = models.DateField(_('Created Date'), auto_now=False, auto_now_add=True)
    modified_date = models.DateField(_('Created Date'), auto_now=True, auto_now_add=False)
    inactivation_date = models.DateField(_('Created Date'), auto_now=True, auto_now_add=False)
    # created_by
    # updated_by


    class Meta:
        """Meta definition for BaseModel."""

        abstract = True
        verbose_name = 'BaseModel'
        verbose_name_plural = 'BaseModels'

    # TODO: Define custom methods here

