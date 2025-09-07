from django.urls import path
from rest_framework.routers import DefaultRouter

from announcements.apps import AnnouncementsConfig
from announcements.views import (
    AnnouncementViewSet,
    ReviewCreateAPIView,
    ReviewDestroyAPIView,
    ReviewListAPIView,
    ReviewUpdateAPIView,
)

app_name = AnnouncementsConfig.name


router = DefaultRouter()
router.register("", AnnouncementViewSet)

urlpatterns = [
    path("review_create/", ReviewCreateAPIView.as_view(), name="review_create"),
    path("review/<int:pk>/update", ReviewUpdateAPIView.as_view(), name="review_update"),
    path("review_list/", ReviewListAPIView.as_view(), name="review_list"),
    path(
        "review/<int:pk>/delete", ReviewDestroyAPIView.as_view(), name="review_delete"
    ),
] + router.urls
