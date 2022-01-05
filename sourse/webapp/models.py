from django.db import models

# Create your models here.
status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]

class Task(models.Model):
    task = models.CharField(max_length=200, null=False, blank=False, verbose_name="Задача")
    status = models.CharField(max_length=30, null=False, blank=False, default="new", choices=status_choices, verbose_name="Статус")
    description = models.TextField(max_length=2000, null=True, blank=False, default="Подробного описания нет", verbose_name="Описание")
    updated_at = models.DateField(auto_now=False,null=None, blank=False, verbose_name="Дедлайн")

    def __str__(self):
        return f"{self.pk}.  {self.task}: {self.status} / {self.updated_at}"

    class Meta:
        db_table = 'todo'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'