from django.shortcuts import render, HttpResponse
from . forms import data

import cv2
import os
from . import api
from . model import classify as cs
result = ''
min = 0
max = 0
def index(request):
    form = data(request.POST or None, request.FILES)
    if form.is_valid():
        new_data = form.save(commit=False)
        image_predict = new_data.upload_image
        print(str(image_predict))
        new_data.save()
        global result
        result = str(cs.prediction("myapp/model/new_model", "myapp/model/labelbin", "D:/django_project/django_project/media/"+str(image_predict)))
        min_range = new_data.min_range
        max_range = new_data.max_range
        global min
        min = min_range
        global max
        max = max_range
        #api.search(result, str(min_range), str(max_range))
        new_data.delete()
        os.system("RD /S /Q D:\django_project\django_project\media")
    context = {'form': form}
    return render(request, 'index.html', context)

def index2(request):
    global result
    list = api.search(result, str(min), str(max))
    context = {'list': list, 'result' : result}
    return render(request, 'index2.html', context)
