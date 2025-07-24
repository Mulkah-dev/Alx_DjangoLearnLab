from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.TextField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title


# Roles
ROLE_CHOICES = (
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
)


# === Custom User Manager ===
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, role, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field is required.")
        if not username:
            raise ValueError("The Username field is required.")
        if not role:
            raise ValueError("The Role is required.")
        
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            role=role,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'Admin')

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, role='Admin', password=password, **extra_fields)

# === Custom User Model ===
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profiles/', null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    objects = CustomUserManager()

    def __str__(self):
        return self.username