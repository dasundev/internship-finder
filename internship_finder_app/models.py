from django.db import models
 
# Create your models here.

class Vacancy(models.Model):
    vacancy_title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()


class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    skills = models.CharField(max_length=255, blank=True)
    other_skills  = models.CharField(max_length=100)

    def __str__(self):

        return self.username


