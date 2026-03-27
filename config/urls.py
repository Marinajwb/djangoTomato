"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from config.views import *
from tomato.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('post_list/',post_list),
    path('detail/<int:post_id>/', post_detail)
]

urlpatterns += static(
    prefix        = settings.MEDIA_URL,
    document_root = settings.MEDIA_ROOT

    #정적파일 처리는 Web server가 하는 것이 일반적이지만 개발단계의 편의성을 위해서만 Django에서 해주는 것


)