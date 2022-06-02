from rest_framework.viewsets import ReadOnlyModelViewSet

from main.models import Autor
from main.serializers import AutorSerializer


class AutorViewSet(ReadOnlyModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer