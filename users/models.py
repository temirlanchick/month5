from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    activation_code = models.CharField(max_length=6, blank=True, null=True)
    is_active_user = models.BooleanField(default=False)
