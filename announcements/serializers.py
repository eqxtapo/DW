from rest_framework import serializers

from .models import Announcement, Review
from .validators.validators import (
    ForbiddenWordValidator,
    RepeatAnnouncementValidator,
    price_zero_validator,
)


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ("id", "text", "created_at", "announcement", "owner")
        validators = [ForbiddenWordValidator(review_text="text")]


class AnnouncementSerializer(serializers.ModelSerializer):

    price = serializers.IntegerField(validators=(price_zero_validator,))

    class Meta:
        model = Announcement
        fields = (
            "id",
            "title",
            "price",
            "description",
            "created_at",
            "owner",
        )
        validators = [
            ForbiddenWordValidator(
                announcement_title="title", announcement_description="description"
            ),
            RepeatAnnouncementValidator(
                title="title", description="description", price="price"
            ),
        ]


class AnnouncementRetrieveSerializer(serializers.ModelSerializer):

    announcement_reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Announcement
        fields = (
            "id",
            "title",
            "price",
            "description",
            "created_at",
            "owner",
            "announcement_reviews",
        )
