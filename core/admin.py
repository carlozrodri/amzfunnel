from django.contrib import admin
from .models import Email, Items, Categorias, ContactUs

# Register your models here.
admin.site.register(Categorias)
# admin.site.register(Items)
admin.site.register(Email)

class ItemsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created')
    list_filter = ("category",)
    search_fields = ['title', 'content']
    # prepopulated_fields = {'slug': ('title',)}

admin.site.register(Items, ItemsAdmin)


class ContactUs2(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_on')
    

admin.site.register(ContactUs, ContactUs2)
