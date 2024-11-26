from rest_framework.generics import ListCreateAPIView,ListAPIView
from .models import Flags
from .serializers import FlagSerializer

class FlagsListCreateAPIView(ListCreateAPIView):
    queryset = Flags.objects.all()
    serializer_class = FlagSerializer   


class FlagsListEditAPIView(ListAPIView):
    queryset = Flags.objects.all()
    serializer_class = FlagSerializer
