from django import forms

from .models import Post

# iniform
class PostForm(forms.ModelForm):
    class Meta :
        model = Post
        fields = [
            "title",
            "content",
            "image",
            "draft",
            "publish",
        ]
