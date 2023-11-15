#common 앱에 urls.py 신규 작성
from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    #LoginView 가 common dir 의 템플릿 참조하도록 변경 
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    #{% url ‘common:logout’ %} 에 대응하는 URL 매핑
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #signup url mapping
    path('signup/', views.signup, name='signup'), 
 ]


