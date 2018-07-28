from django_filters import rest_framework as filters

from ..models import Article, Tag, Entry


class EntryFilter(filters.FilterSet):
    tags = filters.ModelMultipleChoiceFilter(
        name='tags__slug',
        to_field_name='slug',
        lookup_expr='in',
        queryset=Tag.objects.all()
    )

    user_reviewed = filters.BooleanFilter(
        name='user_reviewed',
    )

    date_range = filters.DateFromToRangeFilter(
        name='article__pub_date',
    )

    class Meta:
        model = Entry
        fields = ('tags', 'user_reviewed', 'date_range')
