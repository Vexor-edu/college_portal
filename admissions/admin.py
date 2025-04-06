from django.contrib import admin
from .models import StudentApplication
from .models import FacultyMember

admin.site.register(StudentApplication)
admin.site.register(FacultyMember)

