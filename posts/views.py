from django.shortcuts import render, redirect
from posts.models import Post
from posts.forms import CommentForm
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect

def feeds(req):
    if not req.user.is_authenticated:
        return redirect('/users/login')
    posts = Post.objects.all()
    comment_form = CommentForm()
    context = {
        'posts' : posts,
        'comment_form' : comment_form,
    }
    return render(req, 'feeds.html', context)

@require_POST
def comment_add(req):
    #req.POST로 전달된 데이터를 사용해 CommentForm 인스턴스 생성
    form = CommentForm(data= req.POST)
    if form.is_valid():
        #commit= False 옵션으로 메모리상에 Comment 객체 생성
        comment = form.save(commit=False)
        #Comment 생성에 필요한 사용자 정보를 req에서 가져와 할당
        comment.user = req.user
        #DB에 Comment 객체 저장
        comment.save()

    return HttpResponseRedirect(f'/posts/feeds/#post-{comment.post.id}')