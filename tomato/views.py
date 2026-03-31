from django.shortcuts import render
from tomato.models import Post

def post_list(req):
    posts = Post.objects.all()

    context = {'posts' : posts}

    return render(req,'post_list.html',context)

def post_detail(req,post_id):
    post = Post.objects.get(id=post_id)

    context = {
        'post' : post,
    }
    return render(req, "post_detail.html", context)

def post_add(req):
    if req.method == 'POST':
        print("method POST")
        title = req.POST['text']
        content = req.POST['content']
        print(title)
    else:
        print("method GET")
    return render(req, 'post_add.html')