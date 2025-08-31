from rest_framework import serializers

from announcements.models import Review
from announcements.paginators import ADSPagination
from announcements.serializers import AnnouncementSerializer, ReviewSerializer

from .models import User


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class ProfileUserSerializer(serializers.ModelSerializer):

    announcements = AnnouncementSerializer(many=True, read_only=True)
    author_reviews = ReviewSerializer(many=True, read_only=True)
    received_reviews = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "phone",
            "image",
            "announcements",
            "author_reviews",
            "received_reviews",
        )

    def get_received_reviews(self, obj):

        announcements = obj.announcements.all()
        reviews = Review.objects.filter(announcement__in=announcements)

        paginator = ADSPagination()
        paginated_reviews = paginator.paginate_queryset(
            reviews, self.context["request"]
        )

        return ReviewSerializer(paginated_reviews, many=True).data


class ProfileOwnerAdSerializer(serializers.ModelSerializer):

    announcements = AnnouncementSerializer(many=True, read_only=True)
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "first_name",
            "phone",
            "image",
            "announcements",
            "reviews",
        )

    def get_reviews(self, obj):

        announcements = obj.announcements.all()
        reviews = Review.objects.filter(announcement__in=announcements)

        paginator = ADSPagination()
        paginated_reviews = paginator.paginate_queryset(
            reviews, self.context["request"]
        )
        return ReviewSerializer(paginated_reviews, many=True).data
