from django.db import models

# Create your models here.
# 这是一个表
class Test(models.Model):
    name = models.CharField(max_length=20)


class User(models.Model):
    fname = models.CharField(max_length=20)
    pw = models.CharField(max_length=20)
    