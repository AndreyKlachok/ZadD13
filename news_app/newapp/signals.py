from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect
from django.template.loader import render_to_string
from .models import Post, Category


@receiver(post_save, sender=Post)
def send_sub_mail(sender, instance, created, **kwargs):
    global subscriber
    sub_text = instance.text
    category = Category.objects.get(pk=Post.objects.get(pk=instance.pk).category.pk)
    subscribers = category.subscribers.all()

    post = instance


    for subscriber in subscribers:
        html_content = render_to_string(
            'mail.html', {'user': subscriber, 'text': sub_text[:50], 'post': post})

        msg = EmailMultiAlternatives(
            subject=f'Здравствуй, {subscriber.username}. Новая статья в вашем разделе!',
            from_email='testpost111111@yandex.by',
            to=[subscriber.email]
        )

        msg.attach_alternative(html_content, 'text/html')
        msg.send()

    return redirect('/news/')
