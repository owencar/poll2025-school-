from django.shortcuts import render
from .models import Poll, Option 
from django.views.generic import ListView, DetailView, RedirectView #一個是獲取資料列表，一個是獲取詳細的資料;RedirectView 仔仔入夜麵食重新導向一次(把變更過的票數重新縣市一次)
 
# Create your views here.
def poll_list(req):   #，定義並接收來自url傳來的req
    polls = Poll.objects.all()   #把投票紀錄塞入Poll
    return render(req, "default/list.html",{'poll_list': polls,'msg':'hellow!'})
    #render(收到回應後， "用個頁面範本去顯示"， {"從poll_list中" 從所有在(:)polls中的 , 第二個傳去的資料'msg':'hellow' })

#資料模型Poll建在default/mosels.py
class Polllist(ListView):
    model = Poll  #定義資料來源要從哪個資料模型索要

    #尋找要顯示的頁面範本的規則(list view):[應用程式名稱/資料模型_list.html]
    #ex:[default/poll_list.html]>>>>他就會以(poll_list.html)作為頁面範本去顯示

class PollView(DetailView):  #DetailView 會預設用urld中設定的pk參數去找ip
    model = Poll

    #他會把獲得的參數傳給(頁面範本)[default/poll_detail.html]

#def poll_view(req, pk):
    #poll = Poll.object.get(id = pk)   (前備知識:每個資料在產生時會戴有一個屬於自己的id，從第一筆資料1、第二筆2....)此兩行是DetailView預設會做的事:找出資料id與pk相同的資料並且用於顯示
    def get_context_data(self, **kwargs):  #額外獲取要傳給頁面範本的資料(解決有些資料不再Poll中)        
        ctx =  super().get_context_data(**kwargs) #ctx是一本字典，裡面裝有DetailView獲取要傳給範本的資料和他沒獲取到的
        #option_list = Option.objects.filter(poll_id=self.object.id)  #object:紀錄獲取資料各種屬性(id就是其中一種)
        #ctx['option_list'] = option_list
        ctx['option_list'] = Option.objects.filter(poll_id=self.object.id)  #化簡上兩行
        return ctx #記得把加工後的資料傳回去給目標的頁面範本使用
class PollVote(RedirectView):
    pass