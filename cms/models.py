from django.db import models


# Create your models here.
class Company(models.Model):
    creator = models.ForeignKey('auth.User')
    owner = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    stock_price = models.FloatField()

    def add(self):
        self.save()

    def __str__(self):
        rep = str(self.name) + ' ' + str(self.stock_price) + '$'
        return rep
