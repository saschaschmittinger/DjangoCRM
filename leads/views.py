from django.shortcuts import render
from .models import Lead



def home_view(request):
    leads= Lead.objects.all()
    title = 'CRM Home View'
    context ={
        'title':title,
        'leads':leads
    }
    return render(request,'leads/home.html',context)

