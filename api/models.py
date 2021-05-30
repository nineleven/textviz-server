from django.db import models


class SampleText(models.Model):

    name = models.CharField(max_length=40)

    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
