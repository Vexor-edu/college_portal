from django.shortcuts import render, redirect
from .forms import StudentApplicationForm
from django.contrib import messages
from .models import FacultyMember, StudentApplication


def student_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        dob = request.POST.get('dob')  # Assume date input

        try:
            student = StudentApplication.objects.get(email=email, dob=dob)
            request.session['student_id'] = student.id
            return redirect('student_dashboard')
        except StudentApplication.DoesNotExist:
            messages.error(request, "Invalid credentials. Please try again.")

    return render(request, 'admissions/login.html')


def student_dashboard(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('student_login')

    student = StudentApplication.objects.get(id=student_id)
    return render(request, 'admissions/student_dashboard.html', {'student': student})



def home(request):
    return render(request, 'admissions/home.html')


def apply(request):
    if request.method == 'POST':
        form = StudentApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to same page with query param
            return redirect('/apply/?submitted=true')
        else:
            messages.error(request, "❌ Please fix the errors below.")
    else:
        form = StudentApplicationForm()

    # Check if ?submitted=true is in URL to trigger SweetAlert
    submitted = request.GET.get('submitted') == 'true'
    return render(request, 'admissions/apply.html', {
        'form': form,
        'submitted': submitted
    })


def contact(request):
    return render(request, 'admissions/contact.html')


def faculty_page(request):
    departments = {}
    for member in FacultyMember.objects.all():
        dept = member.department
        departments.setdefault(dept, []).append(member)
    return render(request, 'admissions/faculty.html', {'departments': departments})


