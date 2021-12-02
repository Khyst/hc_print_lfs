from django.contrib import admin
from .models import product_list
from .models import product
# from .models import product_list

class customAdmin(admin.ModelAdmin):
    list_display = ['displayed_name', 'ext', 'title', 'desc', 'src', 'prefix']
    list_display_links = ['displayed_name', 'title']
    search_fields = ['title', 'desc', 'displayed_name', 'name', 'ext']


# Register your models here.
admin.site.register(product, customAdmin),
admin.site.register(product_list),
