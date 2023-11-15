#django.contrib.auth.authenticate - 사용자 인증 담당 (사용자명과 비밀번호 유효한지 검증)
#djnago.contrib.auth.login - 로그인을 담당(사용자 세션 생성)
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm  

def signup(request) : 
    #post - 입력값으로 사용자 생성
    if request.method == "POST" : 
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            #폼 입력값을 개별적으로 얻고 싶은 경우(인증 시 사용할 사용자명과 비밀번호를 얻음)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            #authenticate / login : 신규 사용자 생성 후 자동 로그인 될 수 있도록 
            user = authenticate(username=username, password=raw_password) 
            login(request, user)
            return redirect('index')
    else: #get - 회원가입 화면 띄움
            form = UserForm()
    return render(request, 'common/signup.html', {'form':form})


#page_not_found 함수 구현 
def page_not_found(request, exception) : 
     return render(request, 'common/404.html', {})  