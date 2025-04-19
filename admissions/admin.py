from django.contrib import admin, messages
from .models import StudentApplication, FacultyMember
from django.utils.html import format_html
from django.urls import path
from django.shortcuts import get_object_or_404, redirect

class StudentApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'course', 'student_id', 'submitted_at', 'status', 'print_button', 'action_buttons')
    list_filter = ('status', 'course')
    search_fields = ('full_name', 'email', 'student_id')
    actions = ['approve_selected', 'reject_selected']

    # 🖨️ Print Button
    def print_button(self, obj):
        return format_html(
            '<a class="button" href="/print/{}/" target="_blank">🖨️ Print</a>',
            obj.pk
        )
    print_button.short_description = 'Print'

    # ✅ Action Buttons (Approve / Reject)
    def action_buttons(self, obj):
        if obj.status == 'pending':
            return format_html(
                '<a class="button" style="color:green;" href="approve/{}/">✅ Approve</a>&nbsp;&nbsp;'
                '<a class="button" style="color:red;" href="reject/{}/">❌ Reject</a>',
                obj.pk, obj.pk
            )
        elif obj.status == 'approved':
            return format_html('<span style="color:green;">✔️ Approved</span>')
        elif obj.status == 'rejected':
            return format_html('<span style="color:red;">❌ Rejected</span>')

    action_buttons.short_description = 'Actions'

    # 🔧 Custom Admin URLs
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('approve/<int:application_id>/', self.admin_site.admin_view(self.approve_application)),
            path('reject/<int:application_id>/', self.admin_site.admin_view(self.reject_application)),
        ]
        return custom_urls + urls

    def approve_application(self, request, application_id):
        application = get_object_or_404(StudentApplication, pk=application_id)
        application.status = 'approved'
        application.save()
        self.message_user(request, f"{application.full_name} has been approved ✅", level=messages.SUCCESS)
        return redirect(request.META.get('HTTP_REFERER'))

    def reject_application(self, request, application_id):
        application = get_object_or_404(StudentApplication, pk=application_id)
        application.status = 'rejected'
        application.save()
        self.message_user(request, f"{application.full_name} has been rejected ❌", level=messages.WARNING)
        return redirect(request.META.get('HTTP_REFERER'))

    # ✅ Bulk Admin Actions
    def approve_selected(self, request, queryset):
        updated = queryset.update(status='approved')
        self.message_user(request, f"{updated} application(s) approved ✅", level=messages.SUCCESS)

    def reject_selected(self, request, queryset):
        updated = queryset.update(status='rejected')
        self.message_user(request, f"{updated} application(s) rejected ❌", level=messages.WARNING)

admin.site.register(StudentApplication, StudentApplicationAdmin)
admin.site.register(FacultyMember)
