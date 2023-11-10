#계정 생성 시 사용할 UserForm 을 작성
from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 

#이미 속성들이 있어 UserForm 없이  그냥 사용해도 되지만, 이메일 등은 작성해야 한다. 
class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    #메타 클래스? 
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")
