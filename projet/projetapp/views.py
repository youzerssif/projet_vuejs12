from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.

def index(request):
    return render(request, 'index.html')

def enregistrement(request):
    return render(request, 'enregistrement.html')

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
    
    if username is not None:
        isSuccess=True
    else:
        isSuccess=False
    
    compt=1
    while compt <100000:
        compt += 1
    
    datas = {
        'success':True,
        'name':name
    }
    
    
    return JsonResponse(datas, safe=False)