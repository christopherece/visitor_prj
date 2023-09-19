# visitor/models.py
from django.db import models

class PersonToVisit(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

class Visitor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    person_to_visit = models.ForeignKey(PersonToVisit, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
