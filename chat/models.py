from django.db import models

# Create your models here.
class CHAT(models.Model):   #文字 
    subject = models.CharField("內文",max_length=200) 
    created = models.DateField("建立日期",auto_now_add=True) #發送時間
    user_name = models.CharField("使用者名稱",max_length=64)
    group_id = models.IntegerField("群組編號")
    def __str__(self):
        return f"{self.user_name}-{self.subject}"
    
class GROUP(models.Model): #群組
    group_name = models.CharField("群組名稱")
    desc = models.TextField("說明") #群組說明  
    def __str__(self):
        return self.group_name
