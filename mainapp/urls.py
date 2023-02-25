from django.urls import path

from mainapp.views import (
    Slider1View,
    Slider2View,
    Slider3View
)


urlpatterns = [
    path('slider_1/', Slider1View.as_view(), name='slider_1'),
    path('slider_2/', Slider2View.as_view(), name='slider_2'),
    path('slider_3/', Slider3View.as_view(), name='slider_3'),
]
