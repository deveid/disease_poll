from django.db import models
from django.db.models import Count
from itertools import groupby
Gender_Choice = (
    ('Male', 'MALE'),
    ('Female', 'FEMALE'),
)

Diseases_Choice= (
    ('Cholera', 'CHOLERA'),
    ('HIV', 'HIV'),
    ('Malaria', 'MALARIA'),
    ('Typhoid', 'TYPHOID'),
    ('Measles', 'MEASLES'),
)


class Gender(models.Model):
    gender=models.CharField(max_length=19, choices=Gender_Choice , default='Male')

    def __str__(self):
        return self.gender


class Diseases(models.Model):
    gender_disease = models.ForeignKey(Gender, on_delete=models.CASCADE)
    diseases = models.CharField(max_length=19, choices=Diseases_Choice , default='Malaria')

    def __str__(self):
        return self.diseases
