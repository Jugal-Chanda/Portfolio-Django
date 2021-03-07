from django.shortcuts import render,redirect
from django.http import HttpResponse

from blog.models import Blog
from blog.forms import BlogCreateForm
# Create your views here.

def index(request):
    context = {}
    blogs = Blog.objects.all()
    context['blogs'] = blogs
    return render(request,'blogs.html',context)

def create(request):
    context = {}
    if(request.POST):
        form = BlogCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Blog Created')
        else:
            context['form'] = form
    else:
        context['form'] = BlogCreateForm()
    return render(request,'blogs_create.html',context)

def delete(request,id):
    context = {}
    blog = Blog.objects.get(pk=id)
    blog.delete()
    return redirect('blog.index')
