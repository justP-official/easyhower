from django import forms

from tasks.models import Task


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'urgency', 'importancy']

    name = forms.CharField()
    description = forms.CharField()
    urgency = forms.ChoiceField(
        choices=[
            ("0", False),
            ("1", True)
        ]
    )
    importancy = forms.ChoiceField(
        choices=[
            ("0", False),
            ("1", True)
        ]
    )

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'urgency', 'importancy']

    name = forms.CharField()
    description = forms.CharField()
    urgency = forms.ChoiceField(
        choices=[
            ("0", False),
            ("1", True)
        ]
    )
    importancy = forms.ChoiceField(
        choices=[
            ("0", False),
            ("1", True)
        ]
    )
    