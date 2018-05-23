from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
# Create your views here.
def posts_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        simpan = form.save(commit=False)
        simpan.save()

    context = {
        "form": form,}
    return render(request, "post_form.html", context)

def posts_detail(request, id=None):
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

def posts_update(request,id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        simpan = form.save(commit=False)
        simpan.save()
    context = {
        "title": instance.title,
        "instance": instance,
        "form" : form, }
    return render(request, "post_form.html", context)


def posts_delete(request):
    return HttpResponse("<h1> Delete </h1>")

def posts_awal(request):
    return HttpResponse("<h1> hello! </h1>")