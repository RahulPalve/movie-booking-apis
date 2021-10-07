
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Movie Booking REST API's",
      default_version='v0.1',
      description="APIs for system similar to bookmyshow",
      contact=openapi.Contact(email="hi.rahulpalve@gmail.com"),
      license=openapi.License(name="MIT"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)