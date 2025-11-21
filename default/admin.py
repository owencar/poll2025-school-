from django.contrib import admin
from .models import Poll,Option 

# Register your models here.
admin.site.register(Poll)  #register>將自訂的資料註冊至後台
admin.site.register(Option)
