from django.db import models
from django.contrib.postgres.fields import ArrayField

class City(models.Model):
    name = models.CharField(max_length=50)

class Cinema(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, related_name="cinemas", on_delete=models.CASCADE)

class Movie(models.Model):
    name = models.CharField(max_length=50)
    rating = models.DecimalField(default=5, max_digits=3, decimal_places=1)

class Show(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    total_seats = models.PositiveIntegerField(default=25)
    booked_seats = ArrayField(
        models.PositiveIntegerField(), size=25, blank=True, null=True
    )
    cinema = models.ForeignKey(Cinema, related_name="shows", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name="shows", on_delete=models.CASCADE)