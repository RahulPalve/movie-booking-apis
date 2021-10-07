from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CityViewSet, CinemaViewSet, MovieViewSet, ShowViewSet, book_ticket
from bms_api.docs.views import schema_view

router = DefaultRouter()
router.register(r'citys', CityViewSet, basename='city')
router.register(r'cinemas', CinemaViewSet, basename='cinema')
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'shows', ShowViewSet, basename='show')

urlpatterns = [
    path("show/<slug:show_codename>/book/<int:seat_no>", book_ticket),
    path("docs/", schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]

urlpatterns.extend(router.urls)