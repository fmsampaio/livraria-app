from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.filters import SearchFilter

from main.models import Autor
from main.serializers import AutorSerializer


class AutorViewSet(ReadOnlyModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nome']