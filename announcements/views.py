from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters, generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from announcements.filters import AnnouncementFilter
from announcements.models import Announcement, Review
from announcements.paginators import ADSPagination
from announcements.serializers import (
    AnnouncementRetrieveSerializer,
    AnnouncementSerializer,
    ReviewSerializer,
)
from users.permissions import IsModer, IsOwner


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_description="Контроллер для получения списка всех объявлений"
    ),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_description="Контроллер для получения информации о конкретном объявлении"
    ),
)
@method_decorator(
    name="create",
    decorator=swagger_auto_schema(
        operation_description="Контроллер для создания объявления"
    ),
)
@method_decorator(
    name="update",
    decorator=swagger_auto_schema(
        operation_description="Контроллер для обновления информации об объявлении"
    ),
)
@method_decorator(
    name="partial_update",
    decorator=swagger_auto_schema(
        operation_description="Контроллер для обновления определенной информации об объявлении"
    ),
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(
        operation_description="Контроллер для удаления объявления"
    ),
)
class AnnouncementViewSet(viewsets.ModelViewSet):

    queryset = Announcement.objects.all()
    pagination_class = ADSPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = AnnouncementFilter
    filterset_fields = (
        "owner",
        "title",
        "created_at",
    )
    search_fields = ("title",)
    ordering_fields = ("created_at",)

    def perform_create(self, serializer):
        announcement = serializer.save()
        announcement.owner = self.request.user
        announcement.save()

    def get_serializer_class(self):
        """Выбор сериализатора в зависимости от действия."""
        if self.action == "retrieve":
            return AnnouncementRetrieveSerializer
        return AnnouncementSerializer

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [AllowAny]
        elif self.action == "create":
            self.permission_classes = [IsAuthenticated]
        elif self.action == "retrieve":  # ИСПРАВЛЕНО: убрано 'in'
            self.permission_classes = [IsAuthenticated | IsModer | IsOwner]
        elif self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes = [IsOwner | IsModer]
        else:
            self.permission_classes = [IsAuthenticated]  # Добавлено для других действий

        return super().get_permissions()


class ReviewCreateAPIView(generics.CreateAPIView):  # ИСПРАВЛЕНО: опечатка в названии

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        review = serializer.save()
        review.owner = self.request.user
        review.save()


class ReviewListAPIView(generics.ListAPIView):  # ИСПРАВЛЕНО: опечатка в названии

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = ADSPagination
    permission_classes = [AllowAny]


class ReviewUpdateAPIView(generics.UpdateAPIView):  # ИСПРАВЛЕНО: опечатка в названии

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsModer]


class ReviewDestroyAPIView(generics.DestroyAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsModer]
