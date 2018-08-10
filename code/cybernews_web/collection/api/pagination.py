from rest_framework.pagination import LimitOffsetPagination


class EntryPagination(LimitOffsetPagination):
    page_size_query_param = 'page_size'
    default_limit = 20
    max_limit = 1000
