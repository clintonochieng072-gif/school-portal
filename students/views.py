from django.shortcuts import render, redirect
from django.db.models import Avg
from .forms import StudentForm, JointExamForm
from .models import JointExam, Student  # <-- Make sure Student model exists

def home(request):
    return render(request, "students/home.html")

def admit_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            if student.level == "Primary":
                student.grade_or_form = f"Grade {student.grade_or_form}"
            elif student.level == "Secondary":
                student.grade_or_form = f"Form {student.grade_or_form}"
            student.save()
            return redirect("home")
    else:
        form = StudentForm()
    return render(request, "students/admit_student.html", {"form": form})

def record_joint_exam(request):
    if request.method == "POST":
        form = JointExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("joint_exam_ranking")
    else:
        form = JointExamForm()
    return render(request, "students/record_joint_exam.html", {"form": form})

def joint_exam_ranking(request):
    exams = JointExam.objects.all().order_by("-score")
    school_means = (
        JointExam.objects.values("school")
        .annotate(mean_score=Avg("score"))
        .order_by("-mean_score")
    )
    return render(request, "students/joint_exam_ranking.html", {"student_ranking": exams, "school_means": school_means})

# --------------------------
# NEW: Student list view
# --------------------------
def student_list(request):
    students = Student.objects.all()
    return render(request, "students/student_list.html", {"students": students})
