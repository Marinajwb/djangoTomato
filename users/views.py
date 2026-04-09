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
    if req.method == "POST":
        form = signupForm(data=req.POST, files=req.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            profile_image = form.cleaned_data['profile_image']
            short_description = form.cleaned_data["short_description"]
            #비밀번호 확인값 겁사
            if password1 != password2:
                form.add_error('password2','비밀번호와 비밀번호 확인란의 값이 다릅니다.')
            if User.objects.filter(username=username).exists():
                form.add_error('username','현재 사용중인 사용자명 입니다.')
            #에러가 존재한다면, 에러를 포함한 form을 사용해 회원가입 페이지를 다시 렌더린
            if form.errors:
                context = {'form': form}
                return render(req, 'signup.html', context)
            #에러가 없다면 사용자를 생성하고 로그인 처리 후 피드 페이지로 이동
            else:
                user = User.objects.create_user(
                    username=username,
                    password = password1,
                    profile_image = profile_image,
                    short_description = short_description,
                    )
                login(req, user)
                return redirect('posts/feeds/')
        context = {'form' : form,}
        return render(req, 'signup.html', context)
    # GET요청에는 빈 Form을 보여준다
    else:
        form = signupForm()
        context = {"form": form}
    return render(req,'signup.html',context)

