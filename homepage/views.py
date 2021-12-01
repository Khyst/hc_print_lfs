from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage # 이메일 메시지롤 보내기 위한 장고 기능

from .models import product_bigcoating, product_calendar, product_diary, product_general_binding, product_hospital, product_print, product_poster, product_paper, product_report, product_etc
from .models import product_bindding, product_binder, product_catalog, product_creature_of_prize, product_drawing
from .models import product_hard, product_index, product_invite, product_memorial, product_post_it
from .models import product_prize, product_report_box, product_spring, product_form_board, product_shoppingbag
from .models import product_envelope, product_namecard, product_sticker, product_nametag, product_exhibit
from .models import product_bindding, product_photo, product_general_binding, product_bici, product_hospital
from .models import product_printout, product_album, product_profile, product_rock, product_wedding, product_calendar, product_diary
from .models import product_list

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
    "namecard", "sticker", "exhibit", "photo", "big_coating", "bici", "printout", "album", "hospital", "profile", "rock", "wedding"
    ,"calendar", "diary"]

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

def product(request):
    context = {
        "product_print": product_print.objects.all(),
        "product_poster": product_poster.objects.all(),
        "product_paper": product_paper.objects.all(), 
        "product_report": product_report.objects.all(),
        "product_etc": product_etc.objects.all(), 
        "product_bindding": product_bindding.objects.all(), 
        "product_binder": product_binder.objects.all(), 
        "product_catalog": product_catalog.objects.all(), 
        "product_creature_of_prize": product_creature_of_prize.objects.all(), 
        "product_drawing": product_drawing.objects.all(), 
        "product_hard": product_hard.objects.all(), 
        "product_index": product_index.objects.all(), 
        "product_invite": product_invite.objects.all(),
        "product_memorial": product_memorial.objects.all(), 
        "product_post_it": product_post_it.objects.all(), 
        "product_prize": product_prize.objects.all(), 
        "product_report_box": product_report_box.objects.all(), 
        "product_spring": product_spring.objects.all(), 
        "product_form_board": product_form_board.objects.all(),
        "product_shoppingbag": product_shoppingbag.objects.all(), 
        "product_envelope": product_envelope.objects.all(), 
        "product_namecard": product_namecard.objects.all(),
        "product_sticker": product_sticker.objects.all(),
        "product_nametag" : product_nametag.objects.all(),
        "product_exhibit" : product_exhibit.objects.all(),
        "product_bigcoating" : product_bigcoating.objects.all(),
        "product_general_binding" : product_general_binding.objects.all(),
        "product_photo" : product_photo.objects.all(),
        "product_hospital": product_hospital.objects.all(),
        "product_bici" : product_bici.objects.all(),
        "product_printout": product_printout.objects.all(),
        "product_album": product_album.objects.all(),
        "product_rock" : product_rock.objects.all(),
        "product_wedding" : product_wedding.objects.all(),
        "product_profile" : product_profile.objects.all(),
        "product_diary" : product_diary.objects.all(),
        "product_calendar" : product_diary.objects.all(),
        }
        
    return render(request, 'base_product.html', context)

