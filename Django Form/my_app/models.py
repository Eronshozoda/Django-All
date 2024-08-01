from django.db import models

class Employee(models.Model):
    fullname=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    GENDER_CHOICE=((1,"male"),(2,"Female"),(3,"other"))
    gender=models.IntegerField(choices=GENDER_CHOICE)
    date_of_birth=models.DateField()
    is_active=models.BooleanField(default=True)
    email=models.EmailField(max_length=255)
    photo=models.ImageField(upload_to="static/images")


    def __str__(self):
        return self.fullname



