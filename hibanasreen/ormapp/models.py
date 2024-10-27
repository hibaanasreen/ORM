from django.db import models
from django.contrib import admin
class Bankloan(models.Model):
   name=models.CharField(max_length=100)
   ifsc=models.CharField(max_length=30)
   mobno=models.IntegerField()
   accno=models.IntegerField(primary_key="accno")
   loanamount=models.IntegerField()

class BankloanAdmin(admin.ModelAdmin):
 list_display=('name','ifsc','mobno','accno','loanamount')



