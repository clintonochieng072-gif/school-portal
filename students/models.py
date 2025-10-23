from django.db import models
from dateutil import parser

class Student(models.Model):
    LEVEL_CHOICES = [
        ("Primary", "Primary"),
        ("Secondary", "Secondary"),
    ]

    name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES)
    grade_or_form = models.CharField(max_length=20, blank=True, null=True)
    admission_date = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.CharField(max_length=50, blank=True, null=True)
    parent_name = models.CharField(max_length=100, blank=True, null=True)
    parent_contact = models.CharField(max_length=20, blank=True, null=True)
    next_of_kin_name = models.CharField(max_length=100, blank=True, null=True)
    next_of_kin_contact = models.CharField(max_length=20, blank=True, null=True)
    disability = models.BooleanField(default=False)
    sickness = models.BooleanField(default=False)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.level})"

    def normalize_date(self, raw_date):
        if not raw_date:
            return ""
        try:
            return parser.parse(raw_date).strftime("%Y-%m-%d")
        except Exception:
            return raw_date

    @property
    def admission_date_normalized(self):
        return self.normalize_date(self.admission_date)

    @property
    def date_of_birth_normalized(self):
        return self.normalize_date(self.date_of_birth)


class Exam(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    score = models.IntegerField()
    exam_date = models.CharField(max_length=50, blank=True, null=True)
    form_or_grade = models.CharField(max_length=20, blank=True, null=True)

    def normalize_date(self, raw_date):
        if not raw_date:
            return ""
        try:
            return parser.parse(raw_date).strftime("%Y-%m-%d")
        except Exception:
            return raw_date

    @property
    def exam_date_normalized(self):
        return self.normalize_date(self.exam_date)


class JointExam(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    school = models.CharField(max_length=100)
    exam_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    score = models.IntegerField()
    joint_exam_date = models.CharField(max_length=50, blank=True, null=True)
    form_or_grade = models.CharField(max_length=20, blank=True, null=True)

    def normalize_date(self, raw_date):
        if not raw_date:
            return ""
        try:
            return parser.parse(raw_date).strftime("%Y-%m-%d")
        except Exception:
            return raw_date

    @property
    def joint_exam_date_normalized(self):
        return self.normalize_date(self.joint_exam_date)


class Remedial(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, limit_choices_to={'level': 'Secondary'})
    subject = models.CharField(max_length=100)
    remedial_date = models.CharField(max_length=50, blank=True, null=True)

    def normalize_date(self, raw_date):
        if not raw_date:
            return ""
        try:
            return parser.parse(raw_date).strftime("%Y-%m-%d")
        except Exception:
            return raw_date

    @property
    def remedial_date_normalized(self):
        return self.normalize_date(self.remedial_date)


class ReamPaper(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, limit_choices_to={'level': 'Secondary'})
    subject = models.CharField(max_length=100)
    score = models.IntegerField()
    ream_date = models.CharField(max_length=50, blank=True, null=True)

    def normalize_date(self, raw_date):
        if not raw_date:
            return ""
        try:
            return parser.parse(raw_date).strftime("%Y-%m-%d")
        except Exception:
            return raw_date

    @property
    def ream_date_normalized(self):
        return self.normalize_date(self.ream_date)

# Create your models here.
