from django.db import models

class Type(models.Model):
    description = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.description}'

class Acronyme(models.Model):
    acro = models.CharField(max_length=8)

    answer = models.CharField(max_length=64)

    type = models.ForeignKey('Type', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.acro} {self.answer}'
