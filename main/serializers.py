from rest_framework.serializers import ModelSerializer, CharField, HiddenField
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
    usuario = HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Livro
        fields = '__all__'


class LivroDetailSerializer(ModelSerializer):
    categoria = SerializerMethodField()
    #editora = CharField(source='editora.nome')
    editora = SerializerMethodField()
    autores = SerializerMethodField()

    class Meta:
        model = Livro
        #fields = '__all__'
        fields = ['id','ISBN','categoria','preco','quantidade','autores','editora']
        depth = 1

    def get_autores(self, instance):
        nomes_autores = []
        autores = instance.autores.get_queryset()
        for autor in autores:
            nomes_autores.append(
                {
                    "id" : autor.id,
                    "nome" : autor.nome
                }
            )
        return nomes_autores
    
    def get_editora(self, instance):
        return { 
            "id" : instance.editora.id,
            "nome" : instance.editora.nome
        }
    
    def get_categoria(self, instance):
        return {
            "id" : instance.categoria.id,
            "nome" : instance.categoria.descricao
        }