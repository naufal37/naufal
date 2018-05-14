from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.
def posts_create(request):
    context = {
        "title": "Create"}
    return render(request, "index.html", context)

def posts_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance" : instance,}
    return render(request, "list.html", context)

def posts_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list" : queryset,
        "title": "List",}
    return render(request,"index.html",context)

def posts_update(request):
    return HttpResponse("<h1> Update </h1>")

def posts_delete(request):
    return HttpResponse("<h1> Delete </h1>")

def posts_awal(request):
    return HttpResponse("<h1> hello! </h1>")