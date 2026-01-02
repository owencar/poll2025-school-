from django.shortcuts import render
from .models import CHAT, GROUP
from django.views.generic import ListView, DetailView, RedirectView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy #給他一組路徑規則的名城她會反推一次路徑
from django.contrib.auth.mixins import LoginRequiredMixin #確保只有登入才能進行操作 #注意這屬性不能單獨存在，只能依附於別的屬性增強他們

# Create your views here.

def group_list(req):
    groups = GROUP.group_name.all()
    return render(req, "chtat/lsit.html",{'chat_list': groups})

class Grouplist(ListView):
    model = GROUP
