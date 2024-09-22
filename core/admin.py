from django.contrib import admin
from .models import Email, Items, Categorias, ContactUs, Urls

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


# class UrlsAdmin(admin.ModelAdmin):
#     list_display = ['url']
#     search_fields = ['url']

# admin.site.register(Urls, UrlsAdmin)
# from .models import Urls

class UrlsAdmin(admin.ModelAdmin):
    list_display = ('url', 'created_at', 'updated_at', 'last_scraped', 'scraped', 'product_name', 'product_price')
    search_fields = ('url', 'product_name', 'product_description', 'product_price')
    list_filter = ('scraped', 'created_at', 'last_scraped', 'product_category')
    fieldsets = (
        (None, {
            'fields': ('url', 'scraped', 'last_scraped')
        }),
        ('Product Information', {
            'fields': ('product_name', 'product_description', 'product_price', 'product_image', 'product_category')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

admin.site.register(Urls, UrlsAdmin)