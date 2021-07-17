from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from.models import OrderLineItem

@reciever(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    update order total on lineitem create/update
    """
    instance.order.update_total()

@reciever(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    update order total on lineitem create/update
    """
    instance.order.update_total()
