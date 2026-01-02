from django.urls import path
from .views import Grouplist

urlpatterns = [
    path("", Grouplist.as_view(), name='group_list'),
]