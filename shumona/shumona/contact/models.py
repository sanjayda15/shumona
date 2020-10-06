# Create your models here.
from django.db import models
from django.core.validators import RegexValidator

class Contact(models.Model):
    name           = models.CharField(max_length=200)
    email          = models.EmailField(max_length=250)
    phone_regex    = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    products       = models.TextField(max_length=250)

    def __str__(self):
        return f'customer name:-{self.name}'
