from django.db import models

# Create your models here.


# creating a  model class 
class Destination(models.Model):
    id:int
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='')
    description=models.TextField
    price=models.IntegerField()


