from django.shortcuts import render
from .models import CHAT, GROUP
from django.views.generic import ListView, DetailView, RedirectView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy #給他一組路徑規則的名城她會反推一次路徑
from django.contrib.auth.mixins import LoginRequiredMixin #確保只有登入才能進行操作 #注意這屬性不能單獨存在，只能依附於別的屬性增強他們

# Create your views here.

def group_list(req):
    groups = GROUP.objects.all()
    return render(req, "chtat/lsit.html",{'group_list': groups})

class Grouplist(ListView):
    model = GROUP

class Chatview(DetailView):
    model = GROUP

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['chat_list'] = CHAT.objects.filter(group_id = self.object.id)
        return ctx
    
class Groupcreate(CreateView, LoginRequiredMixin):
    model = GROUP
    fields = '__all__'
    success_url = reverse_lazy('group_list')

class Chatcreate(CreateView, LoginRequiredMixin):
    model = CHAT
    fields = ['user_name', 'subject']

    def form_valid(self, form):
        form.instance.group_id = self.kwargs['cid']
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('chat_view', kwargs={'pk': self.kwargs['cid']})