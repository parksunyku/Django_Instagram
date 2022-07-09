from django.contrib import admin
from .models import Post


@admin.register(Post)  # wrapping
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'is_public',
                    'message_length', 'created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']

    def message_length(self, post):
        return f"{len(post.message)} 글자"
