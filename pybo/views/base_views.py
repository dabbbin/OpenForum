from django.shortcuts import render, get_object_or_404, redirect  # 404 추가 / redirect 추가
from ..models import Question
# from django.http import HttpResponseNotAllowed
from django.core.paginator import Paginator #paging 
#OR 조건으로 데이터를 조회하기 위해 Q함수 선언 
from django.db.models import Q




def index(request):
    page = request.GET.get('page', '1') #페이지 
    kw = request.GET.get('kw', '') #검색어 
    # 질문 목록 데이터를 얻는다.
    # order_by 를 통해 최근글로 정렬 - : 역방향
    question_list = Question.objects.order_by("-create_date")
    if kw: 
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  #제목검색 
            Q(content__icontains=kw) |  #내용검색 
            Q(answer__content__icontains=kw) | #답변 내용 검색
            Q(author__username__icontains=kw) | #질문 글쓴이 검색 
            Q(answer__author__username__icontains=kw) #답변 글쓴이 검색
        ).distinct()


    paginator = Paginator(question_list, 10) #페이지당 10개씩 보여줌 
    page_obj = paginator.get_page(page) #해당 페이지의 데이터만 조회하도록 쿼리가 변경
    # context = {"question_list": question_list}
    # page 와 kw 를 템플릿에 전달하기 위해 context 딕셔너리에 추가한다. 
    context = {"question_list": page_obj, 'page':page,'kw':kw}
    # render : 파이썬 데이터를 템플릿에 적용해 HTML 로 반환하는 함수
    return render(request, "pybo/question_list.html", context)
    # return HttpResponse("Hello, Pybo")

# 질문을 보여주는 views.detail 생성
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
