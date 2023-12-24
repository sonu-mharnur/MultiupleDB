from django.shortcuts import render
from django.http import JsonResponse
from .models import UserData
# Create your views here.

def registeruser(request):
    if request.POST:
        name= request.POST.get('name')
        contact = request.POST.get('contact')

        obj =UserData(name=name, contact=contact)
        obj .save(using='userdb')

        dic = {'status':'Successfully Registered' }
        return JsonResponse(dic)

def showuser(request):
    obj = UserData.objects.all().using('userdb')
    datali = []
    for rec in obj:
        datali.append({'name':rec.name,'contact':rec.contact})

    return JsonResponse(datali)

def registercar(request):
    pass


def showcar(request):
    pass
