from celery import shared_task
from django.core.mail import EmailMultiAlternatives



@shared_task
def send_mail_for_sub_once(sub_username, sub_useremail, html_content):
    msg = EmailMultiAlternatives(
        subject=f'Здравствуй, {sub_username}. Новая статья в вашем разделе!',
        from_email='testpost111111@yandex.by',
        to=[sub_useremail]
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def send_mail_for_sub_every_week(sub_username, sub_useremail, html_content):
    msg = EmailMultiAlternatives(
        subject=f'Здравствуй, {sub_username}, новые статьи за прошлую неделю в вашем разделе!',
        from_email='testpost111111@yandex.by',
        to=[sub_useremail]
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()