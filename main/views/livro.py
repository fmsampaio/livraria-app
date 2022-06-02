from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from main.serializers import LivroSerializer, LivroDetailSerializer
from main.models import Livro


class LivroViewSet(ReadOnlyModelViewSet):
    queryset = Livro.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['ISBN', 'editora', 'categoria']
    search_fields = ['titulo']

    def get_serializer_class(self):
        if self.action == 'list':
            return LivroDetailSerializer
        if self.action == 'retrieve':
            return LivroDetailSerializer
        return LivroSerializer