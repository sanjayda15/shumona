from django.db import models
from shumona.utils import unique_slug_generator
from django.db.models.signals import pre_save,post_save
from django.urls import reverse
# Create your models here.

import random
import os
# Create your models here.
def get_filename_ext(filepath):
    base_file = os.path.basename(filepath)
    name,ext =os.path.splitext(base_file)
    return name,ext

def upload_image_path(instance,filename):
    new_filename = random.randint(1,9999999)
    name,ext =  get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'products/{new_filename}/{final_filename}'

class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def men(self):
        return self.filter(men=True,active=True)

    def women(self):
        return self.filter(women=True,active=True)

    def Kids(self):
        return self.filter(kids=True,active=True)


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model,using=self._db)

    def all(self):
        return self.get_queryset().active()

    def men(self):
        return self.get_queryset().men()

    def women(self):
        return self.get_queryset().women()

    def kids(self):
        return self.get_queryset().Kids()

class Product(models.Model):
    title       = models.CharField(max_length=250)
    slug        = models.SlugField(blank=True,unique=True)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2,max_digits=20,default=800)
    image       = models.ImageField(upload_to=upload_image_path,null=True,blank=True)
    timestamp   = models.DateTimeField(auto_now=True)
    active      = models.BooleanField(default=True)
    sale        = models.BooleanField(default=False)
    men         = models.BooleanField(default=False)
    women       = models.BooleanField(default=False)
    kids        = models.BooleanField(default=False)

    objects = ProductManager()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug':self.slug})



def product_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(product_pre_save_receiver, sender=Product)
