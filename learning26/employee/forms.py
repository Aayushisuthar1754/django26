from django import forms
from . import models

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = models.Employee
        exclude = ['join_date']  

class CourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = '__all__'


class LibraryForm(forms.ModelForm):
    class Meta:
        model = models.Library
        fields = '__all__'

class EventForm(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = '__all__'

           