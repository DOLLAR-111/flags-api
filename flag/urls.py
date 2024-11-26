from  django.urls import path
from .views import FlagsListCreateAPIView


urlpatterns = [
    path('', FlagsListCreateAPIView.as_view(), name="flags")

]
