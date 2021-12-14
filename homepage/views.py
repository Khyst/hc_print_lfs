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

product_li = dict()
step = 0
for elem in product_list.objects.all():
    product_li[step] = elem.list_name
    step = step + 1

dict_product = {
    "hospital" : "각종 병원 양식",
    "album" : "앨범",
    "printout" : "각종 인쇄",
    "bici" : "BI & CI 간판 디자인",
    "bigcoating" : "대형 코팅",
    "photo" : "상업용 사진",
    "exhibit" : "전시회 백월 포스터",
    "sticker" : "스티커",
    "namecard" : "명함",
    "envelope" : "봉투",
    "shoppingbag" : "쇼핑백",
    "postit" : "포스트잇",
    "memorial" : "기념품",
    "creature_of_prize" : "상패 디자인",
    "invite" : "청첩장 & 초대장",
    "prize" : "상장 & 단증",
    "print" : "각종 출력",
    "catalog" : "카탈로그",
    "binder" : "바인더",
    "spring" : "스프링",
    "hard" : "하드커버제본",
    "spring" : "스프링제본",
    "formboard" : "폼보드",
    "report" : "보고서 & 제안서",
    "poster" : "포스터 & 학회포스터",
    "paper" : "논문",
    "rock" : "석부작 작품",
    "wedding" : "웨딩사진 출력",
    "profile" : "혜천문화사 프로필",
    "diary" : "다이어리",
    "calendar" : "달력", 
    "general_binding" : "일반 제본 및 교본",
    "index" : "인덱스",
    "drawing" : "도면 제본",
    "big_coating" : "대형코팅",
    "master" : "마스터 인쇄",
    "offset" : "오프셋 인쇄"
}

list_product = list()
for elem in product_list.objects.all():
    list_product.append(elem.list_name)

def initial_list(request):
    product_li = ["report", "poster", "formboard", "paper", "hard", 
    "spring", "binder", "catalog", "print", "invite", "creature_of_prize", "memorial", "postit", "shoppingbag", "envelope",
    "namecard", "sticker", "exhibit", "photo", "bigcoating", "bici", "printout", "album", "hospital", "profile", "rock", "wedding"
    ,"calendar", "diary", "prize", "index", "drawing", "general", "master", "offset", "academy", "kindergarden"]

    for idx in range(len(product_li)):
        try:
            product_list(list_name = product_li[idx]).save()
        except:
            pass
    redirect('product')

def transfer_to_email(request):
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     subject = request.POST['subject']
    #     message = request.POST['message']
    #     tel = request.POST['tel']

    #     email = EmailMessage(
    #         "혜천문화사 홈페이지를 통해 다음과 같은 문의사항이 들어왔습니다 : " + str(subject),

    #         "이름(" + name + ")" + " 이메일(" + email + ") 전화번호(" + tel + ")"
    #         + "<br> 문의한 내용 : " + message,

    #         email,
            
    #         to = ['hccopy@naver.com'], # 서버 전송용 프로토콜
    #     )

    #     email.send()
    return redirect('home')

def product_page(request):
    context = {
        "product_li" : ["report", "poster", "formboard", "paper", "hard", 
                            "spring", "binder", "catalog", "print", "invite", "creature_of_prize", "memorial", "postit", "shoppingbag", "envelope",
                            "namecard", "sticker", "exhibit", "photo", "bigcoating", "bici", "printout", "album", "hospital", "profile", "rock", "wedding"
                            ,"calendar", "diary", "prize", "index", "drawing", "general", "master", "offset", "academy", "kindergarden"],
        }

    context = {"product_li" : list_product}
    return render(request, 'base_product.html', context)

def initial(request): #초기화 하는 코드 -> 제품 으로 통합
    BASE = os.path.dirname(os.path.abspath(__file__))
    initial_list = ["report", "poster", "formboard", "paper", "hard", "drawing", "spring", "binder", "index", "catalog", "invite", "report_box", "prize", "print", "memorial", "postit", "shoppingbag", "envelope", "namecard", "sticker", "exhibit", "bigcoating", "general", "rock", "wedding", "profile", "diary", "calendar", "master", "offset", "academy"]
    for category_name in initial_list:
        file_path = category_name + "_url.txt"
        f = open(os.path.join(BASE, "product_urls", file_path))
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            print(line)
            print(product_li[category_idx])
            temp_elem = product(name=line[:line.find(".")], ext=line[line.find(".")+1:], category=product_list.objects.get(list_name=product_li[category_idx]), src="product_source/"+product_li[category_idx]+"/"+line)
            temp_elem.save()
            print(line[:line.find(".")], line[line.find(".")+1:])
        f.close()
    redirect('product')

    # for category_name in initial_list:
    #     file_path = category_name + "_url.txt"
    #     f = open(os.path.join(BASE, "product_urls", file_path))
    #     lines = f.readlines()
    #     for line in lines:
    #         line = line.strip()
    #         print(line)
    #         print(category_name)
    #         temp_elem = product(name=line[:line.find(".")], ext=line[line.find(".")+1:], category=product_list.objects.get(list_name=category_name), src="product_source/"+category_name+"/"+line)
    #         temp_elem.save()
    #         print(line[:line.find(".")], line[line.find(".")+1:])
    #     f.close()
    # redirect('product')

def delete_init(request):
    product.objects.all().delete()
    return redirect('product')

def product_view(request, product_name):

    dict_product = {
        "hospital" : "각종 병원 양식",
        "album" : "앨범",
        "printout" : "각종 인쇄",
        "bici" : "BI & CI 간판 디자인",
        "bigcoating" : "대형 코팅",
        "photo" : "상업용 사진",
        "exhibit" : "전시회 백월 포스터",
        "sticker" : "스티커",
        "namecard" : "명함",
        "envelope" : "봉투",
        "shoppingbag" : "쇼핑백",
        "postit" : "포스트잇",
        "memorial" : "기념품",
        "creature_of_prize" : "상패 디자인",
        "invite" : "청첩장 & 초대장",
        "prize" : "상장 & 단증",
        "print" : "각종 출력",
        "catalog" : "카탈로그",
        "binder" : "바인더",
        "spring" : "스프링",
        "hard" : "하드커버제본",
        "spring" : "스프링제본",
        "formboard" : "폼보드",
        "report" : "보고서 & 제안서",
        "poster" : "포스터 & 학회포스터",
        "paper" : "논문",
        "rock" : "석부작 작품",
        "wedding" : "웨딩사진 출력",
        "profile" : "혜천문화사 프로필",
        "diary" : "다이어리",
        "calendar" : "달력", 
        "general" : "일반 제본 및 교본",
        "index" : "인덱스",
        "drawing" : "도면 제본",
        "big_coating" : "대형코팅",
        "master": "마스터",
        "academy" : "각종 학원 교재",
        "kindergarden" : "각종 유치원 교재",
    }

    context = {
        "product_detail" : product.objects.filter(name=product_name),
        "product_li" : ["report", "poster", "formboard", "paper", "hard", 
                            "spring", "binder", "catalog", "print", "invite", "creature_of_prize", "memorial", "postit", "shoppingbag", "envelope",
                            "namecard", "sticker", "exhibit", "photo", "bigcoating", "bici", "printout", "album", "hospital", "profile", "rock", "wedding"
                            ,"calendar", "diary", "prize", "index", "drawing", "general", "master", "offset", "academy", "kindergarden"],
        "product_name" : product_name,
        "product_title": dict_product[product_name],
    }

    return render(request, "product_detail/product_detail.html", context)