from django.urls import path
from .views import poll_list, Polllist, PollView, PollVote

urlpatterns = [
    path("" , poll_list), #乎較位於views中的東西(ex.poll_list傳送req)
    path("list",Polllist.as_view(), name='poll_list'), #用name 為各種路徑取一個名子 
    path("<int:pk>/",PollView.as_view(), name = 'poll_view'), #用小於大於標示要變動的參數,pk是一個參數  ;#用name 為各種路徑取一個名子，可與poll_detail第12行的url合併使用
    path('<int:oid>/vote/',PollVote.as_view(), name= 'poll_vote')
]