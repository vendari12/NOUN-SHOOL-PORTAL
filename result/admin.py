from django.contrib import admin
from .models import *
class ScoreAdmin(admin.ModelAdmin):
	list_display = ['student', 'course', 'ca', 'exam', 'total', 'grade', 'comment']

class AllocationAdmin(admin.ModelAdmin):
	list_display = ['lecturer',]

class ResultAdmin(admin.ModelAdmin):
	list_display = ['student', 'gpa', 'semester', 'level', 'cgpa']

class FacultyAdmin(admin.ModelAdmin):
	list_display = [ 'title', 'department']	

class DepartmentAdmin(admin.ModelAdmin):
	list_display = ['title', ]


admin.site.register(Semester)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(CourseAllocation, AllocationAdmin)
admin.site.register(TakenCourse, ScoreAdmin)
admin.site.register(Session)
admin.site.register(User)
admin.site.register(CarryOverStudent)
admin.site.register(RepeatingStudent)
admin.site.register(Result, ResultAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Department, DepartmentAdmin)


