from rest_framework.serializers import ModelSerializer, CharField
from rest_framework.serializers import SerializerMethodField
from rest_framework import serializers

from main.models import Autor, Categoria, Editora,  Livro


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'

class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'


class LivroDetailSerializer(ModelSerializer):
    categoria = CharField(source='categoria.descricao')
    editora = CharField(source='editora.nome')
    autores = SerializerMethodField()

    class Meta:
        model = Livro
        fields = '__all__'
        depth = 1

    def get_autores(self, instance):
        nomes_autores = []
        autores = instance.autores.get_queryset()
        for autor in autores:
            nomes_autores.append(autor.nome)
        return nomes_autores