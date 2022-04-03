from django.db import models


class Rental(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name
