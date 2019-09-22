from django.contrib import admin

# Register your models here.

from myapp.models import  Grade,Student
class GradeAdmin(admin.ModelAdmin):
    list_display = ['id','gid','name','add_date']
    listfilter=['name']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','sid','name','add_date']

admin.site.register(Grade,GradeAdmin)
admin.site.register(Student,StudentAdmin)
