from django.db import models

from user.models import User


class Task(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False, verbose_name='Название задачи')
    description = models.TextField(max_length=256, blank=True, null=True, verbose_name='Описание задачи')
    urgency = models.BooleanField(default=True, verbose_name='Срочность задачи')
    importancy = models.BooleanField(default=True, verbose_name='Важность задачи')
    is_active = models.BooleanField(default=True, verbose_name='Активна ли задача')

    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Владелец задачи')

    class Meta:
        db_table = 'task'
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        ordering = ('id',)

    def __str__(self) -> str:
        return f"{self.name}"
    
    