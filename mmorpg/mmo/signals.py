from django.db.models.signals import post_save

from .tasks import *
from django.dispatch import receiver


@receiver(post_save, sender=Post)
def send_notify_new_post_handler(sender, instance, created, **kwargs):
    if created:
        send_notify_new_post.delay(instance.pk)

@receiver(post_save, sender=Response)
def send_notify_new_response_handler(sender, instance, created, **kwargs):
    if created:
        send_notify_new_response.delay(instance.post_id, instance.id)

@receiver(post_save, sender=Response)
def send_notify_accept_response_handler(sender, instance, created, **kwargs):
    if not created:
        if instance.status != kwargs.get('update_fields', None):
            send_notify_accept_response.delay(instance.id)