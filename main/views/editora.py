from rest_framework.viewsets import ReadOnlyModelViewSet
from main.serializers import EditoraSerializer
from main.models import Editora


class EditoraViewSet(ReadOnlyModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
