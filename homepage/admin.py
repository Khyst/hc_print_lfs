from django.contrib import admin
from .models import product_list
from .models import product
# from .models import product_list

class customAdmin(admin.ModelAdmin):
    list_display = ['name', 'ext', 'title', 'desc', 'src', 'prefix']
    list_display_links = ['name', 'title']
    search_fields = ['title', 'desc', 'name', 'ext']


# Register your models here.
admin.site.register(product, customAdmin),
admin.site.register(product_list),
