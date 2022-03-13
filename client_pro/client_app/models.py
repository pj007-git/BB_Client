from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)

class roles(models.Model):
    role_id = models.CharField(max_length=10)
    role_name = models.CharField(max_length=70, default='')

    def __str__(self) -> str:
        return self.role_id

class userDetails(models.Model):
    roles = models.ForeignKey(roles, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username
