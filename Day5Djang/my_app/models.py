from django.db import models

color=(
    ("Red","Red"),
    ("Blue","Blue"),
    ("Green","Green"),
    ("White","White"),
)



class Category(models.Model):
    category_name=models.CharField(max_length=50)



    def __str__(self):
        return self.category_name
    

class Product(models.Model):
    product_name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    color=models.CharField(max_length=50,choices=color)
    quantity=models.IntegerField()
    issue_year=models.IntegerField()
    cotegory_name=models.ForeignKey(Category,on_delete=models.CASCADE)




    def __str__(self):
        return self.product_name