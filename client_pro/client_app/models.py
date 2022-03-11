from django.db import models
from django.contrib.auth.models import User


class userDetails(models.Model):
    roles = models.CharField(max_length=70, default='')
    deleted = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
