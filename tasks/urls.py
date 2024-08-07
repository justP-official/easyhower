from django.urls import path

from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('tasks/', views.TasksView.as_view(), name='tasks'),
    path('create-task/', views.CreateTask.as_view(), name='create_task'),
    path('read-task/<int:task_id>/', views.ReadTask.as_view(), name='read_task'),
    path('update-task/<int:task_id>/', views.UpdateTask.as_view(), name='update_task'),
    path('delete-task/<int:task_id>/', views.DeleteTask.as_view(), name='delete_task'),
    path('complate-task/<int:task_id>/', views.ComplateTask.as_view(), name='complate_task'),
]