from django.db import models

class StudentApplication(models.Model):
    full_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    COURSE_CHOICES = [
    ('BTECH', 'B.Tech'),
    ('MTECH', 'M.Tech'),
    ('BCA', 'BCA'),
    ('MCA', 'MCA'),
    ('MBA', 'MBA'),
    ('BBA', 'BBA'),
    ('BSC', 'B.Sc.')]

    course = models.CharField(max_length=10, choices=COURSE_CHOICES)

    photo = models.FileField(upload_to='photo/')
    document = models.FileField(upload_to='documents/')
    signature = models.FileField(upload_to='signature/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

# for faculty

# admissions/models.py
class FacultyMember(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, choices=[
        ('Physics', 'B.Sc. Physics'),
        ('Chemistry', 'B.Sc. Chemistry'),
        ('Electronics', 'B.Sc. Electronics'),
        ('Math', 'B.Sc. Mathematics'),
        ('CS', 'Computer Science'),
        ('BioMed', 'Biomedical Science'),
        ('Botany', 'Botany'),
        ('Zoology', 'Zoology'),
        ('BCom', 'B.Com'),
    ])
    photo = models.ImageField(upload_to='faculty_photos/')
    email = models.EmailField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name
