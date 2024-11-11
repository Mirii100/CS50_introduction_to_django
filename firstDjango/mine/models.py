from django.db import models

# Create your models here.
# creating member model

class Member(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=100)
    email=models.EmailField(null=True)
    phoneNumber=models.IntegerField(null=True)

    
