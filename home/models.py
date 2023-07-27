from django.db import models
class award(models.Model):   #荣誉
    description=models.TextField(max_length=500,blank=True,null=True)#文字描述
    photo = models.ImageField(upload_to='award/',blank=True)#图片
# Create your models here.
