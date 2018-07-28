from rest_framework.pagination import LimitOffsetPagination


class EntryPagination(LimitOffsetPagination):
    page_size = 25
