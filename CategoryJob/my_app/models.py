from django.db import models

class JobCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def str(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def str(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    salary = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255)

    def str(self):
        return self.title