from django.db import models




class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
   

    def __str__(self):
        return self.name



class Product(models.Model):
    name=models.CharField(max_length=60)
    desciption=models.TextField()
    price=models.IntegerField()
    Category=models.ForeignKey("app.Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    