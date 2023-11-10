from django.db import models
#User Model : django.contrib.models 가 제공한 사용자 모델, 회원가입시 데이터저장에 사용한 모델
from django.contrib.auth.models import User

class Question(models.Model):
    #글쓴이 author 필드 생성 및 User 모델을 외래키로 적용 | 계정 삭제 시, 작성 질문 모두 삭제 
    author = models.ForeignKey(User,related_name="author_question" ,on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField() 
    create_date = models.DateTimeField()
    #추천인 추가   
    voter = models.ManyToManyField(User, related_name="voter_question") 
    #질문이 언제 수정되었는지 확인하는 수정일시 속성 추가 
    #modify_date칼럼에 null을 허용함 
    #blank=Ture 는 form.is_vaild() 를 통한 입력 데이터 검증 시 값이 없어도 됨 
    #null=true, blank = ture 는 어떤 조건으로든 값을 비워둘 수 있다.
    modify_date = models.DateTimeField(null=True, blank=True)
    #str 함수에 의해 질문 id값이 제목으로 표시 
    def __str__(self):
        return self.subject 
    
class Answer(models.Model): 
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    #Question 외래키로 받고, 부모(질문) 삭제시, 자식(답변)도 연쇄 삭제로 설정 
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    content = models.TextField() 
    #답이 언제 수정되었는지 확인하는 수정일시 속성 추가   
    modify_date = models.DateTimeField(null=True, blank=True) 
    create_date = models.DateTimeField()  
    voter = models.ManyToManyField(User, related_name="voter_answer") 