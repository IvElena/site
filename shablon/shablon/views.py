from django.http import HttpResponse
from django.shortcuts import render


def one_page(request):
    return HttpResponse('<h1>Hello!!!</h1>')

def picters(request):
    return HttpResponse("info about picters")

def page(request):
    return render(request,"picters.html")

def menu(request):
    return render(request,'menu.html',{'menu':"Меню"})

def Napitki(request):
    return render(request,'Napitki.html',{'Napitki':"Напитки"})

def Vtorie_bluda(request):
    return render(request,'Vtorie_bluda.html',{'Vtorie_bluda':"Вторые блюда"})
