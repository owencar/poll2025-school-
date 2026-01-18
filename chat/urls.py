from django.urls import path
from .views import Grouplist, Chatview, Groupcreate, Chatcreate, Groupupdate, Chatupdate, Groupdelete, Chatdelete

urlpatterns = [
    path("", Grouplist.as_view(), name='group_list'),
    path("<int:pk>/", Chatview.as_view(), name= 'chat_view'),
    path("add/", Groupcreate.as_view(), name= 'group_create'),
    path("<int:cid>/add", Chatcreate.as_view(), name= 'chat_create'),
    path("<int:pk>/update/", Groupupdate.as_view(), name= 'group_edit'),
    path("<int:uid>/edit", Chatupdate.as_view(), name= 'chat_edit'),
    path("<int:pk>/delete", Groupdelete.as_view(), name= 'group_delete'),
    path("<int:pk>/clean", Chatdelete.as_view(), name= 'chat_delete'),
]