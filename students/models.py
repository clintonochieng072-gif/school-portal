from django.db import models

# Create your models here.
from django.db import models
from decimal import Decimal

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    admission_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)  # optional
    admitted_date = models.DateField()  # mandatory
    grade = models.CharField(max_length=50)   # e.g., Form 1
    active = models.BooleanField(default=True)
    parent_contact = models.CharField(max_length=20, blank=True)  # optional
    parent_email = models.EmailField(blank=True)  # optional
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.admission_number} - {self.first_name} {self.last_name}"

class FeeRecord(models.Model):
    FEE_TYPE_CHOICES = [
        ('school_fee', 'School Fee'),
        ('ream_paper', 'Ream Paper'),
        ('remedial_fee', 'Remedial Fee'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='fee_records')
    fee_type = models.CharField(max_length=20, choices=FEE_TYPE_CHOICES)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    payment_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    @property
    def balance(self):
        due = self.amount_due or Decimal('0.00')
        paid = self.amount_paid or Decimal('0.00')
        return due - paid


    def save(self, *args, **kwargs):
        if self.amount_paid > self.amount_due:
            raise ValueError("Amount paid cannot exceed amount due")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.admission_number} - {self.get_fee_type_display()} - {self.amount_due}"
