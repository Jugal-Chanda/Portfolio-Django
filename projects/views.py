from django.shortcuts import render,redirect
from django.http import HttpResponse
from projects.models import Project

def index(request):
    context = {}
    context['projects'] = Project.objects.all()
    return render(request,'projects.html',context)
