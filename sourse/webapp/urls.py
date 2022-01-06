
from django.urls import path

from webapp.views import create_view, list_view, todo_view, view_edit, view_delete

urlpatterns = [
    path('', list_view, name="index"),
    path('add/', create_view, name="create"),
    path('view/<int:pk>/', todo_view, name='view'),
    path('view/<int:pk>/edit/', view_edit, name='edit'),
    path('view/<int:pk>/delete', view_delete, name='delete')
]