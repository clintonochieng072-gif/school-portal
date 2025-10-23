from django.contrib import admin
from .models import Student, Exam, JointExam, Remedial, ReamPaper


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "name", "school", "level", "grade_or_form",
        "admission_date_normalized", "date_of_birth_normalized",
        "parent_name", "parent_contact", "next_of_kin_name", "next_of_kin_contact",
        "disability", "sickness",
    )


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ("student", "subject", "score", "exam_date_normalized", "form_or_grade")


@admin.register(JointExam)
class JointExamAdmin(admin.ModelAdmin):
    list_display = ("student", "school", "exam_name", "subject", "score", "joint_exam_date_normalized", "form_or_grade")


@admin.register(Remedial)
class RemedialAdmin(admin.ModelAdmin):
    list_display = ("student", "subject", "remedial_date_normalized")


@admin.register(ReamPaper)
class ReamPaperAdmin(admin.ModelAdmin):
    list_display = ("student", "subject", "score", "ream_date_normalized")

# Register your models here.
