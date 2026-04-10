from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from users.forms import LoginForm, signupForm
from users.models import User

def login_view(req):
    if req.user.is_authenticated:
        return redirect('/posts/feeds')

    if req.method == "POST":
        form = LoginForm(data = req.POST)
        if form.is_valid():
           username = form.cleaned_data['username']
           password = form.cleaned_data['password']
           user = authenticate(username=username, password=password)
            #해당 사용자가 존재한다면
           if user:
               login(req, user) #로그인 처리
               return redirect('/posts/feeds/') # 리다이렉트
           else:
               form.add_error(None,'입력한 자격증명에 해당하는 사용자가 없습니다.')

        #어떤 경우든 실패했을 때
        context = {'form': form}
        return render(req, 'login.html', context)
    else:
        form = LoginForm()
        context = {'form': form}
        return render(req,'login.html',context)

def logout_view(req):
    logout(req)
    return redirect('/users/login/')

def signup(req):
    #Post 요청 시, form이 유효한다면 최종적으로 redirect 처리된다
    if req.method == "POST":
        form = signupForm(data=req.POST, files=req.FILES)
        if form.is_valid():
            #form에서 에러 없으면 save() 메서드로 사용자 생성
            user = form.save()
            login(req, user)
            return redirect('posts/feeds/')
           #POst 요청에서 form이 유효하지 않다면 아래의 context = ... 부분으로 이동

   # GET요청에는 빈 Form을 보여준다
    else:
        form = signupForm()
    #context로 전달되는 form은 두가지 경우가 존재
    #1.POST 요청에서 생성된 form이 유효하지 않은 경우 -> 에러를 포함한 form이사용에게 보여진다
    #2.GET  요청으로 빈 form이 생성된 경우 -> 빈form이사용자에게 보여진다
    context = {"form": form}
    return render(req,'signup.html',context)

