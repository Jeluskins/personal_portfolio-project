from unittest.util import _MAX_LENGTH
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2500)
    date = models.DateField(default = '2022-08-01')

    def __str__(self):
        return self.title