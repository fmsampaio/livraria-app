from rest_framework.viewsets import ReadOnlyModelViewSet

from main.serializers import LivroSerializer, LivroDetailSerializer
from main.models import Livro


class LivroViewSet(ReadOnlyModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return LivroDetailSerializer
        if self.action == 'retrieve':
            return LivroDetailSerializer
        return LivroSerializer