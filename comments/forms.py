from django import forms
from .models import BlogComment


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['comment_body']

    comment_body = forms.CharField(
        required=True,
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Add comment'
        })
    )
