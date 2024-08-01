from django.db import models

class Company(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    address=models.CharField(max_length=200)
    contact_info=models.CharField(max_length=100)



    def __str__(self):
        return self.name
    





class JobCategory(models.Model):
    name=models.CharField(max_length=50)


    def __str__(self):
        return self.name





class Job(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    salary=models.DecimalField(max_digits=10,decimal_places=2)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    category=models.ForeignKey(JobCategory,on_delete=models.SET_NULL,null=True)



    def __str__(self):
        return self.title


    


