from django.db import models

# Create your models here.

class Subject(models.Model):
    label = models.CharField(max_length = 300, null = False, blank = False)
    target = models.FloatField()
    policy = models.FloatField()
    practice = models.FloatField()

    def __str__(self):
        return self.label



