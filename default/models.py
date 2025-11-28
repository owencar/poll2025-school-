from django.db import models

# Create your models here.
#在這定義需要的資料類型
#開頭的英文字鳩可自訂
class Poll(models.Model):   #models.Model 如何與底層資料庫聯繫
    subject = models.CharField("投票主題",max_length=64)   #["投票主題"][subject]投票名稱，可自訂
    desc = models.TextField ("說明") #紀錄欄位型態
    created = models.DateField("建立日期",auto_now_add=True)  #紀錄投票時間(日期)
    
    def __str__(self):              #定義一種資料叫做'self'
        return self.subject
class Option(models.Model):
    title = models.CharField("選項文字", max_length=64)
    votes = models.IntegerField("票數", default=0) #紀錄該項投了幾次[IntegerField>>紀錄整數]
    poll_id = models.IntegerField("投票主題編號") #*id>在>models.Model自動產生的流水號，這裡用來記錄編號與資料庫的關係

    def __str__(self):
        return "{} - {}".format(self.poll_id, self.title)
        return  f"{self.poll_id} - {self.title}"