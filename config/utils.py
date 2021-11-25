# import os

# from ..homepage.models import product_envelope, product_general_binding, product_photo, product_shoppingbag, product_bigcoating, product_bindding, product_binder, product_catalog, product_creature_of_prize, product_drawing, product_etc, product_exhibit, product_form_board, product_hard, product_index, product_invite, product_list, product_memorial, product_namecard, product_nametag, product_paper, product_post_it, product_poster, product_print, product_prize, product_report, product_report_box, product_spring, product_sticker

# def rename_imagefile_to_uuid(instance, filename):
#     upload_to = f'{instance.prefix}'
#     ext = filename.split('.')[-1]
#     if instance: # 인스턴스가 존재하면
#         last_ord = product_list.objects.get(instance.prefix.split('/')[-2])
#         filename = '{}_{}.{}'.format(instance.prefix.split('/')[-2], last_ord + 1, ext)
#         print(filename)
#         instance.save(name=instance.prefix.split('/')[-2], ext=ext, id=instance.uuid)

#     else:
#         pass

#     return os.path.join(upload_to, filename)