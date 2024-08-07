from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from tasks.forms import CreateTaskForm, UpdateTaskForm
from tasks.models import Task


class TasksView(LoginRequiredMixin, ListView):
    template_name = "tasks/tasks.html"
    context_object_name = 'tasks'
    extra_context = {"title": "Easyhower - Задачи",}

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user, is_active=True)
        

class CreateTask(LoginRequiredMixin, CreateView):
    form_class = CreateTaskForm
    success_url = reverse_lazy("tasks:tasks")

    def form_valid(self, form):
        form.instance.owner = self.request.user

        return super().form_valid(form)


class ReadTask(LoginRequiredMixin, DetailView):
    pk_url_kwarg = 'task_id'
    template_name = 'tasks/includes/task_info.html'
    context_object_name = 'task'

    def get(self, request, task_id):
        task = self.get_object(task_id)
        task_info_html = render_to_string(
                self.template_name, 
                {self.context_object_name: task}, 
                request=request
            )

        response_data = {"html": task_info_html}

        return JsonResponse(response_data)
    
    def get_object(self, task_id, queryset=None):
        return Task.objects.get(id=task_id)
        

class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = UpdateTaskForm
    success_url = reverse_lazy('tasks:tasks')
    pk_url_kwarg = 'task_id'


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:tasks')
    pk_url_kwarg = 'task_id'


class ComplateTask(LoginRequiredMixin, View):
    def get(self, request, task_id):
        task = self.get_object(task_id)
        task.is_active = False
        task.save()

        user = task.owner
        user.complate_tasks_quantity += 1
        user.save()

        return HttpResponseRedirect(reverse_lazy('tasks:tasks'))
    
    def get_object(self, task_id, queryset=None):
        return Task.objects.get(id=task_id)
