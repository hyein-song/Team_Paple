from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['post_name', 'post_content']

        labels = {
            'post_name': '제목',
            'post_content': '내용'
        }

        widgets = {
            'post_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'post_content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 1,
                    'cols': 40,
                    'style': 'height: 20em;'
                }
            )
        }
