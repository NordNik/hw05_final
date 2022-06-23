from django import forms
from .models import Post, Group, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

groups = Group.objects.all()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group', 'image')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)