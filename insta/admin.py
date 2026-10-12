from django.contrib import admin

from insta.models import Profile, Post


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["profile", "text"]