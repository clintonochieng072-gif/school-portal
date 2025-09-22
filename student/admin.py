# students/admin.py
from django.contrib import admin
from .models import Student, FeeRecord, Subject, Enrollment, ExamResult, JointExamResult

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "level_of_study", "grade", "form", "admission_date")
    list_filter = ("level_of_study", "grade", "form")
    search_fields = ("first_name", "last_name", "parent_guardian_name")

@admin.register(FeeRecord)
class FeeRecordAdmin(admin.ModelAdmin):
    list_display = ("student", "year", "term", "school_fee", "ream_paper_fee", "remedial_fee")
    list_filter = ("year", "term")

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "level_of_study")
    list_filter = ("level_of_study",)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("student", "subject")

@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
    list_display = ("student", "subject", "marks", "exam_date")
    list_filter = ("exam_date",)

@admin.register(JointExamResult)
class JointExamResultAdmin(admin.ModelAdmin):
    list_display = ("student_name", "school_name", "subject", "marks", "exam_date")
    list_filter = ("school_name", "exam_date")
    search_fields = ("student_name", "school_name")
