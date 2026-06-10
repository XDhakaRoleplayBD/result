from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('results/', views.result_page, name='results'),

    path('teacher-login/', views.teacher_login, name='teacher_login'),
    path('student-login/', views.student_login, name='student_login'),

    path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),

    path('upload-result/', views.upload_result, name='upload_result'),
    path('delete-result/<int:id>/', views.delete_result, name='delete_result'),

    path('logout/', views.user_logout, name='logout'),
]