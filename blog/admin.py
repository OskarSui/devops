from django.contrib import admin

from .models import Post, Comment

admin.site.register(Post)

admin.site.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'post', 'date_posted', 'active')
#     list_filter = ('active', 'date_posted', 'updated')
#     search_fields = ('name', 'email', 'content')