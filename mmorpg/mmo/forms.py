import random
from string import hexdigits

from allauth.account.forms import SignupForm
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.conf import settings
from django.core.mail import send_mail

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

class CommonSignupForm(SignupForm):
    def save(self, request):
        user = super(CommonSignupForm, self).save(request)
        user.is_active = False
        code = ''.join(random.sample(hexdigits, 5))
        user.code = code
        user.save()
        send_mail(
            subject=f'Код активации',
            message=f'Код активации аккаунта: {code}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
        )
        return user