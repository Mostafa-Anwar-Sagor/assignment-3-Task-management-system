from django import forms
from .models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['taskTitle', 'taskDescription', 'is_completed', 'categories']
        widgets = {
            'categories': forms.CheckboxSelectMultiple(),
        }
