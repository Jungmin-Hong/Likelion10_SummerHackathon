from django.contrib import admin
from django.urls import path
from home import views
from board import views as board_views
from account import views as account_views
from party import views as party_views
from django.conf import settings #settings.py import
from django.conf.urls.static import static # 'static' import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    #게시판
    path('board/', board_views.board_main, name='board_main'),
    path('board/write', board_views.board_write, name='board_write'),
    path('board/detail/<int:board_id>', board_views.board_detail, name='board_detail'),
    path('newcomment/<int:board_id>', board_views.new_comment, name='new_comment'),
    path('good/', board_views.board_good, name='board_good'),
    path('bad/', board_views.board_bad, name='board_bad'),
    #마이페이지
    path('mypage', account_views.mypage, name='mypage'),
    path('signup', account_views.signup, name='signup'),
    #파티
    path('party/', party_views.party_main, name='party_main'),
    path('party/frugality', party_views.party_main_fru, name='party_main_fru'), #절약 카테고리
    path('party/saving', party_views.party_main_saving, name='party_main_saving'), #저축 카테고리
    path('party/detail/<int:team_id>', party_views.party_detail, name='party_detail'), # 파티 상세화면
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
