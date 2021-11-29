from django.contrib import admin
from .models import product_bigcoating, product_exhibit, product_nametag, product_print, product_poster, product_paper, product_report, product_etc, product_bindding, product_binder, product_catalog, product_creature_of_prize, product_drawing, product_hard, product_index, product_invite, product_memorial, product_post_it, product_prize, product_report_box, product_spring, product_form_board, product_shoppingbag, product_envelope, product_namecard, product_sticker, product_album, product_bici, product_general_binding, product_printout, product_hospital, product_list, product_photo, product_profile, product_wedding, product_rock
# from .models import product_list

class customAdmin(admin.ModelAdmin):
    list_display = ['name', 'ext', 'title', 'desc', 'src', 'prefix']
    list_display_links = ['name', 'title']
    search_fields = ['title', 'desc', 'name', 'ext']


# Register your models here.
admin.site.register(product_print, customAdmin),
admin.site.register(product_poster, customAdmin),
admin.site.register(product_paper, customAdmin),
admin.site.register(product_report, customAdmin),
admin.site.register(product_etc, customAdmin),
admin.site.register(product_bindding, customAdmin),
admin.site.register(product_binder, customAdmin),
admin.site.register(product_catalog, customAdmin),
admin.site.register(product_creature_of_prize, customAdmin),
admin.site.register(product_drawing, customAdmin),
admin.site.register(product_hard, customAdmin),
admin.site.register(product_index, customAdmin),
admin.site.register(product_invite, customAdmin),
admin.site.register(product_memorial, customAdmin),
admin.site.register(product_post_it, customAdmin),
admin.site.register(product_prize, customAdmin),
admin.site.register(product_report_box, customAdmin),
admin.site.register(product_spring, customAdmin),
admin.site.register(product_form_board, customAdmin),
admin.site.register(product_shoppingbag), customAdmin, 
admin.site.register(product_envelope), customAdmin, 
admin.site.register(product_namecard), customAdmin, 
admin.site.register(product_sticker, customAdmin),
admin.site.register(product_nametag, customAdmin),
admin.site.register(product_bigcoating, customAdmin),
admin.site.register(product_exhibit, customAdmin),
admin.site.register(product_photo, customAdmin),
admin.site.register(product_album, customAdmin),
admin.site.register(product_bici, customAdmin),
admin.site.register(product_printout, customAdmin),
admin.site.register(product_hospital, customAdmin),
admin.site.register(product_rock, customAdmin),
admin.site.register(product_wedding, customAdmin),
admin.site.register(product_profile, customAdmin),

admin.site.register(product_list),
