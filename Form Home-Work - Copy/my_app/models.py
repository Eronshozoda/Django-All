from django.db import models


class Cars(models.Model):
    name=models.CharField(max_length=50)
    # colores=(("Black","Black"),("Blue","Blue"),("Red","Red"),("Yellow","Yellow"))
    date_of_issue=models.IntegerField()
    color=models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Book(models.Model):
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=50)
    genre=models.CharField(max_length=50)


    def __str__(self):
        return self.title
    