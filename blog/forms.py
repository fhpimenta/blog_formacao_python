from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    name = forms.CharField(max_length=30, label='Nome')
    body = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={'rows':4}),
        label='Escreva aqui seu comentário...'
    )

    class Meta:
        model=Comment
        fields=('name','body')
