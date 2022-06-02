from rest_framework.viewsets import ReadOnlyModelViewSet

from main.serializers import CategoriaSerializer
from main.models import Categoria


class CategoriaViewSet(ReadOnlyModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
