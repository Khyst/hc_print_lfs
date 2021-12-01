from django.db import models
import os
from uuid import uuid4
import datetime

dict_product = {
        "hospital" : "각종 병원 양식",
        "album" : "앨범",
        "printout" : "각종 인쇄",
        "bici" : "BI & CI 간판 디자인",
        "big_coating" : "대형 코팅",
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
}

class product_list(models.Model):
    list_name = models.CharField(max_length=20, default="")

    def __str__(self):
        try:
            return str(dict_product[self.list_name])
        except:
            return str(self.list_name)

# 제안서
class product_report(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="report", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="(페이지에 들어갈 이미지에 대한 제목)")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="(페이지에 들어갈 이미지에 대한 자세한 설명)")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/report/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "보고서/제안서"

# 학회 포스터
class product_poster(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="poster", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/poster/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "포스터/학회포스터"

# 폼 보드
class product_form_board(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="formboard", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/formboard/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "폼보드"

# 논문
class product_paper(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="paper", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/paper/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)
    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "논문"

# 하드커버 제본
class product_hard(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="hard", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/hard_binding/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)
    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "하드커버 제본"

# 도면 제본
class product_drawing(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="drawing", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/drawing_binding/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "도면(반책) 제본"

# 스프링 제본
class product_spring(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="spring", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/spring_binding/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "스프링 제본"

# 바인더
class product_binder(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="binder", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/binder/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "바인더"

# 인덱스
class product_index(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="index", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/index/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "인덱스(색인)"

# 카타로그
class product_catalog(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="catalog", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/catalog/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "카탈로그"

# 청첩장, 초대장
class product_invite(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="invite", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/invite/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "초대장"

# 상장, 단증, 자격증
class product_prize(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="prize", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/prize/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "상장 / 단증 / 자격증"

# 제안서 박스
class product_report_box(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="report_box", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/report_box/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "제안서 박스"

# 출력
class product_print(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="print", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/print/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "출력"

# 제본
class product_bindding(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="binding", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/binding/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "제본(현재 사용 x)"

# 기타
class product_etc(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="etc", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/etc/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "기타(현재 사용 X)"

# 기념품
class product_memorial(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="memorial", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/memorial/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "기념품"

# 포스트 잇
class product_post_it(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="postit", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/postit/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "포스트 잇"

# 상패
class product_creature_of_prize(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="creature_of_prize", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/creature_of_prize/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "상패"

# 명함
class product_namecard(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="namecard", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/namecard/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "명함"

# 봉투
class product_envelope(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="envelope", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/envelope/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "봉투"

# 스티커
class product_sticker(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="sticker", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/sticker/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "스티커"

# 쇼핑백
class product_shoppingbag(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="shoppingbag", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/shoppingbag/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "쇼핑백"

# 전시회 백월 포스터
class product_exhibit(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="exhibit", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/exhibit/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "전시회 백월 포스터"

# 명찰
class product_nametag(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="nametag", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/nametag/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)
    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "명찰"

# 대형 코팅
class product_bigcoating(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="general", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/bigcoating/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "대형코팅"

# 일반 교본
class product_general_binding(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'

        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], ext)
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="general", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/general_binding/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "보고서 책자 및 교본"

# 상업용 사진
class product_photo(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="photo", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/photo")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "상업용 사진"

# BI & CI
class product_bici(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="bici", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/bici")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "BI & CI"

# 각종 인쇄
class product_printout(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="printout", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/printout")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "각종 인쇄"

# 앨범
class product_album(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="album", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/album")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "앨범"

# 각종 병원 양식
class product_hospital(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="hospital", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/hospital")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "각종 병원 양식"

# 석부작 작품
class product_rock(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="rock", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/rock")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "석부작 작품"

# 웨딩 사진 출력
class product_wedding(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="wedding", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/wedding")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "웨딩 사진 출력"


# 혜천문화사 프로필
class product_profile(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="profile", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/profile")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "혜천문화사 프로필"


# 다이어리
class product_diary(models.Model):
    prod_name = "diary"

    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default=prod_name, blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/"+prod_name)
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "다이어리"

# 달력 (캘린더)
class product_calendar(models.Model):
    prod_name = "calendar"

    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default=prod_name, blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/"+prod_name)
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "달력 (캘린더) "

# 달력 (캘린더)
class product(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            self.ext = ext
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False)
    video_ok = models.BooleanField(default=False, verbose_name="동영상 여부: ", help_text="동영상 파일을 업로드 할 경우 체크해주세요!!")
    src = models.FileField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/")
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        try:
            return str(dict_product[self.name]) + str(self.pk)
        except:
            return str(self.name) + str(self.pk)

    class Meta:
        verbose_name_plural = "달력 (캘린더) "

