from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

states = (("created", "created"),
          ("in_progress", "in_progress"),
          ("completed", "completed"),
          ("failed", "failed"))

roles = (
    ("superuser", "superuser"),
    ("admin", "admin"),
    ("guest", "guest")
)


class Prob(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    location = models.JSONField(blank=False, null=False)
    state = models.TextField(max_length=20, blank=False,
                             null=False, default='created', choices=states)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class userAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=20, blank=False,
                            null=False, default='guest', choices=roles)

    objects = userAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    def getName(self):
        return self.name

    def getShortName(self):
        return self.name

    def __str__(self):
        return self.email
