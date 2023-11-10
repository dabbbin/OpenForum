from django import forms
from pybo.models import Question,Answer


# forms.ModelForm을 상속, 연결된 모델의 데이터를 저장 
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        # QuestionForm 에서 사용할 Question 모델의 속성
        fields = ["subject", "content"]
        # 라벨을 붙여 subject -> 제목 변환
        labels = {"subject": "제목", 
                  "content": "내용"}

class AnswerForm(forms.ModelForm) : 
    class Meta:
        model = Answer #Answer 모델 사용  
        fields = ['content'] #content 속성 사용 
        labels = {
            'content' : '답변내용',
        }
        