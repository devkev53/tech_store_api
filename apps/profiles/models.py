from datetime import date
# Django Imports
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext as _
# Simple History
from simple_history.models import HistoricalRecords

# Create your models here.

class Role(models.Model):
    """Model definition for Role."""

    # TODO: Define fields here
    description = models.CharField(_('description'), max_length=100)

    class Meta:
        """Meta definition for Role."""

        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    def __str__(self):
        """Unicode representation of Role."""
        return self.description

    # TODO: Define custom methods here


class UserManager(BaseUserManager):
    ''' Manejador para los objetosy creacion de usuarios '''

    def _create_user(self, email, name, last_name, password, is_staff, is_superuser, **extra_fields):
        ''' Metodo que crea el usuario con los campos de django y campos extras proporcionados'''
        if not email:
            raise ValueError(_('Users must have a email'))
        
        email = self.normalize_email(email)

        user = self.model(
            email=email,
            name=name,
            last_name=last_name,
            password=password,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self, email, name, last_name, password=None, **extra_fields):
        ''' Metodo para creacion de usuarios standar '''
        return self._create_user(email, name, last_name, password, False, False, **extra_fields)

    def create_superuser(self, email, name, last_name, password, **extra_fields):
        ''' Metodo para creacion de usuarios standar '''
        return self._create_user(email, name, last_name, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    ''' Definicion del modelo customizado de usuario '''
    email = models.EmailField(_('Email'), max_length=255, unique=True)
    name = models.CharField(_('Name'), max_length=255, blank=True, null=True)
    last_name = models.CharField(_('Last Name'), max_length=255, blank=True, null=True)
    profile_img = models.ImageField(_('Profile Image'), blank=True, null=True, upload_to='profile/')
    date_to_birth = models.DateField(_('Date to Birth'), blank=True, null=True)
    is_active = models.BooleanField(_('Is Active'), default=True)
    is_staff = models.BooleanField(_('Is Staff'), default=False)
    historical = HistoricalRecords()

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'last_name']

    def get_full_name(self):
        ''' Retorna el nombre completo'''
        return '%s %s' % (self.name, self.last_name)

    def get_short_name(self):
        ''' Retorna el nombre'''
        return self.name
    
    def __str__(self):
        ''' Retorna como se ve el objeto en un query'''
        return self.email
    
    def years_old(self):
        years_old = None
        if self.date_to_birth:
            date_today = date.today()
            date_birth=self.date_to_birth
            years_old = date_today.year - date_birth.year - ((date_today.month, date_today.day) < (date_birth.month, date_birth.day))
        # primero restamos los años y luego restamos la comparación entre mes y día actual y mes y día de nacimiento. 
        return years_old