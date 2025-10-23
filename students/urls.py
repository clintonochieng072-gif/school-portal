from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("admit/", views.admit_student, name="admit_student"),
    path("record-joint-exam/", views.record_joint_exam, name="record_joint_exam"),
    path("joint-exam-ranking/", views.joint_exam_ranking, name="joint_exam_ranking"),
]
