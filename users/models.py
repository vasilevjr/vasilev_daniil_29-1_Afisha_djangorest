import string
from django.db import models
from django.contrib.auth.models import User
import random


def generation_code():
    return ''.join(random.choices(string.digits, k=6))


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, default=generation_code, unique=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.code
