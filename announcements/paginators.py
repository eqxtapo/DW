from rest_framework.pagination import PageNumberPagination


class ADSPagination(PageNumberPagination):

    page_size = 4
