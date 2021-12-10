from django.db import models
import os
from uuid import uuid4
import datetime

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
        "offset" : "오프셋 디자인",
        "master" : "마스터 디자인",
}

class product_list(models.Model):
    list_name = models.CharField(max_length=20, default="")

    def __str__(self):
        try:
            return str(dict_product[self.list_name])
        except:
            return str(self.list_name)

    class Meta:
        verbose_name_plural = "제품 리스트"

# 바뀔 데이터베이스
class product(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_id = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            uuid_name = filename.split('.')[-2]
            print("upload_to : ", upload_to)
            print("upload_by : ", uuid_name)
            filename = '{}_{}.{}'.format(uuid_name, uuid_id, ext)
            self.ext = ext
            
        return os.path.join(upload_to, str(self.category.list_name), filename)
        
    name = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False, verbose_name="파일 이름")
    displayed_name= models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False, verbose_name="이름")
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False, verbose_name="확장자")
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming, verbose_name="미디어 파일(클릭시 보여짐)")
    prefix = models.CharField(max_length=50, default="product_source/", editable=False, verbose_name="미디어 파일 경로")
    create_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="생성된 날짜")
    update_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="업데이트된 날짜")
    category = models.ForeignKey("product_list", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        print(self.category.list_name)
        self.name = self.category.list_name
        print("name:", self.name)
        self.displayed_name = dict_product[self.name]
        print(str(self.src)[str(self.src).find(".")+1:])
        self.ext = str(self.src)[str(self.src).find(".")+1:]
        self.prefix = self.prefix + self.name + '/'

        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "제품"