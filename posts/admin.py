from django.contrib import admin

from posts.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "amount_of_upvotes", "author_name")
    ordering = ("creation_date",)
    list_filter = ("amount_of_upvotes",)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("content", "post", "author_name")
    ordering = ("creation_date",)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
