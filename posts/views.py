from django.shortcuts import render, redirect

def feeds(req):
    if not req.user.is_authenticated:
        return redirect('/users/login')
    return render(req, 'feeds.html')