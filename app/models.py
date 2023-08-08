from django.db import models

# Create your models here.
class Trainer(models.Model):
    Trainer_name=models.CharField(max_length=100,primary_key=True)
    Subject=models.CharField(max_length=100)
    Age=models.IntegerField()