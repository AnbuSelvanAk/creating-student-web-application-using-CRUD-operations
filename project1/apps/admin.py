from django.contrib import admin
from apps.models import Student
class StudentAdmin (admin.ModelAdmin):
	list_display=['sno','sname','salary','saddress']

admin.site.register(Student)