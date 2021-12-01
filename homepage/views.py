from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage # 이메일 메시지롤 보내기 위한 장고 기능
from .models import product_list
from .models import product
# from .models import product_list
import os.path
# from django.views import views

def blog_to_home(request):
    return redirect('home')
    
def home(request):
    return render(request, 'home/homepage_1.html')

def notice(request):
    return render(request, 'home/notice.html')

def index(request):
    return render(request, 'home/index.html')

def introduce(request):
    return render(request, 'home/introduce.html')

def customer(request):
    return render(request, 'home/customer.html')

def initial_list(request):
    product_li = ["report", "poster", "formboard", "paper", "hard", 
    "spring", "binder", "catalog", "print", "invite", "creature_of_prize", "memorial", "postit", "shoppingbag", "envelope",
    "namecard", "sticker", "exhibit", "photo", "bigcoating", "bici", "printout", "album", "hospital", "profile", "rock", "wedding"
    ,"calendar", "diary", "prize", "index", "drawing", "general_binding"]

    for product in product_li:
        try:
            product_list(list_name=product).save()
        except:
            pass

def transfer_to_email(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        tel = request.POST['tel']

        email = EmailMessage(
            subject,
            "이름(" + name + ")" + " 이메일(" + email + ") 전화번호(" + tel + ")" + "이 보낸 메시지: " + message,
            email,
            to = ['hccopy@naver.com', 'kyh48752242@gmail.com'], # 서버 전송용 프로토콜
        )

        email.send()
        return redirect('')

def product_page(request):
    context = {
        "product_li" : ["report", "poster", "formboard", "paper", "hard", 
                            "spring", "binder", "catalog", "print", "invite", "creature_of_prize", "memorial", "postit", "shoppingbag", "envelope",
                            "namecard", "sticker", "exhibit", "photo", "bigcoating", "bici", "printout", "album", "hospital", "profile", "rock", "wedding"
                            ,"calendar", "diary", "prize", "index", "drawing", "general_binding"],
                            
        "product_print": product.objects.filter(name="print"),
        "product_poster": product.objects.filter(name="poster"),
        "product_paper": product.objects.filter(name="paper"), 
        "product_report": product.objects.filter(name="report"),
        "product_etc": product.objects.filter(name="etc"), 
        "product_bindding": product.objects.filter(name="bindding"), 
        "product_binder": product.objects.filter(name="binder"), 
        "product_catalog": product.objects.filter(name="catalog"), 
        "product_creature_of_prize": product.objects.filter(name="creature_of_prize"), 
        "product_drawing": product.objects.filter(name="drawing"), 
        "product_hard": product.objects.filter(name="hard"), 
        "product_index": product.objects.filter(name="index"), 
        "product_invite": product.objects.filter(name="invite"),
        "product_memorial": product.objects.filter(name="memorial"), 
        "product_post_it": product.objects.filter(name="post_it"), 
        "product_prize": product.objects.filter(name="prize"), 
        "product_report_box": product.objects.filter(name="report_box"), 
        "product_spring": product.objects.filter(name="spring"), 
        "product_form_board": product.objects.filter(name="form_board"),
        "product_shoppingbag": product.objects.filter(name="shoppingbag"), 
        "product_envelope": product.objects.filter(name="envelope"), 
        "product_namecard": product.objects.filter(name="namecard"),
        "product_sticker": product.objects.filter(name="sticker"),
        "product_nametag" : product.objects.filter(name="nametag"),
        "product_exhibit" : product.objects.filter(name="exhibit"),
        "product_bigcoating" : product.objects.filter(name="bigcoating"),
        "product_general_binding" : product.objects.filter(name="general_binding"),
        "product_photo" : product.objects.filter(name="photo"),
        "product_hospital": product.objects.filter(name="hospital"),
        "product_bici" : product.objects.filter(name="bici"),
        "product_printout": product.objects.filter(name="printout"),
        "product_album": product.objects.filter(name="album"),
        "product_rock" : product.objects.filter(name="rock"),
        "product_wedding" : product.objects.filter(name="wedding"),
        "product_profile" : product.objects.filter(name="profile"),
        "product_diary" : product.objects.filter(name="diary"),
        "product_calendar" : product.objects.filter(name="calendar"),
        }

    return render(request, 'base_product.html', context)

def initial(request): #초기화 하는 코드 -> 제품 으로 통합
    BASE = os.path.dirname(os.path.abspath(__file__))
    initial_list = ["report", "poster", "formboard", "paper", "hard", "drawing", "spring", "binder", "index", "catalog", "invite", "report_box", "prize", "print", "memorial", "postit", "shoppingbag", "envelope", "namecard", "sticker", "exhibit", "bigcoating", "general_binding", "rock", "wedding", "profile", "diary", "calendar"]
    for category_name in initial_list:
        file_path = category_name + "_url.txt"
        f = open(os.path.join(BASE, "product_urls", file_path))
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            print(line)
            print(category_name)
            temp_elem = product(name=line[:line.find(".")], ext=line[line.find(".")+1:], category=product_list.objects.get(list_name=category_name))
            temp_elem.save()
            print(line[:line.find(".")], line[line.find(".")+1:])
        f.close()

def delete_init(request):
    product.objects.filter(name="print").delete()
    product.objects.filter(name="poster").delete()
    product.objects.filter(name="paper").delete()
    product.objects.filter(name="report").delete()
    product.objects.filter(name="etc").delete()
    product.objects.filter(name="bindding").delete()
    product.objects.filter(name="binder").delete()
    product.objects.filter(name="catalog").delete()
    product.objects.filter(name="creature_of_prize").delete()
    product.objects.filter(name="drawing").delete()
    product.objects.filter(name="hard").delete()
    product.objects.filter(name="index").delete()
    product.objects.filter(name="invite").delete()
    product.objects.filter(name="memorial").delete()
    product.objects.filter(name="post_it").delete()
    product.objects.filter(name="prize").delete()
    product.objects.filter(name="report_box").delete()
    product.objects.filter(name="spring").delete()
    product.objects.filter(name="form_board").delete()
    product.objects.filter(name="shoppingbag").delete() 
    product.objects.filter(name="envelope").delete() 
    product.objects.filter(name="namecard").delete() 
    product.objects.filter(name="sticker").delete()
    product.objects.filter(name="exhibit").delete()
    product.objects.filter(name="bigcoating").delete()
    product.objects.filter(name="nametag").delete()
    product.objects.filter(name="general_binding").delete()
    product.objects.filter(name="photo").delete()
    product.objects.filter(name="bici").delete()
    product.objects.filter(name="hospital").delete()
    product.objects.filter(name="printout").delete()
    product.objects.filter(name="album").delete()
    product.objects.filter(name="wedding").delete()
    product.objects.filter(name="profile").delete()
    product.objects.filter(name="rock").delete()
    product.objects.filter(name="diary").delete()
    product.objects.filter(name="calendar").delete()
    
    return redirect('product')

def product_view(request, product_name):

    context = {
        "product_li" : ["report", "poster", "formboard", "paper", "hard", 
                            "spring", "binder", "catalog", "print", "invite", "creature_of_prize", "memorial", "postit", "shoppingbag", "envelope",
                            "namecard", "sticker", "exhibit", "photo", "bigcoating", "bici", "printout", "album", "hospital", "profile", "rock", "wedding"
                            ,"calendar", "diary", "prize", "index", "drawing", "general_binding"],

        "product_print": product.objects.filter(name="print"),
        "product_poster": product.objects.filter(name="poster"),
        "product_paper": product.objects.filter(name="paper"), 
        "product_report": product.objects.filter(name="report"),
        "product_etc": product.objects.filter(name="etc"), 
        "product_bindding": product.objects.filter(name="bindding"), 
        "product_binder": product.objects.filter(name="binder"), 
        "product_catalog": product.objects.filter(name="catalog"), 
        "product_creature_of_prize": product.objects.filter(name="creature_of_prize"), 
        "product_drawing": product.objects.filter(name="drawing"), 
        "product_hard": product.objects.filter(name="hard"), 
        "product_index": product.objects.filter(name="index"), 
        "product_invite": product.objects.filter(name="invite"),
        "product_memorial": product.objects.filter(name="memorial"), 
        "product_post_it": product.objects.filter(name="post_it"), 
        "product_prize": product.objects.filter(name="prize"), 
        "product_report_box": product.objects.filter(name="report_box"), 
        "product_spring": product.objects.filter(name="spring"), 
        "product_form_board": product.objects.filter(name="form_board"),
        "product_shoppingbag": product.objects.filter(name="shoppingbag"), 
        "product_envelope": product.objects.filter(name="envelope"), 
        "product_namecard": product.objects.filter(name="namecard"),
        "product_sticker": product.objects.filter(name="sticker"),
        "product_nametag": product.objects.filter(name="nametag"),
        "product_exhibit": product.objects.filter(name="exhibit"),
        "product_bigcoating": product.objects.filter(name="bigcoating"),
        "product_general_binding": product.objects.filter(name="general_binding"),
        "product_hospital": product.objects.filter(name="hospital"),
        "product_bici": product.objects.filter(name="bici"),
        "product_printout": product.objects.filter(name="printout"),
        "product_album": product.objects.filter(name="album"),
        "product_rock": product.objects.filter(name="rock"),
        "product_profile": product.objects.filter(name="profile"),
        "product_wedding": product.objects.filter(name="wedding"),
        "product_diary": product.objects.filter(name="diary"),
        "product_calendar": product.objects.filter(name="calendar"),
    }
    connectUrl = 'product_detail/product_' + product_name + '.html'
    return render(request, connectUrl, context)