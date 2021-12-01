# Generated by Django 3.2.8 on 2021-12-01 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_product_product_calendar_product_diary'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_paper',
            name='video_ok',
            field=models.BooleanField(default=False, help_text='동영상 파일을 업로드 할 경우 체크해주세요!!', verbose_name='동영상 여부: '),
        ),
        migrations.AlterField(
            model_name='product_paper',
            name='link_ok',
            field=models.BooleanField(default=False),
        ),
    ]
