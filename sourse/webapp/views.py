from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from webapp.models import Task


def list_view(request):
    task = Task.objects.order_by("updated_at")
    return render(request, 'index.html', {'task': task})


def create_view(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    else:
        task = request.POST.get('task')
        status = request.POST.get('status')
        new_task = Task.objects.create(task=task, status=status)
        context = {"article": new_task}

        return render(request, 'view.html', context)


def todo_view(request):
    pk = request.GET.get("pk")
    task = Task.objects.get(pk=pk)
    context = {"task": task}
    return render(request, 'view.html', context)
