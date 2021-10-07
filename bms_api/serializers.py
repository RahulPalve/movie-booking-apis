from os import read
from rest_framework import serializers
from bms_api.models import City, Cinema, Movie, Show


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        exclude = ('created_at', 'updated_at')

class ShowSerializer(serializers.ModelSerializer):
    cinema = serializers.SlugRelatedField(
        slug_field="name", queryset=Cinema.objects.all()
    )
    movie = serializers.SlugRelatedField(
        slug_field="name", queryset=Movie.objects.all()
    )
    available_seats = serializers.ReadOnlyField()

    class Meta:
        model = Show
        exclude = ('created_at', 'updated_at')
        read_only_fields = ("booked_seats","available_seats")



class CinemaSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(
        slug_field="name", queryset=City.objects.all()
    )
    shows = ShowSerializer(many=True, read_only=True)

    class Meta:
        model = Cinema
        fields = ("name", "codename", "city", "shows")


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ('created_at', 'updated_at')


