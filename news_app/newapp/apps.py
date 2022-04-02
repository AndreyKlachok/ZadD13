from django.apps import AppConfig
import redis


class NewappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newapp'

    def ready(self):
        import newapp.signals


red = redis.Redis(
    host='redis-19994.c1.asia-northeast1-1.gce.cloud.redislabs.com',
    port=19994,
    password='K2qfVC40dQIPdMO3gzlEdIfFTVS4gncV'
)