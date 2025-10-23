from django import forms
from .models import Student, Exam, JointExam, Remedial, ReamPaper

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = "__all__"

class JointExamForm(forms.ModelForm):
    class Meta:
        model = JointExam
        fields = "__all__"

class RemedialForm(forms.ModelForm):
    class Meta:
        model = Remedial
        fields = "__all__"

class ReamPaperForm(forms.ModelForm):
    class Meta:
        model = ReamPaper
        fields = "__all__"
