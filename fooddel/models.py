from django.db import models

# Create your models here.

class UserLog(models.Model):
    userlogid = models.AutoField(primary_key = True)
    fullname = models.CharField(max_length = 150)
    email = models.CharField(max_length = 150)

class OrderLog(models.Model):
    quantity = models.FloatField(null = False)
    rate = models.FloatField(null = False)
    total = models.FloatField(null = False)
    userlogid = models.ForeignKey(UserLog, on_delete = models.PROTECT)

