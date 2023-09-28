from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='drinks', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
