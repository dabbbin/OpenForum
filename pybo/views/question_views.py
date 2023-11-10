from django.shortcuts import render, get_object_or_404, redirect  # 404 추가 / redirect 추가
from django.utils import timezone  # timezone import
from ..models import Question

from ..forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator #paging 
#로그인이 필요한 함수
from django.contrib.auth.decorators import login_required
#넌필드 오류를 발생시킬 경우 메세지 출력
from django.contrib import messages 


# HttpResponse 요청에 대한 응답을 하기 위해
# from django.http import HttpResponse
# pybo/ URL 매핑될 views.index 함수를 추가한다.


#로그인 필요 애너테이션
@login_required(login_url='common:login')
# 질문 question_create 생성
def question_create(request):
    if request.method == "POST":
        # 인수를 넣어 subject, content값이 QuestionForm 의
        # 속성에 자동으로 저장되어 객체가 생성된다.
        form = QuestionForm(request.POST)
        # 폼이 유효하다면
        if form.is_valid():
            # 임시 저장(commit=false)해 question 객체를 리턴받음 why?
            question = form.save(commit=False)
            # author 속성에 로그인 계정을 저장   
            question.author = request.user 
            # 실제 저장을 위해 작성일시를 설정함
            question.create_date = timezone.now() 
            # 데이터를 실제로 저장함
            question.save()
            return redirect("pybo:index")
    else:
        form = QuestionForm()
        # get방식
    context = {"form": form}
    return render(request, "pybo/question_form.html", context)
    # 템플릿에서 질문 등록시 사용할 폼 엘리먼트

#수정 함수 작성
@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #로그인한 사용자와 수정하려는 질문의 글쓴이가 다를 경우 오류 발생 
    if request.user != question.author : 
        messages.user != question.author
        messages.error(request, '수정권한이 없습니다.')
        return redirect('pybo:detail', question.id) 
    if request.method == "POST": #수정 데이터 저장 
        # 질문수정 화면에 조회된 질문 제목 및 내용이 반영될 수 있도록 폼 생성 
        #instance 를 기준으로 QuestionForm 을 생성하지만 request.POST 값으로  덮어씀  
        form = QuestionForm(request.POST, instance=question) 
        if form.is_valid():
            question = form.save(commit=False)
            #질문 수정 일시 = 현재 일시
            question.modify_date = timezone.now()
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        #수정 버튼 클릭시 Get 방식으로 호출되어 질문수정화면으로 보여줌 
        #질문수정 템플릿 = 질문등록 템플릿(QuestionForm)
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

#질문 삭제 함수 작성
@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')

#질문 추천 기능 함수 작성 
@login_required(login_url='common:login')
def question_vote(request, question_id):
    question = get_object_or_404(Question, pk= question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다. ')
    else: #Question 모델의 voter 는 여러 사람을 추가할 수 있는 필드이므로 add함수를 사용 
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id= question.id)

