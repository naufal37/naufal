from django.contrib import admin

# Register your models here.
from .models import Post,Postingan

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title","timestamp","updated"]
    list_display_links = ["timestamp","updated"]
    list_filter = ["timestamp","updated"]
    search_fields = ["title","content"]
    class Meta :
        model = Post


admin.site.register(Post,PostModelAdmin)