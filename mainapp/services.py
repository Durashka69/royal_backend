import os

from io import BytesIO

from uuid import uuid4

from PIL import Image

from django.core.files import File


def image_jpg_name(filename):
    basefilename, file_extension = os.path.splitext(str(filename))
    name = f"media/{uuid4()}{basefilename}.jpg"
    return name


def compress(image):
    im = Image.open(image)
    im = im.convert("RGB")
    print(im)
    im.save(image_jpg_name(im))
    print(im)
    im_io = BytesIO()
    im.save(im_io, "JPEG", quality=70)
    new_image = File(im_io, name=image.name)
    return new_image
