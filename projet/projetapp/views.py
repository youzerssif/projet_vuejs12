from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import utilisateur
from django.core.validators import validate_email

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


def postsImage(request):
    # postdata = json.loads(request.body.decode('utf-8'))
        
    # name = request.POST['name']
    isSuccess=False
    compt=1
    while compt < 1000000:
        compt+=1
    if request.POST is not None:
        
        name=request.POST.get('name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        passconf=request.POST.get('passconf')
        print("Name ++++++++++++++++++++",name)
        print("Username ++++++++++++++++++++",username)
        print("Phone ++++++++++++++++++++",phone)
        emailOk=False
        if ((name is not None) and (username is not None) and (phone is not None) ):
            image=request.FILES['file']
            try:
                validate_email(email)
                emailOk=True
            except:
                result={
                    'success':False,
                    'message':'Email is not valide'
                }
            if emailOk:
                try:
                    user = utilisateur(username =username, name = name, email = email,phone=phone,images=image,password=password)
                    user.save()
                    
                    result={
                        'success':True,
                        'message':'Enregistrement Effectue avec success '
                    }
                except Exception as err:
                    print(err)
                    result={
                        'success':False,
                        'message':'Error lor de l\'enregistrement '
                    }
        else:
            result={
                'success':False,
                'message':'Veille verifier tous vos champs'
            }
    else:
        result={
            'success':False,
            'message':'Empty form '
        }
    
  
    print("+++++++++++++++++++++++++++++\n",request.POST['username'])
    print("+++++++++++++++++++++++++++++\n",request.FILES['file'])

    return JsonResponse(result, safe=False)
