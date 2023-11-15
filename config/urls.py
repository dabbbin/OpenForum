from django.contrib import admin
from django.urls import path
from pybo.views import base_views

#views import
#from pybo import views 
#path, include import 
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #pybo/ URL 요청되면 pybo.urls 시작하는 페이지를 요청하고 매핑 정보를
    # 읽어 처리한다. 
    path('pybo/', include('pybo.urls')),
    #common앱의 urls.py 파일 사용 
    path('common/', include('common.urls')),
    # '/' 에 해당되는 path 
    path('',base_views.index,name='index'), 
   
]

#handler 사용시 사용자 정의 뷰 함수 출력  
handler404 = 'common.views.page_not_found'

