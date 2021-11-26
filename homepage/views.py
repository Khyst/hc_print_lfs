from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage # 이메일 메시지롤 보내기 위한 장고 기능

from .models import product_bigcoating, product_general_binding, product_print, product_poster, product_paper, product_report, product_etc
from .models import product_bindding, product_binder, product_catalog, product_creature_of_prize, product_drawing
from .models import product_hard, product_index, product_invite, product_memorial, product_post_it
from .models import product_prize, product_report_box, product_spring, product_form_board, product_shoppingbag
from .models import product_envelope, product_namecard, product_sticker, product_nametag, product_exhibit
from .models import product_bindding, product_photo, product_general_binding

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
        }
        
    return render(request, 'base_product.html', context)

def initial_list(request):
    prod_list = [
        "report", "poster", "form_board", "paper", "hard", "drawing", "spring", "binder", "index", "catalog", "invite", "report_box", 
        "prize", "print", "memorial", "postit", "creature_of_prize","shoppingbag","envelope","name_card","sticker"
    ]

    try:
        report = product_list(name="report")
        report.save()
    except:
        pass

    try:
        poster = product_list(name="poster")
        poster.save()
    except:
        pass


    try:
        form_board = product_list(name="form_board")
        form_board.save()
    except:
        pass

    try:
        paper = product_list(name="paper")
        paper.save()
    except:
        pass

    try:
        hard = product_list(name="hard")
        hard.save()
    except:
        pass

    try:
        drawing = product_list(name="drawing")
        drawing.save()
    except:
        pass

    try:
        spring = product_list(name="spring")
        spring.save()
    except:
        pass

    try:
        binder = product_list(name="binder")
        binder.save()
    except:
        pass

    try:
        index = product_list(name="index")
        index.save()
    except:
        pass

    try:
        catalog = product_list(name="catalog")
        catalog.save()
    except:
        pass

    try:
        invite = product_list(name="invite")
        invite.save()
    except:
        pass

    try:
        report_box = product_list(name="report_box")
        report_box.save()
    except:
        pass

    try:
        print = product_list(name="print")
        print.save()
    except:
        pass

    try:
        memorial = product_list(name="memorial")
        memorial.save()
    except:
        pass

    try:
        postit = product_list(name="postit")
        postit.save()
    except:
        pass

    try:
        prize = product_list(name="prize")
        prize.save()
    except:
        pass

    # 상패, 쇼핑백, 봉투, 명함, 스티커 제품 추가
    try:
        creature_of_prize = product_list(name="creature_of_prize")
        creature_of_prize.save()   
    except:
        pass
    try:
        shoppingbag = product_list(name="shoppingbag")
        shoppingbag.save()
    except:
        pass
    try:
        envelope = product_list(name="envelope")
        envelope.save()
    except:
        pass
    try:
        namecard = product_list(name="namecard")
        namecard.save()
    except:
        pass
    try:
        sticker = product_list(name="sticker")
        sticker.save()
    except:
        pass
    # 2021-11-14 ( 전시회 백월 포스터, 명찰, 대형 코팅 제품 추가 )
    try:
        exhibit = product_list(name="exhibit")
        exhibit.save()
    except:
        pass
    try:
        nametag = product_list(name="nametag")
        nametag.save()
    except:
        pass
    try:
        bigcoating = product_list(name="bigcoating")
        bigcoating.save()
    except:
        pass
    # 2021-11-21 상업용 사진, 교본 추가
    try:
        photo = product_list(name="photo")
        photo.save()
    except:
        pass
    try:
        general_binding = product_list(name="general_binding")
        general_binding.save()
    except:
        redirect('product')

    redirect('product')

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
    }

    connectUrl = 'product_detail/product_' + product_name + '.html'
    return render(request, connectUrl, context)