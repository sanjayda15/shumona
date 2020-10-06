from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model   = Contact
        fields  = ('name','email','contact_number','products')
        label   ={'name':'Name','email':'Email Address','contact_number':'Contact Number','products':'Product Id'}
        widgets ={'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Your Name'}),
                  'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Your Email Address'}),
                  'contact_number':forms.TextInput(attrs={'class':'form-control','placeholder':'Your contact number'}),
                  'products':forms.Textarea(attrs={'class':'form-control','placeholder':'products-title'})}
