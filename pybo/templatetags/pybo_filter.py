import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

#템플릿 필터 함수 만들기 
#@register.filter 애너테이션을 적용하면 해당 함수를 필터로 사용 가능
@register.filter 
def sub(value, arg) :
    return value - arg

@register.filter
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))