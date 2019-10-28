

from django.db import models
from django.utils import timezone
from typeidea.settings.base import MEDIA_ROOT


# Create your models here.


class FileImage(models.Model):
    '''上传文件和图片'''
    title = models.CharField(max_length=30, verbose_name="名称", default="")  # 标题
    image = models.ImageField(verbose_name="上传图片", upload_to="up_image", blank=True)
    files = models.FileField(verbose_name="上传文件", upload_to='up_file', blank=True)
    add_time = models.DateField(auto_now=True, verbose_name="添加时间")

    def __str__(self):
        return self.__doc__ + "title->" + self.title

    class Meta:
        verbose_name = "上传文件和图片"
        verbose_name_plural = verbose_name
        db_table='file'