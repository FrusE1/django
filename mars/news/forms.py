from django.forms import ModelForm, Textarea, TextInput, DateTimeInput
from .models import Articles


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи',
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание статьи',
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Контент',
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации',
            })
        }
