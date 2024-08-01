from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=50, null=False, verbose_name='Ном:')
    last_name = models.CharField(max_length=50, null=False, verbose_name='Насаб:')
    midle_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Тахаллус:')
    subject = models.CharField(max_length=50, null=False)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} Муаллими {self.subject}'
