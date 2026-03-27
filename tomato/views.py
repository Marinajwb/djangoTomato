from django.shortcuts import render
from tomato.models import Post

def post_list(req):
    posts = Post.objects.all()

    context = {'posts' : posts}

    return render(req,'post_list.html',context)