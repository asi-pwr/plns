from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def _create_user(self,email,password,is_staff,is_superuser):
        if not email:
            raise ValueError('Email is Reqired')
        email = self.normalize_email(email)
        user= self.model(email=email,is_staff=is_staff,is_superuser=is_superuser)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self,email,password):
        return self._create_user(email,password,False,False)
    def create_superuser(self,email,password):
        return self._create_user(email,password,True,True)


class AbstractUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(('email address'), max_length=255,unique=True, db_index=True)
    is_staff = models.BooleanField(('Admin?'), default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')
        abstract = True

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email
class User(AbstractUser):

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'