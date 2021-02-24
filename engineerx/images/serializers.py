from rest_framework.fields import Field

from wagtail.api.v2.serializers import BaseSerializer


class ImageField(Field):
    def get_attribute(self, instance):
        return instance


class ImageLandscapeField(ImageField):
    def to_representation(self, image):
        return image.is_landscape()


class ImagePortraitField(ImageField):
    def to_representation(self, image):
        return image.is_portrait()


class ImageUrlField(ImageField):
    def to_representation(self, image):
        if image.is_landscape():
            return image.get_rendition('min-1500x200').url
        else:
            return image.get_rendition('min-200x1500').url


class ImageSerializer(BaseSerializer):
    is_landscape = ImageLandscapeField(read_only=True)
    is_portrait = ImagePortraitField(read_only=True)
    download_url = ImageUrlField(read_only=True)
