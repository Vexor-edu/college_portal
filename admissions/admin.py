from django.contrib import admin
from .models import StudentApplication
from .models import FacultyMember

from django.utils.html import format_html

class StudentApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'course', 'student_id', 'submitted_at', 'print_button')
    search_fields = ('full_name', 'email')
    
    # Add Print Button to List View
    def print_button(self, obj):
      return format_html(
        '<a class="button" href="/print/{}/" target="_blank">🖨️ Print</a>',
        obj.pk
    )

    print_button.short_description = 'Print Application'
    print_button.allow_tags = True  # Allow HTML rendering in the column

    # Optionally, you can remove the 'Print' button from the list view and add it in individual view
    # Add Print button to list_display
    list_display = ('full_name', 'email', 'course', 'student_id', 'submitted_at', 'print_button')

admin.site.register(StudentApplication, StudentApplicationAdmin)
admin.site.register(FacultyMember)


