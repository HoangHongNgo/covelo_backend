from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _


class Bicycle(models.Model):
    bicycle_id = models.CharField(max_length=50, unique=True, default='')
    is_good = models.BooleanField()


class Station(models.Model):
    location = models.CharField(max_length=30)
    capacity = models.IntegerField()


class Locker(models.Model):
    bicycle = models.ForeignKey(Bicycle, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE, default='')


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, name, age, type, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        if not name:
            raise ValueError('The Name field must be set')
        if not age:
            raise ValueError('The Age field must be set')
        if not type:
            raise ValueError('The Type field must be set')
        user = self.model(
            username=username,
            name=name,
            age=age,
            type=type,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    type = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'age', 'type']

    def __str__(self):
        return self.username


class Rental(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='user_rentals')
    bicycle = models.ForeignKey(Bicycle, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
