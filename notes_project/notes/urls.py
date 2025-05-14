from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('create/', views.create_note, name='create_note'),
    path('edit/<int:pk>/', views.edit_note, name='edit_note'),
    path('delete/<int:pk>/', views.delete_note, name='delete_note'),
    path('note/<int:pk>/', views.view_note, name='view_note'),

# Auth
    path('login/', auth_views.LoginView.as_view(template_name='notes/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
