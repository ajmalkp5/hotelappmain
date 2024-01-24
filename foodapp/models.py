from django.db import models


class Hotelapp(models.Model):
    hotel=models.CharField(max_length=200,unique=True)
    foodname=models.CharField(max_length=200)
    quantity=models.PositiveIntegerField()
    special=models.CharField(max_length=200)
    maxtime=models.PositiveIntegerField()
    delivery=models.CharField(max_length=200)
    price=models.PositiveIntegerField()

    def __str__(self):
        return self.hotel




