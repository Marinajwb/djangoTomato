from django.contrib import admin
from tomato.models import Post, Comment


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "thumbnail"]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
   pass