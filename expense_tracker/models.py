from django.db import models


# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(max_length=15, blank=False)
    last_name = models.CharField(max_length=15, blank=False)
    budget = models.FloatField(blank=False)

    def get_values_dict(self):
        new = dict([(x, y) for x, y in self.__dict__.items() if x != '_state' and x != 'id'])
        return new


class Expense(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False)
    image_url = models.URLField(blank=False, max_length=200)
    description = models.TextField(blank=False)
    price = models.FloatField(blank=False)

    def get_values_dict(self):
        new = dict([(x, y) for x, y in self.__dict__.items() if x != '_state' and x != 'id'])
        return new
