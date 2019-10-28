from django.contrib import admin

import xadmin
from xadmin import views
from .models import  FileImage

class ControlFiles(object):
    list_display = ['title', "add_time"]


xadmin.site.register(FileImage, ControlFiles)