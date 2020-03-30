from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    is_admin = models.NullBooleanField(default=False, db_index=True)
    email = models.EmailField(max_length=254, blank=True, unique=True)