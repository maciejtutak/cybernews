from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters import rest_framework as filters

from ..models import Tag, Entry, Article
from .serializers import TagSerializer, EntrySerializer, ArticleSerializer
from .pagination import EntryPagination
from .filters import EntryFilter


class TagViewSet(ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'slug'


class EntryViewSet(ReadOnlyModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    lookup_field = 'slug'

    pagination_class = EntryPagination
    filter_class = EntryFilter
    filter_backends = (filters.DjangoFilterBackend,)


class ArticleViewSet(ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'


