from django import forms
from django.forms import widgets

from webapp.models import status_choices


class TaskForm(forms.Form):
    task = forms.CharField(max_length=200, required=True, label="Задача")
    status = forms.ChoiceField(choices=status_choices, required=True, label="Статус", initial=status_choices[0][1])
    description = forms.CharField(max_length=200, required=True, label="Описание", widget=widgets.Textarea(attrs={'rows':5, 'cols-':50}))
    updated_at = forms.CharField(required=True, label="Дата",widget=widgets.DateTimeInput)
