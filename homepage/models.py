from django.db import models
import os
from uuid import uuid4

class product_list(models.Model):
    pass

# 제안서
class product_report(models.Model):
    def auto_naming(self, filename):
        upload_to = f'{self.prefix}'
        uuid_name = uuid4().hex
        if self:
            ext = filename.split('.')[-1]
            filename = '{}_{}.{}'.format(self.prefix.split('/')[-2], uuid_name, ext)
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="report", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="(페이지에 들어갈 이미지에 대한 제목)")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="(페이지에 들어갈 이미지에 대한 자세한 설명)")
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/report/")
    def __str__(self):
        return '보고서/제안서_' + str(self.pk)

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
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="poster", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/poster/")

    def __str__(self):
        return '포스터/학회포스터_' + str(self.pk)

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
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="formboard", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/formboard/")

    def __str__(self):
        return '폼보드_' + str(self.pk)

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
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="paper", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/paper/")

    def __str__(self):
        return '논문_' + str(self.pk)

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
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="hard", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/hard_binding/")
    def __str__(self):
        return '하드커버 제본_' + str(self.pk)

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
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="drawing", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/drawing_binding/")

    def __str__(self):
        return '도면(반책) 제본_' + str(self.pk)

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
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="spring", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/spring_binding/")

    def __str__(self):
        return '스프링 제본_' + str(self.pk)

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
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="binder", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/binder/")

    def __str__(self):
        return '바인더_' + str(self.pk)

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
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="index", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/index/")

    def __str__(self):
        return '인덱스(색인)_' + str(self.pk)

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
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="catalog", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/catalog/")

    def __str__(self):
        return '카탈로그_' + str(self.pk)

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
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="invite", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/invite/")

    def __str__(self):
        return '청첩장 / 초대장_' + str(self.pk)

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
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="prize", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/prize/")

    def __str__(self):
        return '상장 / 단증 / 자격증_' + str(self.pk)

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
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="report_box", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/report_box/")

    def __str__(self):
        return '제안서 박스_' + str(self.pk)

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
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="print", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/print/")

    def __str__(self):
        return '출력_' + str(self.pk)

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
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="binding", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/binding/")

    def __str__(self):
        return '제본(현재 사용 x)_' + str(self.pk)

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
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="etc", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/etc/")

    def __str__(self):
        return '기타(현재 사용 X)_' + str(self.pk)

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
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="memorial", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/memorial/")

    def __str__(self):
        return '기념품_' + str(self.pk)

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
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="postit", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/postit/")

    def __str__(self):
        return '포스트 잇_' + str(self.pk)

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
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="creature_of_prize", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/creature_of_prize/")

    def __str__(self):
        return '상패_' + str(self.pk)

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
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="namecard", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/namecard/")

    def __str__(self):
        return '명함_' + str(self.pk)

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
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="envelope", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/envelope/")

    def __str__(self):
        return '봉투`_' + str(self.pk)

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
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="sticker", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/sticker/")

    def __str__(self):
        return '스티커_' + str(self.pk)

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
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="shoppingbag", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/shoppingbag/")

    def __str__(self):
        return '쇼핑백_' + str(self.pk)

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
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="exhibit", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/exhibit/")

    def __str__(self):
        return '전시회 백월 포스터_' + str(self.pk)

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
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="nametag", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/nametag/")
    def __str__(self):
        return '명찰_' + str(self.pk)

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
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="general", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/bigcoating/")

    def __str__(self):
        return '대형코팅_' + str(self.pk)

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
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/general_binding/")

    def __str__(self):
        return '보고서 책자 및 교본_' + str(self.pk)

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
            
        return os.path.join(upload_to, filename)
        
    name = models.CharField(max_length=20, default="photo", blank=True, help_text="자동 지정(입력 X)", editable=False)
    ext = models.CharField(max_length=20, blank=True, help_text="자동 지정(입력 X)", editable=False)
    title = models.CharField(max_length=20, blank= True, verbose_name="제목", help_text="페이지에 들어갈 이미지에 대한 제목 ( 입력 안해도 됨 )")
    desc = models.TextField(blank= True, verbose_name="설명", help_text="페이지에 들어갈 이미지에 대한 자세한 설명 (입력 안해도 됨 )")
    link_ok = models.BooleanField(default=False, verbose_name="이미지 직접 추가 여부:", help_text="이미지를 파일 추가를 해서 입력 하면 체크")
    img = models.ImageField(blank=True, upload_to=auto_naming)
    prefix = models.CharField(max_length=50, default="product_source/photo")

    def __str__(self):
        return '상업용 사진' + str(self.pk)

    class Meta:
        verbose_name_plural = "상업용 사진"
