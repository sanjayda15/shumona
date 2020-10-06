from django.contrib import admin

from .models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display= ('name','email','contact_number')
    search_fields =('name','email','contact_number')


admin.site.register(Contact,ContactAdmin)
