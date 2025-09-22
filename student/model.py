# students/models.py
from django.db import models
from django.utils import timezone

# Choices
LEVEL_CHOICES = [
    ('primary', 'Primary School'),
    ('secondary', 'Secondary School'),
]

GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
]

# -----------------------------
# Student Model
# -----------------------------
class Student(models.Model):
    level_of_study = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    admission_date = models.DateField(default=timezone.now)

    # Personal details
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    # Parent/guardian and next of kin
    parent_guardian_name = models.CharField(max_length=150, blank=True, null=True)
    parent_guardian_contact = models.CharField(max_length=20, blank=True, null=True)
    next_of_kin_name = models.CharField(max_length=150, blank=True, null=True)
    next_of_kin_contact = models.CharField(max_length=20, blank=True, null=True)

    # Health
    has_disability = models.BooleanField(default=False)
    has_sickness = models.BooleanField(default=False)
    health_notes = models.TextField(blank=True, null=True)

    # Academic placement
    grade = models.CharField(max_length=20, blank=True, null=True, help_text="For primary school students")
    form = models.CharField(max_length=20, blank=True, null=True, help_text="For secondary school students")

    def save(self, *args, **kwargs):
        # Ensure grade is only for primary and form only for secondary
        if self.level_of_study == 'primary':
            self.form = None
        elif self.level_of_study == 'secondary':
            self.grade = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name or ''} {self.last_name or ''} - {self.level_of_study}"


# -----------------------------
# Fee Model
# -----------------------------
class FeeRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="fees")
    year = models.IntegerField(default=timezone.now().year)
    term = models.IntegerField(choices=[(1, "Term 1"), (2, "Term 2"), (3, "Term 3")], blank=True, null=True)

    # Core fee
    school_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # Secondary-only fees
    ream_paper_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                         help_text="Applies per term (Secondary only)")
    remedial_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                       help_text="Applies once per year (Secondary only)")

    def __str__(self):
        return f"Fees {self.student} - {self.year} Term {self.term}"


# -----------------------------
# Subject Model
# -----------------------------
class Subject(models.Model):
    name = models.CharField(max_length=100)
    level_of_study = models.CharField(max_length=20, choices=LEVEL_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.level_of_study})"


# -----------------------------
# Enrollment Model (student-subject link)
# -----------------------------
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="enrollments")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="enrollments")

    def __str__(self):
        return f"{self.student} enrolled in {self.subject}"


# -----------------------------
# Exam Results (normal school exams)
# -----------------------------
class ExamResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="exam_results")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    exam_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.student} - {self.subject}: {self.marks}"


# -----------------------------
# Joint Exam Results (multiple schools)
# -----------------------------
class JointExamResult(models.Model):
    student_name = models.CharField(max_length=150)
    school_name = models.CharField(max_length=150)
    subject = models.CharField(max_length=100)
    marks = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    exam_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.student_name} ({self.school_name}) - {self.subject}: {self.marks}"
