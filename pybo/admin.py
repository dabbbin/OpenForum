from django.contrib import admin
from .models import Question 
# Question 모델을 관리자에 등록

#Question 모델에 세부 기능을 추가하는 클래스 생성 
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject'] #subject 으로 질문 데이터를 검색

admin.site.register(Question, QuestionAdmin)

