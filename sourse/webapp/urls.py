
from django.urls import path

from webapp.views import create_view, list_view, todo_view

urlpatterns = [
    path('', list_view, name="index"),
    path('add/', create_view, name="create"),
    path('view/<int:pk>/', todo_view, name='view')
]