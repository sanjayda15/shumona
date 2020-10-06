from django.shortcuts import render
from django.views.generic import CreateView
from .forms import ContactForm

# Create your views here.
class ContactView(CreateView):
    form_class  = ContactForm
    success_url = '/thankyou'
    template_name = 'contact.html'
