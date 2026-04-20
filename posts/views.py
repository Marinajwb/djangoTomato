from django.shortcuts import render, redirect
from posts.models import Post, Comment, PostImage
from posts.forms import CommentForm, PostForm
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpResponseForbidden

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

@require_POST
def comment_delete(req,comment_id):
    if req.method == 'POST':
        comment = Comment.objects.get(id=comment_id)
        if comment.user == req.user:
            comment.delete()
            return HttpResponseRedirect(f'/posts/feeds/#post-{comment.post.id}')
        else:
            return HttpResponseForbidden("이 댓글을 삭제할 권한이 없습니다.")

def post_add(req):
    if( req.method == "POST"):
        form = PostForm(req.POST)
        if form.is_valid():
            # req.POST로 온 데이터 (conent)는 PostForm으로 처리
            post = form.save(commit=False)
            post.user = req.user
            post.save()
            #POST를 생성한 후
            #req.FILES로 전송된 이미지들을 순회하면 PostImage 객체를 생성한다
            for image_file in req.FILES.getlist("images"):
                # req.FILES로 가져온 파일은 Model의 ImageField 부분에 곧바로 할당한다
                PostImage.objects.create(
                    post=post,
                    photo=image_file)
            #모든 PostImage와 Post의 생성이 완료되면
            # 피드 페이지로 이동하여 생성된 Post의 위치로 스크롤되도록 한다.
            url = f'/posts/feeds/#post-{post.id}'
            return HttpResponseRedirect(url)
    else:
        form = PostForm()
    context = { 'form' : form }
    return render(req, 'post_add.html', context)