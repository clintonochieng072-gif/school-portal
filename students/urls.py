from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admit/', views.admit_student, name='admit_student'),
    path('exam/', views.record_exam, name='record_exam'),
    path('fees/', views.record_fee, name='record_fee'),
    path('joint-exam/', views.record_joint_exam, name='record_joint_exam'),
]
