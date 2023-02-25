import os

from uuid import uuid4

from django.db import models

from mainapp.services import compress


def image_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    path = f"{uuid4()}{basefilename}{file_extension}"
    return path


class ImgModel(models.Model):
    pic = models.ImageField(upload_to=image_path)

    def save(self, *args, **kwargs):                
        new_image =  compress(self.pic)                
        self.pic = new_image               
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.pic)

    class Meta:
        abstract = True
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"


class Slider1(ImgModel):
    class Meta:
        verbose_name = "Картинка для первого слайдера"
        verbose_name_plural = "Картинки для первого слайдера"


class Slider2(ImgModel):
    class Meta:
        verbose_name = "Картинка для второго слайдера"
        verbose_name_plural = "Картинки для второго слайдера"


class Slider3(ImgModel):
    class Meta:
        verbose_name = "Картинка для третьего слайдера"
        verbose_name_plural = "Картинки для третьего слайдера"