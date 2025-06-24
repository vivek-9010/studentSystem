from django.db import migrations

def populate_students(apps, schema_editor):
    Student = apps.get_model('students', 'Student')
    for student in Student.objects.all():
        # Set default values for each student
        if not student.roll:
            student.roll = student.id  # Or generate a unique roll number
        if not student.name:
            student.name = "Student " + str(student.id)
        if not student.gender:
            student.gender = 'O'  # Default to 'Other'
        if not student.branch:
            student.branch = "UNKNOWN"
        if not student.year_of_study:
            student.year_of_study = 1
        if not student.email:
            student.email = f"student{student.id}@example.com"
        student.save()

class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_students),
    ]