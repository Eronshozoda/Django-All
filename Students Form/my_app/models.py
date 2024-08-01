from django.db import models




class Cource(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    cource=models.ForeignKey("my_app.Cource",on_delete=models.CASCADE)
    fullname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=70)
    age=models.IntegerField(default=18)
    photo=models.ImageField(upload_to='static/images')
    email=models.EmailField(max_length=80)


    def __str__(self) -> str:
        return self.fullname
