from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    join_date = models.DateField(auto_now_add=True)
    post = models.CharField(max_length=100)

    class Meta:
        db_table = "employee"
        
    def __str__(self):
        return self.name
    

class Course(models.Model):
    name = models.CharField(max_length=100)
    fee = models.IntegerField()
    duration = models.IntegerField()

    class Meta:
        db_table = "course"

    def __str__(self):
        return self.name


class Library(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    class Meta:
        db_table="library"

    def __str__(self):
        return self.name
    
class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

    class Meta:
        db_table = "event"

    def __str__(self):
        return self.name
