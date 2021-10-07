from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django_filters import filterset, rest_framework as filters
from bms_api.models import City, Cinema, Movie, Show
from .serializers import (
    CitySerializer,
    CinemaSerializer,
    MovieSerializer,
    ShowSerializer,
)


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    lookup_field = "name"
    serializer_class = CitySerializer

class CinemaFilter(filters.FilterSet):
    movie = filters.CharFilter(field_name="shows__movie__name", lookup_expr='iexact')
    city = filters.CharFilter(field_name="city", lookup_expr='iexact')

    class Meta:
        model = Cinema
        fields = ['movie',]

class CinemaViewSet(viewsets.ModelViewSet):
    queryset = Cinema.objects.all()
    lookup_field = "name"
    serializer_class = CinemaSerializer
    filterset_class = CinemaFilter

class MovieFilter(filters.FilterSet):
    city = filters.CharFilter(field_name="shows__cinema__city__name", lookup_expr='iexact')

    class Meta:
        model = Movie
        fields = ['city',]

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    lookup_field = "name"
    serializer_class = MovieSerializer
    filterset_class = MovieFilter


class ShowViewSet(viewsets.ModelViewSet):
    queryset = Show.objects.all()
    lookup_field = "name"
    serializer_class = ShowSerializer

@api_view(["GET"])
def book_ticket(request, show_codename, seat_no):
    try:
        show = Show.objects.get(codename=show_codename)
        if not show.book_seat(seat_no):
            return JsonResponse({
                "status":"error", "msg": "Seat is already booked"
            })
    except Show.DoesNotExist:
        return JsonResponse({"status": "error", "msg":"Show does not exist"})
