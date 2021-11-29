from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, password, last_name, email, phone, date_of_birth):
        user = self.model(
            username = username,
            last_name = last_name,
            phone = phone,
            date_of_birth = date_of_birth,
            date_joined = timezone.now(),
            is_superuser = 0,
            is_staff  = 0,
        )

