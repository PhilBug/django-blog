from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date_added']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'date_added', 'content', 'photo_description']
    list_per_page = 25

admin.site.register(Post, PostAdmin)
