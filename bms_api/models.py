import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField

class AbstractEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    codename = models.CharField(
        max_length=50,
        unique=True,
        default=uuid.uuid4
    )
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

class City(AbstractEntity):
    pass

class Cinema(AbstractEntity):
    city = models.ForeignKey(City, related_name="cinemas", on_delete=models.CASCADE)

class Movie(AbstractEntity):
    rating = models.DecimalField(default=5, max_digits=3, decimal_places=1)

class Show(AbstractEntity):
    start_time = models.TimeField()
    end_time = models.TimeField()
    total_seats = models.PositiveIntegerField(default=25)
    booked_seats = ArrayField(
        models.PositiveIntegerField(), size=25, blank=True, null=True
    )
    cinema = models.ForeignKey(Cinema, related_name="shows", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name="shows", on_delete=models.CASCADE)


    @property
    def available_seats(self):
        return self.total_seats-len(self.booked_seats)

    def book_seat(self, seat_no):
        if seat_no > self.total_seats or seat_no in self.booked_seats:
            return False
        else:
            self.booked_seats.append(seat_no)
            self.save()
            return True
        