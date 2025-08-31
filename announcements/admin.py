from django.contrib import admin

from announcements.models import Announcement, Review


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "price",
        "description",
        "created_at",
        "owner",
    )
    search_fields = ("owner",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "text",
        "owner",
        "announcement",
        "created_at",
    )
    search_fields = ("owner",)