def initial(request): #초기화 하는 코드
    BASE = os.path.dirname(os.path.abspath(__file__))
    
    #제안서
    f = open(os.path.join(BASE, "product_urls", "report_url.txt"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        print(line)
        temp_elem = product_report(name=line[:line.find(".")], ext=line[line.find(".")+1:])
        temp_elem.save()

        print(line[:line.find(".")], line[line.find(".")+1:])
    f.close()

    #학회 포스터
    f = open(os.path.join(BASE, "product_urls", "poster_url.txt"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        temp_elem = product_poster(name=line[:line.find(".")], ext=line[line.find(".")+1:])
        temp_elem.save()
    f.close()

    # 폼 보드
    formboard_ext_list = [
        ".jpg", ".jpg", ".jpg", ".jpg"
    ]

    end_formboard_index = len(formboard_ext_list)
    formboard_name_list = [
        "formboard_" + str(i) for i in range(1, end_formboard_index+1)
    ]

    for idx in range(end_formboard_index):
        temp_elem = product_form_board(name=formboard_name_list[idx], ext=formboard_ext_list[idx], id=idx+1)
        temp_elem.save()
        

    # 논문
    f = open(os.path.join(BASE, "product_urls", "paper_url.txt"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        print(line[:line.find(".")], line[line.find(".")+1:])
        temp_elem = product_paper(name=line[:line.find(".")], ext=line[line.find(".")+1:])
        temp_elem.save()
    f.close()

    # 하드 커버 바인딩
    f = open(os.path.join(BASE, "product_urls", "hard_url.txt"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        temp_elem = product_hard(name=line[:line.find(".")], ext=line[line.find(".")+1:])
        temp_elem.save()  
    f.close()

    # 도면 바인딩
    f = open(os.path.join(BASE, "product_urls", "drawing_url.txt"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        temp_elem = product_drawing(name=line[:line.find(".")], ext=line[line.find(".")+1:])
        temp_elem.save()    
    f.close()

    # 스프링 바인딩
    f = open(os.path.join(BASE, "product_urls", "spring_url.txt"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        temp_elem = product_spring(name=line[:line.find(".")], ext=line[line.find(".")+1:])
        temp_elem.save()   
    f.close()

    # 바인더
    f = open(os.path.join(BASE, "product_urls", "binder_url.txt"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        temp_elem = product_binder(name=line[:line.find(".")], ext=line[line.find(".")+1:])
        temp_elem.save()
    f.close()

    # 인덱스 색인
    f = open(os.path.join(BASE, "product_urls", "index_url.txt"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        temp_elem = product_index(name=line[:line.find(".")], ext=line[line.find(".")+1:])
        temp_elem.save()
    f.close()

    # 카탈로그
    f = open(os.path.join(BASE, "product_urls", "catalog_url.txt"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        temp_elem = product_catalog(name=line[:line.find(".")], ext=line[line.find(".")+1:])
        temp_elem.save()
    f.close()

    # 청첩장, 초대장
    f = open(os.path.join(BASE, "product_urls", "invite_url.txt"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        temp_elem = product_invite(name=line[:line.find(".")], ext=line[line.find(".")+1:])
        temp_elem.save()
    f.close()

    # 제안서 박스
    end_report_box_index = 0 #
    report_box_ext_list = [
        ".jpg"
    ]
    report_box_name_list = [
        "report_box_" + str(i) for i in range(1, end_report_box_index+1)
    ]

    for idx in range(end_report_box_index):
        temp_elem = product_report_box(name=report_box_name_list[idx], ext=report_box_ext_list[idx], id=idx+1)
        temp_elem.save()
        
    # 상장, 단증
    f = open(os.path.join(BASE, "product_urls", "prize_url.txt"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        temp_elem = product_prize(name=line[:line.find(".")], ext=line[line.find(".")+1:])
        temp_elem.save()
    f.close()

    # 각종 출력
    f = open(os.path.join(BASE, "product_urls", "print_url.txt"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        temp_elem = product_print(name=line[:line.find(".")], ext=line[line.find(".")+1:])
        temp_elem.save()
    f.close()

    # 기념품
    f = open(os.path.join(BASE, "product_urls", "memorial_url.txt"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        temp_elem = product_memorial(name=line[:line.find(".")], ext=line[line.find(".")+1:])
        temp_elem.save()
    f.close()

    # 포스트 잇
    f = open(os.path.join(BASE, "product_urls", "postit_url.txt"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        temp_elem = product_post_it(name=line[:line.find(".")], ext=line[line.find(".")+1:])
        temp_elem.save()
    f.close()

    # 쇼핑백
    f = open(os.path.join(BASE, "product_urls", "shoppingbag_url.txt"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        temp_elem = product_shoppingbag(name=line[:line.find(".")], ext=line[line.find(".")+1:])
        temp_elem.save()
    f.close()

    # 봉투
    f = open(os.path.join(BASE, "product_urls", "envelope_url.txt"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        temp_elem = product_envelope(name=line[:line.find(".")], ext=line[line.find(".")+1:])
        temp_elem.save()
    f.close()

    # 명함
    f = open(os.path.join(BASE, "product_urls", "namecard_url.txt"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        temp_elem = product_namecard(name=line[:line.find(".")], ext=line[line.find(".")+1:])
        temp_elem.save()
    f.close()

    # 스티커
    f = open(os.path.join(BASE, "product_urls", "sticker_url.txt"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        temp_elem = product_sticker(name=line[:line.find(".")], ext=line[line.find(".")+1:])
        temp_elem.save()
    f.close()

    # 전시회
    f = open(os.path.join(BASE, "product_urls", "exhibit_url.txt"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        temp_elem = product_exhibit(name=line[:line.find(".")], ext=line[line.find(".")+1:])
        temp_elem.save()
    f.close()

    # 대형코팅
    f = open(os.path.join(BASE, "product_urls", "bigcoating_url.txt"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        temp_elem = product_bigcoating(name=line[:line.find(".")], ext=line[line.find(".")+1:])
        temp_elem.save()
    f.close()

    # 교본 및 일반 제본
    f = open(os.path.join(BASE, "product_urls", "general_url.txt"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        temp_elem = product_general_binding(name=line[:line.find(".")], ext=line[line.find(".")+1:])
        temp_elem.save()
    f.close()

    # 석부석 작품
    f = open(os.path.join(BASE, "product_urls", "rock_url.txt"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        temp_elem = product_rock(name=line[:line.find(".")], ext=line[line.find(".")+1:])
        temp_elem.save()
    f.close()

    # 웨딩 사진 출력
    f = open(os.path.join(BASE, "product_urls", "wedding_url.txt"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        temp_elem = product_wedding(name=line[:line.find(".")], ext=line[line.find(".")+1:])
        temp_elem.save()
    f.close()

    # 혜천문화사 프로필
    f = open(os.path.join(BASE, "product_urls", "profile_url.txt"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        temp_elem = product_profile(name=line[:line.find(".")], ext=line[line.find(".")+1:])
        temp_elem.save()
    f.close()

    # 다이어리
    f = open(os.path.join(BASE, "product_urls", "diary_url.txt"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        temp_elem = product_diary(name=line[:line.find(".")], ext=line[line.find(".")+1:])
        temp_elem.save()
    f.close()

    # 달력
    f = open(os.path.join(BASE, "product_urls", "calendar_url.txt"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        temp_elem = product_calendar(name=line[:line.find(".")], ext=line[line.find(".")+1:])
        temp_elem.save()
    f.close()

    return redirect('product')

def delete_init(request):
    product_print.objects.all().delete()
    product_poster.objects.all().delete()
    product_paper.objects.all().delete()
    product_report.objects.all().delete()
    product_etc.objects.all().delete()
    product_bindding.objects.all().delete()
    product_binder.objects.all().delete()
    product_catalog.objects.all().delete()
    product_creature_of_prize.objects.all().delete()
    product_drawing.objects.all().delete()
    product_hard.objects.all().delete()
    product_index.objects.all().delete()
    product_invite.objects.all().delete()
    product_memorial.objects.all().delete()
    product_post_it.objects.all().delete()
    product_prize.objects.all().delete()
    product_report_box.objects.all().delete()
    product_spring.objects.all().delete()
    product_form_board.objects.all().delete()
    product_shoppingbag.objects.all().delete() 
    product_envelope.objects.all().delete() 
    product_namecard.objects.all().delete() 
    product_sticker.objects.all().delete()
    product_exhibit.objects.all().delete()
    product_bigcoating.objects.all().delete()
    product_nametag.objects.all().delete()
    product_general_binding.objects.all().delete()
    product_photo.objects.all().delete()
    product_bici.objects.all().delete()
    product_hospital.objects.all().delete()
    product_printout.objects.all().delete()
    product_album.objects.all().delete()
    product_wedding.objects.all().delete()
    product_profile.objects.all().delete()
    product_rock.objects.all().delete()
    product_diary.objects.all().delete()
    product_calendar.objects.all().delete()
    
    return redirect('product')

def product_view(request, product_name):
    context = {
        "product_print": product_print.objects.all(),
        "product_poster": product_poster.objects.all(),
        "product_paper": product_paper.objects.all(), 
        "product_report": product_report.objects.all(),
        "product_etc": product_etc.objects.all(), 
        "product_bindding": product_bindding.objects.all(), 
        "product_binder": product_binder.objects.all(), 
        "product_catalog": product_catalog.objects.all(), 
        "product_creature_of_prize": product_creature_of_prize.objects.all(), 
        "product_drawing": product_drawing.objects.all(), 
        "product_hard": product_hard.objects.all(), 
        "product_index": product_index.objects.all(), 
        "product_invite": product_invite.objects.all(),
        "product_memorial": product_memorial.objects.all(), 
        "product_post_it": product_post_it.objects.all(), 
        "product_prize": product_prize.objects.all(), 
        "product_report_box": product_report_box.objects.all(), 
        "product_spring": product_spring.objects.all(), 
        "product_form_board": product_form_board.objects.all(),
        "product_shoppingbag": product_shoppingbag.objects.all(), 
        "product_envelope": product_envelope.objects.all(), 
        "product_namecard": product_namecard.objects.all(),
        "product_sticker": product_sticker.objects.all(),
        "product_nametag" : product_nametag.objects.all(),
        "product_exhibit" : product_exhibit.objects.all(),
        "product_bigcoating" : product_bigcoating.objects.all(),
        "product_general_binding" : product_general_binding.objects.all(),
        "product_hospital": product_hospital.objects.all(),
        "product_bici" : product_bici.objects.all(),
        "product_printout": product_printout.objects.all(),
        "product_album": product_album.objects.all(),
        "product_rock": product_rock.objects.all(),
        "product_profile": product_profile.objects.all(),
        "product_wedding": product_wedding.objects.all(),
        "product_diary" : product_diary.objects.all(),
        "product_calendar" : product_calendar.objects.all(),
    }
    
    connectUrl = 'product_detail/product_' + product_name + '.html'
    
    return render(request, connectUrl, context)