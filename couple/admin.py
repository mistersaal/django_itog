from django.contrib import admin
from .models import Subjects, Speciality, Teachers, Classrooms, Groups, Student, Couple
# Register your models here.
admin.site.register(Subjects)
admin.site.register(Speciality)
admin.site.register(Teachers)
admin.site.register(Classrooms)
admin.site.register(Groups)
admin.site.register(Student)
admin.site.register(Couple)
