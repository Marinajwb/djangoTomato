from django.shortcuts import render, redirect
from posts.models import Post
def feeds(req):
    if not req.user.is_authenticated:
        return redirect('/users/login')
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(req, 'feeds.html', context)
