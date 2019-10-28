from django.shortcuts import render
from .models import FileImage
# Create your views here.


def FileView(request):

    file_list=FileImage.objects.all()
    return render(request, 'upfile/show.html',{'title_list':file_list})