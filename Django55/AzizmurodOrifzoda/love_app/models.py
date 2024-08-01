from django.db import models


DUE_DATE = (
    ("1", "Monday"),
    ("2", "Tuesday"),
    ("3", "Wensday"),
    ("4", "Thursday"),
    ("5", "Friday"),
    ("6", "Saturday"),
    ("7", "Sunday"),
)

# Create your models here.

class CustomerUser(models.Model):

    fname=models.CharField(max_length=40)
    lname=models.CharField( max_length=50)
    age=models.IntegerField()
    adress=models.CharField(max_length=50)
    email=models.EmailField()
    phone_number=models.CharField(max_length=20)



    def __str__(self):
        return self.fname + " " + self.lname

class Tasks(models.Model):
    title = models.CharField(max_length=250)
    due_date = models.CharField(max_length=250, choices=DUE_DATE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
