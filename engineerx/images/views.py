from wagtail.images.api.v2 import views

from .serializers import ImageSerializer


class ImagesAPIViewSet(views.ImagesAPIViewSet):
    base_serializer_class = ImageSerializer
    meta_fields = views.ImagesAPIViewSet.meta_fields + [
        'is_landscape', 'is_portrait',
    ]
