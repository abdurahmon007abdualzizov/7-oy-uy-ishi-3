from django.db import models

# Create your models here.

class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.CharField(max_length=10000)
    info = models.TextField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)



    def __str__(self):
        return self.name