from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.template.defaultfilters import slugify


class Broker(AbstractBaseUser):
    name = models.CharField(max_length=80, blank=False, null=False)
    email = models.EmailField(
        max_length=200, blank=False, null=False, unique=True)
    password = models.CharField(max_length=255, blank=False, null=False)
    telephone_number = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    objects = UserManager()

    class Meta:
        permissions = [
            ('create_house', 'Can create a house model')
        ]

    def __str__(self):
        return self.name

    def id(self):
        return self.id

    def get_absolute_url(self):
        return reverse('home')

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class House(models.Model):
    title = models.CharField(max_length=120)
    price = models.CharField(max_length=40)
    plot = models.CharField(max_length=10)
    bathrooms = models.CharField(max_length=10)
    bedrooms = models.CharField(max_length=10)
    living_space = models.CharField(max_length=15)
    plot_size = models.CharField(max_length=15)
    description = models.TextField(max_length=1500)
    image = models.ImageField(max_length=1000)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    broker = models.ForeignKey(
        Broker, null=True, on_delete=models.CASCADE)
    slug = models.SlugField(null=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("houseView", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
