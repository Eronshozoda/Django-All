from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=80)

    def __str__(self):
        return self.name
    

class Video(models.Model):
    title=models.CharField(max_length=200)
    upload_date=models.DateTimeField(auto_now_add=True)
    description=models.TextField()
    category=models.ForeignKey("my_app.Category", on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='videos/')
    image=models.ImageField(upload_to='videos/')

    def __str__(self):
        return self.title