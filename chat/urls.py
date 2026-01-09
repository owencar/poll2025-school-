from django.urls import path
from .views import Grouplist, Chatview, Groupcreate, Chatcreate

urlpatterns = [
    path("", Grouplist.as_view(), name='group_list'),
    path("<int:pk>/", Chatview.as_view(), name= 'chat_view'),
    path("add/", Groupcreate.as_view(), name= 'group_create'),
    path("<int:cid>/add", Chatcreate.as_view(), name= 'chat_create')
]