from django.db import models


class Company(models.Model):
    name=models.CharField( max_length=60)
    description=models.TextField()
    year_of_foundation=models.CharField(max_length=80)
    Condition_is_being_assessed=models.CharField(max_length=80)


    def  __str__(self):
        return self.name
    

class Product(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    company=models.ForeignKey("my_app.Company", on_delete=models.CASCADE)


    def  __str__(self):
        return self.name




