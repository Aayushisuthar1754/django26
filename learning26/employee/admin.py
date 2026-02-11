from sched import Event
from django.contrib import admin
from .models import Employee, Course ,Library,Event
admin.site.register(Employee)
admin.site.register(Course)
admin.site.register(Library)
admin.site.register(Event)