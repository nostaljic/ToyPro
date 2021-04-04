from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path('',views.index,name='index'),
    #path('',views.login,name='login')
]
#views 파일의 main 함수를 default 경로에 매칭시켜준다.