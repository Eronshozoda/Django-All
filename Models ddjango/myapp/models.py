from django.db import models

class Person(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    age=models.IntegerField()


# def __str__(self):
#     return {self.first_name}
