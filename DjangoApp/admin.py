from django.contrib import admin
from .models import LikePost, Profile, Post, FollowersCount

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(FollowersCount)
admin.site.register(LikePost)


class PostAdmin(admin.ModelAdmin):
    fields = ['id', 'user', 'caption', 'created_at', 'image',]

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Header", {"fields": ['title', 'subtitle', 'article_slug', 'series', 'author', 'image_url']}),
        ("Content", {"fields": ['content', 'notes', 'image_url']}),
        ("Date", {"fields": ['modified']})
    ]