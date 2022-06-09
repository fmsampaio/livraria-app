from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

from main.serializers import EditoraSerializer
from main.models import Editora


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nome']
