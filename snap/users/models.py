from django.db import models
from snap.common.models import BaseModel

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager as BUM
from django.contrib.auth.models import PermissionsMixin


class BaseUserManager(BUM):
    def create_user(self, name, mobile_num, email, is_active=True, is_admin=False, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(name=name, mobile_num=mobile_num, email=self.normalize_email(email.lower()),
                          is_active=is_active, is_admin=is_admin)

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, name, mobile_num, email, password=None):
        user = self.create_user(
            name=name,
            mobile_num=mobile_num,
            email=email,
            is_active=True,
            is_admin=True,
            password=password,
        )

        user.is_superuser = True
        user.save(using=self._db)

        return user


class BaseUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email address",
                              unique=True)
    name = models.CharField(max_length=100)
    mobile_num = models.CharField(max_length=11)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = BaseUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def is_staff(self):
        return self.is_admin
