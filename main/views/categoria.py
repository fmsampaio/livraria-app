from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

from main.serializers import CategoriaSerializer
from main.models import Categoria


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = [SearchFilter]
    search_fields = ['descricao']
