from django.contrib import admin
from .models import Student, FeeRecord

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('admission_number', 'first_name', 'last_name', 'grade', 'admitted_date', 'active')
    search_fields = ('admission_number', 'first_name', 'last_name')
    list_filter = ('grade', 'active')
    fieldsets = (
        (None, {'fields': ('admission_number', 'first_name', 'last_name', 'gender', 'date_of_birth', 'admitted_date', 'grade', 'active')}),
        ('Parent Info', {'fields': ('parent_contact', 'parent_email')}),
        ('Additional', {'fields': ('notes',)}),
    )

@admin.register(FeeRecord)
class FeeRecordAdmin(admin.ModelAdmin):
    list_display = ('student', 'fee_type', 'amount_due', 'amount_paid', 'balance', 'payment_date')
    search_fields = ('student__first_name', 'student__last_name', 'student__admission_number')
    list_filter = ('fee_type', 'payment_date')
    readonly_fields = ('balance',)
    autocomplete_fields = ('student',)   

