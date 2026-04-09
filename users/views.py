from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from users.forms import LoginForm
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