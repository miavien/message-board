from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

from .models import *

@shared_task
def send_notify_new_post(pk):
    post = Post.objects.get(pk=pk)
    category = post.category
    subscribers_emails = []

    subscribers = category.subscribers.all()
    subscribers_emails += [s.email for s in subscribers]

    html_content = render_to_string(
        template_name='post_created_email.html',
        context={
            'text': post.text,
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
