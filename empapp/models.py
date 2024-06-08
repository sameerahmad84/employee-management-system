from django.db import models

# Create your models here.
class department(models.Model):
    deptname=models.CharField(max_length=50)
    
class employee(models.Model):
    name=models.CharField(max_length=50)
    empcode=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    
