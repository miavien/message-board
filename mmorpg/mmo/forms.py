from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'category',
        ]
        widgets = {
            'text': CKEditorUploadingWidget(),  # Используем CKEditor с возможностью загрузки файлов
        }

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = [
            'text',
        ]
