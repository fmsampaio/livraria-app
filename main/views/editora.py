from rest_framework.viewsets import ModelViewSet
from main.serializers import EditoraSerializer
from main.models import Editora


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
