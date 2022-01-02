from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from webapp.models import Task
from webapp.models import status_choices


def list_view(request):
    task = Task.objects.order_by("updated_at")
    return render(request, 'index.html', {'task': task})


def create_view(request):
    if request.method == 'GET':
        return render(request, 'create.html', {'status_choices': status_choices})
    else:
        task = request.POST.get('task')
        status = request.POST.get('status')
        updated_at = request.POST.get('updated_at')
        new_task = Task.objects.create(task=task, status=status, updated_at=updated_at)

        return HttpResponseRedirect(f"/view/{new_task.pk}")



def todo_view(request, pk):
    task = Task.objects.get(pk=pk)
    context = {"task": task}
    return render(request, 'view.html', context)
