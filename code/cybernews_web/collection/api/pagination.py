from rest_framework.pagination import LimitOffsetPagination


class EntryPagination(LimitOffsetPagination):
    page_size_query_param = 'page_size'
    default_limit = 50
    max_limit = 1000
