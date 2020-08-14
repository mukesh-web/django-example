from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
from django.utils.timezone import datetime
class Mart(models.Model):

    title=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    desc=models.TextField(blank=True)
    image=models.ImageField(upload_to='images/',blank=True,null=True)
    offer=models.BooleanField(default=False,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    important = models.BooleanField(default=False)


    datecompleted = models.DateTimeField(null=True, blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=True)



    def __str__(self):
        return self.title







