from django.shortcuts import render, get_object_or_404, redirect, resolve_url  # 404 추가 / redirect 추가
from django.utils import timezone  # timezone import
from ..models import Question,Answer
# from django.http import HttpResponseNotAllowed
from ..forms import AnswerForm
#로그인이 필요한 함수
from django.contrib.auth.decorators import login_required
#넌필드 오류를 발생시킬 경우 메세지 출력
from django.contrib import messages 



#login 필요 애너테이션
@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id )
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            #author 속성에 현재 로그인 계정 저장 
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            #return redirect("pybo:detail", question_id=question.id) 
            #앵커 기능을 추가 resolve_url 은 실제 호출되는 URL 문자열을 리턴하는 장고함수 
            return redirect('{}#answer_{}'.format(
                resolve_url('pybo:detail', question_id=question.id),answer.id
            ))
    else:
        # return HttpResponseNotAllowed('Only POST is possible.')
        #402 오류 발생 방지 위해 수정 
        form = AnswerForm()
    context = {'question': question, 'form':form }
    return render(request, 'pybo/question_detail.html', context) 

#답변 삭제 함수 작성
@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제 권한이 없습니다.')
    else : 
        answer.delete() 
#    return redirect('pybo:detail', question_id = answer.question.id) 
    return redirect('{}#answer{}'.format(
        resolve_url('pybo:detail', question_id = answer.question.id), answer.id)
    )        

#답변 추천 함수 작성 
@login_required(login_url='common:login')
def answer_vote(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author : 
        messages.error(request, "본인이 작성한 글엔 추천을 할 수 없습니다.")
    else:
        answer.voter.add(request.user)
    #return redirect('pybo:detail', question_id = answer.question.id)  
    return redirect('{}#answer{}'.format(
        resolve_url('pybo:detail', question_id = answer.question.id), answer.id)
    )    