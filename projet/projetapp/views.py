from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import utilisateur

# Create your views here.

def index(request):
    return render(request, 'index.html')

def enregistrement(request):
    return render(request, 'enregistrement.html')

def exo(request):
    return render(request, 'exo.html')

def senddata(request):
    
    postdata = json.loads(request.body.decode('utf-8'))
    
    # name = postdata['name']
    
    name = postdata['name']
    username = postdata['username']
    email = postdata['email']
    phone = postdata['phone']
    password = postdata['password']
    password1 = postdata['password1']
    isSuccess=False
    
    if name is not None and username is not None and email is not None and phone is not None and password is not None and password1 is not None:
        isSuccess=True
        if password == password1:
            users=utilisateur(name=name, username=username, email=email, phone=phone, password=password, password1=password1)
            users.save()
    else:
        isSuccess=False
    
    compt=1
    while compt < 100000:
        compt += 1
    
    datas = {
        'success':True,
        'name':name
    }
    
    
    return JsonResponse(datas, safe=False)


def sendfile(request):
    
    postdata = json.loads(request.body.decode('utf-8'))
    
    # name = postdata['name']
    
    name = postdata['name']
    username = postdata['username']
    email = postdata['email']
    phone = postdata['phone']
    image = postdata['image']
    password = postdata['password']
    password1 = postdata['password1']
    isSuccess=False
    
    if name is not None and username is not None and email is not None and phone is not None and password is not None and password1 is not None:
        isSuccess=True
        if password == password1:
            users=utilisateur(name=name, username=username, email=email, phone=phone, password=password, password1=password1)
            users.save()
    else:
        isSuccess=False
    
    compt=1
    while compt < 100000:
        compt += 1
    
    datas = {
        'success':True,
        'name':name
    }
    
    
    return JsonResponse(datas, safe=False)