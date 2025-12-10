# p79 Todo 모델을 관리자 페이지에 등록
from django.contrib import admin

from .models import Todo

admin.site.register(Todo)
