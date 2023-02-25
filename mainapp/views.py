from rest_framework.generics import ListAPIView

from mainapp.models import Slider1, Slider2, Slider3
from mainapp.serializers import (
    Slider1Serializer,
    Slider2Serializer,
    Slider3Serializer
)


class Slider1View(ListAPIView):
    queryset = Slider1.objects.all()
    serializer_class = Slider1Serializer


class Slider2View(ListAPIView):
    queryset = Slider2.objects.all()
    serializer_class = Slider2Serializer


class Slider3View(ListAPIView):
    queryset = Slider3.objects.all()
    serializer_class = Slider3Serializer
