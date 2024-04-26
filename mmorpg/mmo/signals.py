from django.db.models.signals import m2m_changed

from .tasks import *
from django.dispatch import receiver


@receiver(m2m_changed, sender=Category.subscribers.through)
def send_notify_new_post_handler(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        send_notify_new_post.delay(instance.pk)