from django.contrib import admin
from .models import Email, ItemSizer, Categorias
# Register your models here.
admin.site.register(Categorias)
admin.site.register(ItemSizer)
admin.site.register(Email)

