
from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import TaskForm
from webapp.models import Task
from webapp.models import status_choices


from webapp.utils import task_validate

def list_view(request):
    task = Task.objects.order_by("updated_at")
    return render(request, 'index.html', {'task': task})


def create_view(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'create.html', {'status_choices': status_choices, 'form': form})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = form.cleaned_data.get('task')
            status = form.cleaned_data.get('status')
            description = form.cleaned_data.get('description')
            updated_at = form.cleaned_data.get('updated_at')
            new_task = Task.objects.create(task=task, status=status, description=description, updated_at=updated_at)
            return redirect("view", pk=new_task.pk)

        return render(request, 'create.html', {'status_choices': status_choices, 'form': form})




def todo_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {"task": task}
    return render(request, 'view.html', context)

def view_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'GET':
        return render(request, 'edit.html', {'task': task, 'status_choices': status_choices})
    else:
        task.task = request.POST.get('task')
        task.status = request.POST.get('status')
        task.description = request.POST.get('description')
        task.updated_at = request.POST.get('updated_at')
        errors = task_validate(task.task, task.updated_at)
        if errors:
            return render(request, 'edit.html', {'status_choices': status_choices, 'errors': errors, 'task': task})


        task.save()

        return redirect("view", pk=task.pk)

def view_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'GET':
        return render(request, 'delete.html',{'task': task})
    else:
        task.delete()
        return redirect("index")

