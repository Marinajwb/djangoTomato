from django.shortcuts import render, redirect
from tomato.models import Post, Comment

def post_list(req):
    posts = Post.objects.all()

    context = {'posts' : posts}

    return render(req,'post_list.html',context)

def post_detail(req,post_id):
    post = Post.objects.get(id=post_id)
    if req.method == 'POST':
        # textarea의 "name" 속성값을 가져옴
        comment_content = req.POST.get("comment")
        print(comment_content)
        Comment.objects.create(
            post    = post,
            content = comment_content,
        )
    context = {
        'post' : post,
    }
    return render(req, "post_detail.html", context)

def post_add(req):
    if req.method == 'POST':
        print("method POST")
        print(req.FILES)
        title = req.POST['text']
        content = req.POST['content']
        thumbnail = req.FILES["thumbnail"] #image file
        post = Post.objects.create(
            title=title,
            content=content,
            thumbnail = thumbnail
        )
        return redirect(f"/detail/{post.id}/")
    else:
        print("method GET")
    return render(req, 'post_add.html')