from django.shortcuts import render, HttpResponse
from blog.models import Post,Categoria

def blog(request):
    posts = Post.objects.all()  
    return render(request, "blog/blog.html",{'posts':posts})

def categoria(request,categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categoria)  
    return render(request, "blog/categoria.html",{'categoria':categoria,'posts':posts})