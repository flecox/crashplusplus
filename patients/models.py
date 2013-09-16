from django.db import models

# Create your models here.

class Question(models.Model):

    GENRE_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    born_date = models.DateField('Born date')
    genre = models.CharField(max_length=2,
                             choices=GENRE_CHOICES)
    dni = models.CharField(max_length=8)
    clinical_history = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    study_level =  models.IntegerField()
    social_support = models.BooleanField()
