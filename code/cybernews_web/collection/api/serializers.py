from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, StringRelatedField

from collection.models import Tag, Article, Entry


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class EntrySerializer(ModelSerializer):
    article = ArticleSerializer()
    tags = StringRelatedField(many=True)

    class Meta:
        model = Entry
        fields = '__all__'
        lookup_field = 'slug'

