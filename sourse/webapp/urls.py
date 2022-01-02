
from django.urls import path

from webapp.views import create_view, list_view, todo_view

urlpatterns = [
    path('', list_view),
    path('add/', create_view),
    path('view/<int:pk>/', todo_view)
]