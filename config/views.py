from django.shortcuts import render, redirect

def index(req):
    if( req.user.is_authenticated ):
        return redirect('/posts/feeds/')
    else:
        return redirect('/users/login')