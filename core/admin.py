from django.contrib import admin
from .models import Email, ItemSizer, Categorias, ContactUs

# Register your models here.
admin.site.register(Categorias)
admin.site.register(ItemSizer)
admin.site.register(Email)
admin.site.register(ContactUs)


class ContactUs(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_on')
    

