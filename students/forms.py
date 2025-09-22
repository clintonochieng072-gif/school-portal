from django import forms
from .models import Student, FeeRecord, ExamResult, JointExamResult

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class FeeRecordForm(forms.ModelForm):
    class Meta:
        model = FeeRecord
        fields = '__all__'

class ExamResultForm(forms.ModelForm):
    class Meta:
        model = ExamResult
        fields = '__all__'

class JointExamResultForm(forms.ModelForm):
    class Meta:
        model = JointExamResult
        fields = '__all__'
