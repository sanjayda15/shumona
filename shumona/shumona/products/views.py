from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from django.http import Http404
from .models import Product,ProductManager
# Create your views here.

class ProductListView(ListView):
    queryset = Product.objects.all().order_by('-id')
    template_name = 'products/productlist.html'

    def get_queryset(self,*args,**kwargs):
        request=self.request
        return Product.objects.all().order_by('-id')


class MenListView(ListView):
    queryset= Product.objects.men().order_by('-id')
    template_name = 'products/menlist.html'

    def get_queryset(self,*args,**kwargs):
        request=self.request
        return Product.objects.men().order_by('-id')

class WomenListView(ListView):
    queryset = Product.objects.women().order_by('-id')
    template_name = 'products/womenlist.html'

    def get_queryset(self,*args,**kwargs):
        request=self.request
        return Product.objects.women().order_by('-id')


class KidsListView(ListView):
    queryset = Product.objects.kids().order_by('-id')
    template_name = 'products/kidslist.html'

    def get_queryset(self,*args,**kwargs):
        request=self.request
        return Product.objects.kids().order_by('-id')

# class ProductDetail(DetailView):
class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_object(self,*args,**kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        try:
            instance = Product.objects.get(slug=slug,active=True)
        except Product.DoesNotExist:
            raise Http404('Sorry Not found....')
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug,active=True)
            instance = qs.first()
        except err:
            raise Http404('check it{err}')
        return instance
