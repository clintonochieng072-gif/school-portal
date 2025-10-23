"""
URL configuration for portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path
from students import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.student_list, name="student_list"),  # root URL shows student list
    path("home/", views.home, name="home"),
    path("admit/", views.admit_student, name="admit_student"),
    path("joint-exam/", views.record_joint_exam, name="record_joint_exam"),
    path("ranking/", views.joint_exam_ranking, name="joint_exam_ranking"),
]
