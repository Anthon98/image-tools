from base64 import b64encode
from io import BytesIO
from PIL import Image as PILImage
from typing import BinaryIO


def create_cache_image(name='test_image', size=(512, 256), color=(128, 128, 128)) -> BinaryIO:
    """Creates a byte .webp image I/O stream in memory."""
    image_format = 'webp'
    image = PILImage.new(mode='RGBA', size=size, color=color)
    file = BytesIO()
    file.name = '%s.%s' % (name, image_format)
    image.save(file, format=image_format)
    file.seek(0)  # Reset the handle offset.
    return file


def convert_to_base64_string(img_stream: BinaryIO) -> str:
    """Encodes and decodes an I/O stream into a utf-8 byte64 string literal."""
    return b64encode(img_stream.read()).decode('utf-8')


def base64_data_uri_format(base64_string: str) -> str:
    """Gives the DataURI prefix for the image base64 string to mimic front-end image generation."""
    return 'data:image/webp;base64,%s' % base64_string


def handle() -> None:
    """The core handler function."""
    image_stream = create_cache_image(name='test_image')
    image_base64_string = convert_to_base64_string(img_stream=image_stream)
    image_data_uri = base64_data_uri_format(base64_string=image_base64_string)
    print(image_data_uri)


if __name__ == '__main__':
    handle()
