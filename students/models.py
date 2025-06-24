# students/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )

    # Make all new fields nullable temporarily
    roll = models.IntegerField(unique=True, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    branch = models.CharField(max_length=100, null=True, blank=True)
    year_of_study = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        null=True,
        blank=True
    )
    email = models.EmailField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    phone_number = models.CharField(
        max_length=15,
        validators=[phone_regex],
        blank=True,
        null=True
    )
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    guardian_name = models.CharField(max_length=100, blank=True, null=True)
    guardian_phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        validators=[phone_regex]
    )
    admission_date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.roll} - {self.name}" if self.roll else f"Unnamed Student {self.id}"

    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.title()
        if self.branch:
            self.branch = self.branch.upper()
        super().save(*args, **kwargs)

    def clean(self):
        if self.date_of_birth and self.date_of_birth > timezone.now().date():
            raise ValidationError("Date of birth cannot be in the future")
        super().clean()