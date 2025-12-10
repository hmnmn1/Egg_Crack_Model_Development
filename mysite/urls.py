"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
     # 추가: 빈 경로 ('') 요청을 todo 앱의 urls.py로 전달합니다.
    path('', include('todo.urls')), 
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')), 
    #todo로 시작하는 요청흔todo 앱 안의 urls.py로 전달 
]
