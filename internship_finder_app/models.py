from django.db import models
 

class Vacancy(models.Model):
    vacancy_title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
 


# Create your models here.
