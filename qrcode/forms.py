# forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import CustomForm, FormField

class DynamicForm(forms.ModelForm):
    class Meta:
        model = CustomForm
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(DynamicForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

class DynamicFormFieldForm(forms.ModelForm):
    field_type = forms.ChoiceField(choices=[
        ('text', 'Text'),
        ('email', 'Email'),
        ('checkbox', 'Checkbox'),
        # Add other choices as needed
    ])

    class Meta:
        model = FormField
        fields = ['label', 'field_type', 'is_required']
