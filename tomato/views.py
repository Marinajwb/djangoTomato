from django.shortcuts import render
from tomato.models import Post

def post_list(req):
    posts = Post.objects.all()

    context = {'posts' : posts}

    return render(req,'post_list.html',context)

def post_detail(req,post_id):
    return render(req, "post_detail.html")