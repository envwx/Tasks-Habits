from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('tasks/<int:task_id>/', views.task_details, name= 'task_details'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:task_id>/edit/', views.task_edit, name='task_edit'),
    path('tasks/<int:task_id>/delete/', views.task_delete, name='task_delete'),
    path('tasks/<int:task_id>/complete/', views.task_complete, name='task_complete'),
    path('habits/<int:habit_id>/', views.habit_details, name= 'habit_details'),
    path('habits/', views.habit_list, name='habit_list'),
    path('habits/create/', views.habit_create, name='habit_create'),
    path('habits/<int:habit_id>/edit/', views.habit_edit, name='habit_edit'),
    path('habits/<int:habit_id>/delete/', views.habit_delete, name='habit_delete'),
    path('habits/<int:habit_id>/complete/', views.habit_complete, name='habit_complete'),
]
