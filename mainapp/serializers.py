from rest_framework.serializers import ModelSerializer

from mainapp.models import (
    Slider1,
    Slider2,
    Slider3
)


class Slider1Serializer(ModelSerializer):
    class Meta:
        model = Slider1
        fields = (
            'id',
            'pic'
        )


class Slider2Serializer(ModelSerializer):
    class Meta:
        model = Slider2
        fields = (
            'id',
            'pic'
        )


class Slider3Serializer(ModelSerializer):
    class Meta:
        model = Slider3
        fields = (
            'id',
            'pic'
        )