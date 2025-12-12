from django.urls import path
from .views import poll_list, Polllist, PollView, PollVote, PollCreate, PollEdit, OptionCreate

urlpatterns = [
    #path("" , poll_list), #乎較位於views中的東西(ex.poll_list傳送req)
    #path("list",Polllist.as_view(), name='poll_list'), #用name 為各種路徑取一個名子 
    path("",Polllist.as_view(), name='poll_list'),
    path("<int:pk>/",PollView.as_view(), name = 'poll_view'), #用小於大於標示要變動的參數,pk是一個參數  ;#用name 為各種路徑取一個名子，可與poll_detail第12行的url合併使用
    path('<int:oid>/vote/',PollVote.as_view(), name= 'poll_vote'),
    path('add', PollCreate.as_view(), name='poll_create'), #新增頭投票主題
    path("<int:pk>/edit", PollEdit.as_view(), name="poll_edit"), #改變投票主題
    path("<int:pid>/add", OptionCreate.as_view(), name="option_create"), #新增投票選項
]

#<int:pk>中，pk是預設的變數名稱，無須額外跟listview說，但如果要自訂變數名稱的話要記的跟listview說(在default/views.py中有用到)