from django.shortcuts import render
from django.http import HttpResponse
from . models import *

# Create your views here.
def fn_index(request):
    if request.method == 'POST':
        # print(request.POST)
        # print(request.FILES)
        user_image = request.FILES['myfile']
        image_obj = UserImage(image=user_image)
        image_obj.save()
        if image_obj.id > 0:
            return render(request, 'testfile.html',{'image':image_obj.image})
    return render(request, 'testfile.html')



