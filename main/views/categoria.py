from rest_framework.viewsets import ModelViewSet

from main.serializers import CategoriaSerializer
from main.models import Categoria


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
