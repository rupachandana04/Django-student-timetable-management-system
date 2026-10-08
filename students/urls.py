from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='root'),
    path('home/', views.home, name='home'),

    path('add/', views.add_student, name='add_student'),
    path('students/', views.view_students, name='view_students'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]