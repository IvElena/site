from django.shortcuts import render
from django.http import HttpResponse

def page(request):
    return render(request,"picters.html")
def picters(request):
    return HttpResponse("info about picters")
def menu(request):
    return render(request,'menu.html',{'menu':"меню"})
def Napitki(request):
    return render(request,'Napitki.html',{'Napitki':"легкие рецепты"})
def Vtorie_bluda(request):
    return render(request,'Vtorie_bluda.html',{'Vtorie_bluda':"легкие рецепты"})
