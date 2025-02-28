from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Car

@receiver(post_save, sender=Car)
def send_car_notification(sender, instance, created, **kwargs):
    if created:  # faqat yangi car qo'shilganda
        subject = "Yangi avtomobil qo'shildi!"
        message = f"{instance.brand} markasidagi {instance.name} avtomobili qo'shildi."
        send_mail(subject, message, settings.EMAIL_HOST_USER, ['user@example.com'])
