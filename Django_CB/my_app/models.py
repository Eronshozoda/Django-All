from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=50, null=False, verbose_name='Name')
    last_name = models.CharField(max_length=50, null=False, verbose_name='Surname:')
    midle_name = models.CharField(max_length=50, null=True, blank=True)
    subject = models.CharField(max_length=50, null=False)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} The teacher of  {self.subject}'
