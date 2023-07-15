from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "text"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название задачи'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание задачи'
            })
        }