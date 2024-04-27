from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

from .models import *

@shared_task
def send_notify_new_post(pk):
    post = Post.objects.get(pk=pk)
    subscribers_emails = []

    subscribers = post.category.subscribers.all()
    subscribers_emails += [s.email for s in subscribers]

    html_content = render_to_string(
        template_name='post_created_email.html',
        context={
            'title': post.title,
            'link': f'{settings.SITE_URL}/post/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=post.title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers_emails,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()

@shared_task
def send_notify_new_response(post_id, response_id):
    post = Post.objects.get(pk=post_id)
    response = Response.objects.get(pk=response_id)
    author_email = post.user.email

    html_content = render_to_string(
        template_name='response_created_email.html',
        context={
            'author': response.user,
            'text': response.text,
            'link': f'{settings.SITE_URL}/post/{post_id}'
        }
    )

    msg = EmailMultiAlternatives(
        subject='У вашего поста новый отклик!',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[author_email],
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()

@shared_task
def send_notify_accept_response(response_id):
    response = Response.objects.get(pk=response_id)
    author_email = response.user.email
    post_id = response.post.pk

    html_content = render_to_string(
        template_name='accept_response_email.html',
        context={
            'link': f'{settings.SITE_URL}/post/{post_id}'
        }
    )

    msg = EmailMultiAlternatives(
        subject='Ваш отклик приняли',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[author_email],
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()