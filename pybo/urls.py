from django.urls import path 
#from . import views 
#views.index 대신 base_views.index 전체 경로를 작성 
from .views import base_views, question_views, answer_views

#namespace
app_name = 'pybo'
#pybo/가 생략된 '' => config/urls.py파일에서 이미 aovld 
urlpatterns = [
    #base_views.py 
    #http://localhost:8000/pybo/URL = index 
    path('', base_views.index, name='index'),
    # http://localhost:8000/pybo/2 = detail
    path('<int:question_id>/',base_views.detail, name="detail"),


    #question_views.py
    path('question/create/',question_views.question_create, name='question_create'),
    #question_modify 수정 페이지 매핑
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    #질문 삭제 페이지 매핑
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),
    # 질문 추천 페이지 매핑
    path('question/vote/<int:question_id>/', question_views.question_vote, name='question_vote'),

    #answer_views.py 
    path('answer/create/<int:question_id>/', answer_views.answer_create,name='answer_create'),
    #질문 views.question_create 함수 경로 호출 
    #답변 삭제 페이지 매핑
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),
    # 답변 추천 페이지 매핑
    path('answer/vote/<int:answer_id>/', answer_views.answer_vote, name='answer_vote'), 

    #answer_views.py 


]